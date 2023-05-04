import requests
from glob import glob


_url = 'http://127.0.0.1:8000/MergeFilesIntoOne/'
# pay_load = {'folder_path': glob('C:\\File**\\sr**\\Input**'), 
#             'extension_type': 'PDF'}
pay_load = {'folder_path': glob('C:\\File**\\sr**\\Input**')[0], 
            'extension_type': 'PDF'}

response = requests.post(url=_url, 
                         json=pay_load)
# print(response.json())
# print(response)
# print(response.text)
