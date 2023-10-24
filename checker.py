import requests
from bs4 import BeautifulSoup
import time

def check_website_status_and_parse(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return "Up", soup
        else:
            return f"Down (Status Code: {response.status_code})", None
    except requests.exceptions.RequestException:
        return "Down (Unable to Connect)", None
website_url = input("Enter the website URL to check: ")
while True:
    status, html_content = check_website_status_and_parse(website_url)

    print(f"Website {website_url} is {status}.")

    if html_content:
        title = html_content.find('title')
        if title:
            print(f"Title: {title.text}")
    time.sleep(120) 
