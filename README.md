# **Broken Link Checker in Python**

A simple Python script to check for broken links in a webpage.

## **Table of Contents**

* [Description](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#description)  
* [Prerequisites](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#prerequisites)  
* [Installation](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#installation)  
* [Usage](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#usage)  
* [Example](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#example)  
* [Features](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#features)  
* [Note on Rate Limiting](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#note-on-rate-limiting)  
* [Troubleshooting](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#troubleshooting)  
* [Future Enhancements](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#future-enhancements)  
* [Acknowledgments](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#acknowledgments)  
* [License](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#license)  
* [Contact](https://chat.deepseek.com/a/chat/s/1ed586b1-7aa1-4be6-a2b7-d5270a3c0ad8#contact)

## **Description**

This script is designed to find and report broken links (HTTP status codes 404, 500, etc.) on a given webpage. It uses the `requests` library to fetch URLs and `BeautifulSoup` from `bs4` to parse HTML content and extract links.

## **Prerequisites**

* Python 3.x  
* `requests` library  
* `beautifulsoup4` library  
* `urllib3` library

You can install the required libraries using:

bash

Copy  
pip install requests beautifulsoup4 urllib3

## **Installation**

1. Clone the repository:  
2. bash  
3. Copy  
4. git clone https://github.com/taleblou/BrokenLinkChecker\_Python.git  
5. Navigate to the project directory:  
6. bash  
7. Copy  
8. cd BrokenLinkChecker\_Python

## **Usage**

Run the script from the command line:

bash

Copy  
python broken\_link\_checker.py \[url\] \[output\_file (optional)\]

* **`[url]`**: The URL of the webpage to check.  
* **`[output_file (optional)]`**: The path to the CSV file where the results will be saved.

**Example:**

bash

Copy  
python broken\_link\_checker.py https://example.com results.csv

## **Example**

bash

Copy  
python broken\_link\_checker.py https://example.com  
**Output:**  
Copy

Checking links on https://example.com

Total links found: 50

Broken links found: 5

Broken Links:

1\. https://example.com/nonexistent-page (404)

2\. https://example.com/broken-link (404)

3\. https://example.com/error-page (500)

4\. https://example.com/another-broken-link (404)

5\. https://example.com/yet-another-broken-link (404)

## **Features**

* Checks for broken links on a given webpage.  
* Supports recursive checking (checks links on linked pages).  
* Saves results to a CSV file for further analysis.  
* Handles common HTTP errors and status codes.

## **Note on Rate Limiting**

Some websites may have rate limiting in place, which could cause the script to return errors or incomplete results. If you encounter such issues, consider adding a delay between requests or using a proxy.

## **Troubleshooting**

* **Missing Libraries**: Ensure all required libraries are installed.  
* **HTTP Errors**: Some links may return HTTP errors due to temporary issues on the server side.  
* **SSL Certificate Warnings**: Add `verify=False` in the `requests.get()` method if you encounter SSL certificate warnings.

## **Future Enhancements**

* Add support for GUI interface.  
* Implement multi-threading for faster link checking.  
* Support for checking links in PDFs or other document formats.  
* Option to check links in a specific section of the webpage.

## **Acknowledgments**

* The script uses the `requests` library for handling HTTP requests.  
* The `BeautifulSoup` library from `bs4` is used for parsing HTML content.

## **License**

This project is licensed under the MIT License \- see the [LICENSE](https://chat.deepseek.com/a/chat/s/LICENSE) file for details.

## **Contact**

For questions or feedback, please contact morteza\_taleblou@yahoo.com.

