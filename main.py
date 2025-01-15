import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tldextract import extract
from queue import Queue
from tqdm import tqdm
import pandas as pd
import time

visited_urls = set()
error_pages = []
max_pages = 10000

start_url = 'https://www.example.com'  # Replace with the target website
parsed_start = extract(start_url)
domain_start = parsed_start.domain
suffix_start = parsed_start.suffix

visited_urls = set()
error_pages = []
max_pages = 10000

start_url = 'https://www.example.com'  # Replace with the target website
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

def check_resource(url):
    try:
        response = requests.head(url, allow_redirects=True)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        return response.status_code
    except Exception as err:
        print(f'Resource error on {url}: {err}')
        return None
    return None


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
        # Collect all resource links
        resource_links = []
        # Check CSS links
        css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet')]
        resource_links.extend(css_links)
        # Check JavaScript links
        js_links = [script['src'] for script in soup.find_all('script', src=True)]
        resource_links.extend(js_links)
        # Check image links
        img_links = [img['src'] for img in soup.find_all('img', src=True)]
        resource_links.extend(img_links)
        # Check video links
        video_tags = soup.find_all('video')
        video_links = []
        for video in video_tags:
            src = video.get('src')
            if src:
                video_links.append(src)
            sources = video.find_all('source')
            for source in sources:
                src = source.get('src')
                if src:
                    video_links.append(src)
        resource_links.extend(video_links)
        # Check iframe links
        iframe_links = [iframe['src'] for iframe in soup.find_all('iframe', src=True)]
        resource_links.extend(iframe_links)
        # Check each resource
        for link in resource_links:
            full_url = urljoin(url, link)
            if is_valid(full_url):
                error_code = check_resource(full_url)
                if error_code and 400 <= error_code < 600:
                    error_pages.append({
                        'Page_URL': url,
                        'Resource_URL': full_url,
                        'Error_Code': error_code
                    })
        # Find all links in the page and add to queue
        links = [link.get('href') for link in soup.find_all('a')]
        links = [urljoin(url, link) for link in links if is_valid(link)]
        for link in links:
            if link not in visited_urls:
                queue.put(link)
        # Optional: Add a delay to avoid overwhelming the server
        # time.sleep(1)
        progress.update(1)
    progress.close()

# Start crawling
crawl()

# Save the error information to a CSV file using pandas
if error_pages:
    df = pd.DataFrame(error_pages)
    df.to_csv('error_details.csv', index=False)
else:
    print("No error pages to save.")

# Let's toast pandas! 🥂
print("Let's toast pandas! 🥂")
