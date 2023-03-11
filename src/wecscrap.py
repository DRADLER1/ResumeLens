import requests
from bs4 import BeautifulSoup
field = input("Enter the name of the field to search: ")

url = f"https://www.indeed.com/resumes?q={field}&l="

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

resume_links = soup.find_all("a", class_="app_link")

for i in range(5):
    print(f"Resume {i+1}: {resume_links[i].get('href')} - {resume_links[i].text.strip()}")