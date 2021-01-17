# Exports AWS actions to HTML file & includes associated condition keys
# 
#   - Script won't export all possible actions per service, as it's dependant on what's posted to the associated AWS docs pages. 
#   - Output may include misc stuff - additional filtering may be required.

import requests, time, csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = requests.get(
    'https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html')
soup = BeautifulSoup(response.text, 'html.parser')
service = soup.find('div', class_='highlights')

f = open("aws-actions.html","w")
f.write('<html><head>')
f.write('<style> table {border: 0px solid #999; padding: 0px; width:100%; table-layout:fixed; font-family: Arial;} \
        td,th {border: 0px solid #999;font-size: 12px; column-width:18%; \
        padding: 0.5rem; text-align:left;vertical-align: top;} \
        .header{background-color:#C0C0C0; }</style>')
f.write('<table class="header"><tr><th>Service</th><th>Actions</th><th>Description</th><th>Access Type</th> \
        <th>Resource Types (*required)</th><th>Condition Keys</th><th>Dependent Actions</th></tr></table>')

for anchor in service.find_all('a'):
    time.sleep(1)
    table = []
    link = anchor.get('href').replace('./', '')
    response = requests.get('https://docs.aws.amazon.com/IAM/latest/UserGuide/' + link)
    soup = BeautifulSoup(response.text, 'html.parser')
    table_service = soup.find('div', class_='table-contents') 
    service_name = soup.find('code') 
    aws_service = [service_name.get_text('code')]   
    thead = table_service.thead
    thead.decompose()     
    tdsoup = soup.new_tag('td', str(aws_service))
    for tr in soup.find_all('tr'):
        tr.insert(1, soup.new_tag('td'))
        tr.td.append(aws_service[0])
    f.write(str(table_service)) 
f.write("</body></html>")
f.close()
