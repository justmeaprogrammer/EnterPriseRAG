from bs4 import BeautifulSoup

def parse_html(file_path:str):
    with open(file_path,'r',encoding='utf-8') as f:
        content=f.read()
        
        soup = BeautifulSoup(content,"html.parser")
        
        #Removing junk
        for tag in soup(["script", "style", "meta", "noscript"]):
            tag.decompose()
            
        ##Extract the text
        text = soup.get_text(separator="\n")
        
        
        ##clean white spaces
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
        text_clean = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text_clean