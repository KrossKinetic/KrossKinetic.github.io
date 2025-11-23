import sys
try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("No PDF library found")
        sys.exit(1)

reader = PdfReader("/home/krosskinetic/main/KrossKinetic.github.io/Anshumaan_Singh_Resume_v2_1.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
print(text)
