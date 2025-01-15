# **Web Crawler Script**

## **Overview**

This script is a Python-based web crawler designed to traverse a website and identify broken resource links such as CSS, JavaScript, images, videos, and iframes. It also checks if the pages belong to the same domain as the starting URL and saves a detailed report of error pages in a CSV file.

---

## **Features**

* **Domain Filtering:** Ensures the crawler stays within the target domain.  
* **Resource Checking:** Verifies the availability of various resource links (e.g., CSS, JS, images, videos, iframes).  
* **Error Reporting:** Logs details of broken resources (HTTP status codes 400–599).  
* **Concurrent Crawling:** Uses a queue to manage page visits.  
* **Progress Tracking:** Displays a progress bar using `tqdm`.  
* **CSV Export:** Saves error details in a CSV file for easy review.

---

## **Requirements**

To run this script, you need the following Python libraries installed:

* `requests`: For making HTTP requests.  
* `BeautifulSoup` (from `bs4`): For parsing HTML content.  
* `tldextract`: For extracting domain and suffix information.  
* `tqdm`: For displaying a progress bar.  
* `pandas`: For saving error reports to a CSV file.

You can install the required packages with:

bash

Copy code

`pip install requests beautifulsoup4 tldextract tqdm pandas`

---

## **How to Use**

**Set the Starting URL:** Replace `https://www.example.com` with the URL of the website you want to crawl:  
python  
Copy code  
`start_url = 'https://www.example.com'`

1. 

**Configure Maximum Pages:** Update the `max_pages` variable to limit the number of pages to crawl (default is 10,000):  
python  
Copy code  
`max_pages = 10000`

2. 

**Run the Script:** Execute the script in your Python environment:  
bash  
Copy code  
`python main.py`

3.   
4. **View Results:**  
   * If broken resource links are found, they will be saved to a file named `error_details.csv` in the script's directory.  
   * If no errors are detected, a message will indicate no error pages were saved.

---

## **Output**

The output CSV file (`error_details.csv`) contains the following columns:

* **Page\_URL:** The page where the broken resource was found.  
* **Resource\_URL:** The URL of the broken resource.  
* **Error\_Code:** The HTTP status code indicating the error.

---

## **Notes**

* **Politeness:** Consider adding a delay (`time.sleep(1)`) between requests to avoid overloading the target server.  
* **Error Handling:** The script handles HTTP errors gracefully but logs other exceptions to the console.  
* **Scalability:** This script is single-threaded and may need optimization for crawling large websites.

---

## **Example Output**

Sample `error_details.csv`:

| Page\_URL | Resource\_URL | Error\_Code |
| ----- | ----- | ----- |
| [https://example.com](https://example.com) | https://example.com/style.css | 404 |
| [https://example.com](https://example.com) | https://example.com/script.js | 403 |

---

## **License**

This script is open-source and available for personal and educational use. Feel free to modify it to suit your needs.

