import pdfplumber

def clean_text(text:str)->str:
    lines = (line.strip() for line in text.splitlines())
    return '\n'.join(line for line in lines if line)
    
def parse_pdf(file_path:str)->str:
    text_parts=[]
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    text = '\n'.join(text_parts)
    return clean_text(text)

