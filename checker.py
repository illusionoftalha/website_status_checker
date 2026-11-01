import time

import requests
from bs4 import BeautifulSoup


def check_website_status_and_parse(url, session=None):
    client = session if session is not None else requests
    try:
        with client.get(url, timeout=(5, 15)) as response:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return "Up", soup
            return f"Down (Status Code: {response.status_code})", None
    except requests.exceptions.RequestException:
        return "Down (Unable to Connect)", None


def main():
    website_url = input("Enter the website URL to check: ")
    try:
        with requests.Session() as session:
            while True:
                status, html_content = check_website_status_and_parse(website_url, session)
                print(f"Website {website_url} is {status}.")
                if html_content is not None:
                    title = html_content.find('title')
                    if title:
                        print(f"Title: {title.text}")
                time.sleep(120)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
