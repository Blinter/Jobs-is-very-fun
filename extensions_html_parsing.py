import bs4
from bs4 import BeautifulSoup
from html2text import HTML2Text


def parse_webpage_bs4(html):
    """
    Convert HTML in page to text using Beautiful Soup
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Remove script tags
    for script in soup(['script', 'style']):
        script.extract()

    comments = soup.find_all(string=lambda text: isinstance(text, bs4.Comment))
    for comment in comments:
        comment.extract()

    paragraphs = soup.find_all('p')
    extracted_text = ''
    for paragraph in paragraphs:
        extracted_text += paragraph.get_text(strip=True) + '\n'

    divs = soup.find_all('div')
    extracted_text = ''
    for paragraph in paragraphs:
        extracted_text += paragraph.get_text(strip=True) + '\n'

    return extracted_text


def parse_webpage_bs4_html5lib(html):
    """
    Convert HTML in page to text using Beautiful Soup
    """
    soup = BeautifulSoup(html, 'html5lib')

    paragraphs = soup.find_all('p')
    extracted_text = ''
    for paragraph in paragraphs:
        extracted_text += paragraph.get_text(strip=True) + '\n'

    return extracted_text


def parse_webpage_html2text(html):
    """
    Use HTML2Text Library to convert HTML to text, converting links to markdown.
    """
    h = HTML2Text()
    h.ignore_links = False
    h.inline_links = True
    h.iwrap_links = True
    h.use_automatic_links = True
    h.ignore_mailto_links = False
    h.ignore_images = True
    h.single_line_break = True
    return h.handle(html)
