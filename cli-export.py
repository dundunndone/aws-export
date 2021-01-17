# cli-export

import requests, time, csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = requests.get('https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html')
soup = BeautifulSoup(response.text, 'html.parser')
service = soup.find('div', class_='toctree-wrapper compound')

with open("cli-export.csv", "wt+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Service", "Actions"])
    for anchor in service.find_all('a'):
        link = anchor.get('href') 
        response = requests.get('https://awscli.amazonaws.com/v2/documentation/api/latest/reference/' + link)
        soup2 = BeautifulSoup(response.text, 'html.parser')
        service_link = link.replace('/index.html', '') # strips link and outputs service names    
        service_list = soup2.find_all("a", class_='reference internal')[4:]
        for name in service_list:
            serv_name = name.get_text()
            writer.writerow([service_link, serv_name])
