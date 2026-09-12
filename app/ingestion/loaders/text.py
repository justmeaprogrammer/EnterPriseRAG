def clean_text(text:str)->str:
    lines = (line.strip() for line in text.splitlines())
    return "\n".join(line for line in lines if line)

def parse_txt(file_path:str):
    with open(file_path,'r',encoding='utf-8') as fileobj:
        text = fileobj.read()
        
    return clean_text(text)
        