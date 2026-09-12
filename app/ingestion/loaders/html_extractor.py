from bs4 import BeautifulSoup

def parse_html(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    # Remove junk
    for tag in soup(["script", "style", "meta", "noscript"]):
        tag.decompose()

    # Extract text
    text = soup.get_text(separator="\n")

    # Collapse blank/whitespace-only lines, keep line structure intact
    lines = (line.strip() for line in text.splitlines())
    text_clean = '\n'.join(line for line in lines if line)

    return text_clean

# print(parse_html("/home/om/projects/EnterpriseRAG/sample/sample.html"))