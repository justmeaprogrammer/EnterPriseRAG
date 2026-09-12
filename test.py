from app.ingestion.loaders import pdf_extractor
from app.ingestion.loaders import html_extractor
from app.ingestion.loaders import docx_extractor
from app.ingestion.loaders import pptx_parser
from app.ingestion.loaders import text

def smart_parser(file_path:str):
    ext = file_path.split('.')[-1]
    if ext=="pdf":
        return pdf_extractor.parse_pdf(file_path=file_path)
    
    elif ext=="html":
        return html_extractor.parse_html(file_path=file_path)
    
    elif ext=="docx":
        return docx_extractor.parse_docx(file_path=file_path)
    
    elif ext=="pptx":
        return pptx_parser.parse_ppt(file_path=file_path)
    
    elif ext=="txt":
        return text.parse_txt(file_path=file_path)
        
    
    
    else:
        return "Incompatible File Extension"
        

doc="/home/om/projects/EnterpriseRAG/sample/sample.docx"
html="/home/om/projects/EnterpriseRAG/sample/sample.html"
pdf="/home/om/projects/EnterpriseRAG/sample/sample.pdf"
ppt="/home/om/projects/EnterpriseRAG/sample/sample.pptx"
txt="/home/om/projects/EnterpriseRAG/sample/sample.txt"

print(smart_parser("txt.obj"))


    