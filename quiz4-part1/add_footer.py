"""Inject a centered page-number footer into a pandoc-generated .docx file."""
import zipfile, shutil, re, sys

FOOTER_XML = """\
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
       xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText xml:space="preserve"> PAGE \\* MERGEFORMAT </w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="separate"/></w:r>
    <w:r><w:t>1</w:t></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
  </w:p>
</w:ftr>"""

REL  = '<Relationship Id="rIdFtr1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
CT   = '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
REF  = '<w:footerReference w:type="default" r:id="rIdFtr1"/>'

def patch(path: str) -> None:
    tmp = path + ".tmp"
    with zipfile.ZipFile(path, "r") as zin, \
         zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            fn   = item.filename

            if fn == "word/_rels/document.xml.rels":
                s = data.decode("utf-8")
                if "rIdFtr1" not in s:
                    s = s.replace("</Relationships>", REL + "\n</Relationships>")
                data = s.encode("utf-8")

            elif fn == "[Content_Types].xml":
                s = data.decode("utf-8")
                if "footer1.xml" not in s:
                    s = s.replace("</Types>", CT + "\n</Types>")
                data = s.encode("utf-8")

            elif fn == "word/document.xml":
                s = data.decode("utf-8")
                if "rIdFtr1" not in s:
                    s = re.sub(r"(</w:sectPr>)", REF + r"\1", s)
                data = s.encode("utf-8")

            zout.writestr(item, data)

        zout.writestr("word/footer1.xml", FOOTER_XML)

    shutil.move(tmp, path)
    print(f"Page-number footer injected → {path}")

if __name__ == "__main__":
    patch(sys.argv[1])
