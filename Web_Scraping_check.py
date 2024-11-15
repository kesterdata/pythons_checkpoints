import requests  
from bs4 import BeautifulSoup  

# 1.1 Function to Get and parse html content from a Wikipedia page  
def get_html_content(url):  
    response = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")  
    response.raise_for_status()  # Raise an error for bad responses  
    return response.text  

# 1.2 Function to Extract article title  
def extract_article_title(html):  
    soup = BeautifulSoup(html, 'html.parser')  
    title = soup.find('h1').text.strip()  # Title is inside the <h1> tag  
    return title  

# 1.3 Function to Extract article text for each paragraph with their respective headings  
def extract_paragraphs_with_headings(html):  
    soup = BeautifulSoup(html, 'html.parser')  
    content = {}  

    for heading in soup.find_all(['h2', 'h3', 'h4']):  # Collecting different heading levels  
        heading_text = heading.text.strip()  
        next_elem = heading.find_next_sibling()  
        paragraphs = []  

        while next_elem and next_elem.name not in ['h2', 'h3', 'h4']:  # Stop at next heading  
            if next_elem.name == 'p':  
                paragraphs.append(next_elem.text.strip())  
            next_elem = next_elem.find_next_sibling()  

        if paragraphs:  
            content[heading_text] = paragraphs  

    return content  

# 1.4 Function to collect every link that redirects to another Wikipedia page  
def collect_internal_wikipedia_links(html):  
    soup = BeautifulSoup(html, 'html.parser')  
    links = set()  

    for a in soup.find_all('a', href=True):  
        href = a['href']  
        if href.startswith('/wiki/') and not href.startswith('/wiki/File:'):  
            links.add('https://en.wikipedia.org' + href)  # Normalize to full URL  

    return list(links)  

# 1.5 Wrap all the previous functions into a single function  
def analyze_wikipedia_page(url):  
    html_content = get_html_content(url)  
    title = extract_article_title(html_content)  
    paragraphs_with_headings = extract_paragraphs_with_headings(html_content)  
    internal_links = collect_internal_wikipedia_links(html_content)  

    return {  
        'title': title,  
        'paragraphs_with_headings': paragraphs_with_headings,  
        'internal_links': internal_links  
    }  

# 1.6 Test the last function on a Wikipedia page of your choice  
if __name__ == "__main__":  
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"  # Change to any wiki page  
    results = analyze_wikipedia_page(url)  
    
    print(f"Title: {results['title']}\n")  
    print("Paragraphs with Headings:")  
    for heading, paragraphs in results['paragraphs_with_headings'].items():  
        print(f"{heading}:")  
        for para in paragraphs:  
            print(f" - {para}")  
    print("\nInternal Links:")  
    for link in results['internal_links']:  
        print(link)