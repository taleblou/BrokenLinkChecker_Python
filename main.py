import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tldextract import extract
from queue import Queue
from tqdm import tqdm
import pandas as pd

# Set to store visited URLs
visited_urls = set()
# List to store pages with CSS errors
error_pages = []
# Maximum number of pages to crawl
max_pages = 10000

# Starting URL (replace with the target website)
start_url = 'https://taleblou.ir/'
parsed_start = extract(start_url)
domain_start = parsed_start.domain
suffix_start = parsed_start.suffix

def is_same_domain(url, domain_start, suffix_start):
    parsed = extract(url)
    return parsed.domain == domain_start and parsed.suffix == suffix_start

def is_valid(url):
    parsed = urlparse(url)
    if not bool(parsed.netloc) or not bool(parsed.scheme):
        return False
    return is_same_domain(url, domain_start, suffix_start)

def crawl():
    queue = Queue()
    queue.put(start_url)
    progress = tqdm(total=max_pages, desc='Crawling Progress', unit='page')

    while not queue.empty() and len(visited_urls) < max_pages:
        url = queue.get()
        if url in visited_urls:
            continue
        visited_urls.add(url)
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            continue
        except Exception as err:
            print(f'An error occurred: {err}')
            continue
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all CSS files linked in the page
        css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet')]
        css_links = [urljoin(url, link) for link in css_links if is_valid(link)]
        # Check each CSS file for errors
        css_error = False
        for css_url in css_links:
            try:
                css_response = requests.get(css_url)
                css_response.raise_for_status()
            except requests.exceptions.HTTPError as http_err:
                print(f'CSS error on {url}: {http_err}')
                error_pages.append(url)
                css_error = True
                break
            except Exception as err:
                print(f'CSS error on {url}: {err}')
                error_pages.append(url)
                css_error = True
                break
        # Find all links in the page and add to queue
        links = [link.get('href') for link in soup.find_all('a')]
        links = [urljoin(url, link) for link in links if is_valid(link)]
        for link in links:
            if link not in visited_urls:
                queue.put(link)
        progress.update(1)
    progress.close()

# Start crawling
crawl()

# Save the list of error pages to a CSV file using pandas
if error_pages:
    df = pd.DataFrame(error_pages, columns=['Error_Page_URL'])
    df.to_csv('error_pages.csv', index=False)
else:
    print("No error pages to save.")

# Let's toast pandas! 🥂
print("Let's toast pandas! 🥂")