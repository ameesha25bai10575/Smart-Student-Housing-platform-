import PyPDF2

def analyze_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    findings = []
    keywords = ["electricity","maintenance","penalty","brokerage","non-refundable"]

    for k in keywords:
        if k in text.lower():
            findings.append(k + " found")

    return findings