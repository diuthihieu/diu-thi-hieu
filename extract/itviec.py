import tls_requests
from bs4 import BeautifulSoup as Soup
import csv

def extract(url: str) -> dict:
    response = tls_requests.get(url)
    print(response.text)

    soup = Soup(response.text, "html.parser")
    job_header_info = soup.find("div", class_="job-header-info")
    introduction = soup.find("div", class_="imb-6")
    skills= soup.find_all("div", class_="itag itag-light itag-sm")
    details= soup.find_all("div", class_="imy-5 paragraph")

    data = {}

    data["title"] = job_header_info.find("h1").text.strip()
    data["company"] = job_header_info.find("div", class_="employer-name").text.strip()
    data["location"]= introduction.find("span", class_="normal-text text-rich-grey").text.strip()
    data["form"]= introduction.find("span", class_="normal-text text-rich-grey ms-1").text.strip()
    for i, skill in enumerate(skills):
        data[f"skill: {i+1}"]= skill.text.strip()
    for i, detail in enumerate(details):
        data[f"detail: {i+1}"]= detail.find("p").text.strip()
    return data