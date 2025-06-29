from docx import Document

def parse_docx(input_file):
    try:
        document = Document(input_file)
        text = []
        for paragraph in document.paragraphs:
            text.append(paragraph.text)
        return "\n".join(text)
    except Exception as e:
        return ""
