from fake_useragent import UserAgent
 
ua = UserAgent()
headers = {'user-agent': ua.random} 

import requests
import csv
import time
from tqdm import tqdm

api_url = "https://airtravelinfo.kr/wiki/api.php"

with open('rawdata/항공위키/airwiki_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["페이지 번호", "문서 제목", "문서 내용"])

    apcontinue = ''
    for _ in tqdm(range(14)):
        
        params = {
            "action": "query",
            "format": "json",
            "list": "allpages",
            "aplimit": "max",
            "apcontinue": apcontinue
        }
        
        time.sleep(0.1)
        response = requests.get(api_url, params=params, headers=headers)
        data = response.json()
        
        if 'query' in data:
            pages = data['query']['allpages']

            for page in pages:
                page_id = page['pageid']
                page_title = page['title']

                page_params = {
                    "action": "query",
                    "format": "json",
                    "prop": "revisions",
                    "rvprop": "content",
                    "pageids": page_id
                }

                time.sleep(0.1)
                page_response = requests.get(api_url, params=page_params, headers=headers)
                page_data = page_response.json()

                page_content = page_data['query']['pages'][str(page_id)]['revisions'][0]['*']
                if page_content[0:5] != "#넘겨주기" and page_content[0:9] != "#redirect":
                    writer.writerow([page_id, page_title, page_content])
                    
        if 'continue' in data:
            apcontinue = data['continue']['apcontinue']
        else:
            break