import json
import pandas as pd
import requests
from tqdm import tqdm
import time
import sqlalchemy

# Retorna uma lista de todos os pacotes do brew
packages_json = requests.get('https://formulae.brew.sh/api/formula.json').json()

results = []
t1 = time.perf_counter()

for package in tqdm(packages_json, desc='Running'):
    
    package_name = package['name']
    package_desc = package['desc']

    packages_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

    r = requests.get(packages_url)
    package_json = r.json()

    install_30 = sum([v for k,v in package_json['analytics']['install_on_request']['30d'].items() if package_name in k ])
    install_90 = sum([v for k,v in package_json['analytics']['install_on_request']['90d'].items() if package_name in k ])
    install_365 = sum([v for k,v in package_json['analytics']['install_on_request']['365d'].items() if package_name in k ])

    data = {
        'name': package_name,
        'desc': package_desc,
        'analytics': {
            '30d': install_30,
            '90d': install_90,
            '365d': install_365,
        }
    }

    results.append(data)
    # time.sleep(r.elapsed.total_seconds())
  
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')

with open('package_info.json', 'w') as f:
    json.dump(results, f, indent=2)