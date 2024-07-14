import requests
import re

document_id = '11No58DpoVARwL-6qsq9jaPcl1ph29hTO7g_EeDw6rB8'
app_script_urlbase = 'https://script.google.com/macros/s'
asky_to_json_appid = 'AKfycbykc9T9NyobDaaf5Xfdtj0AojmbyIM5amNVz-gh6md6CWONIMBkUgb267VZQlr_KZq_aQ'
asky_to_text_appid = 'AKfycbxte9Euu8Mc3pXOjTWMaZYqJpfXcPPl2F-b_jAI8S8L1v4B35Zn9V_-XnlaV4Vf3x2O'

comment_fetcher = f'{app_script_urlbase}/{asky_to_json_appid}/exec'
comments = requests.get(comment_fetcher, params={'id': document_id})
print(comments.json())
print('---')
asky_as_text_fetcher = f'{app_script_urlbase}/{asky_to_text_appid}/exec'
asky_as_text = requests.get(asky_as_text_fetcher, params={'id': document_id})
print(asky_as_text.text)
print('---')
paragraphs = asky_as_text.text.split('\n')
searchable_paras = list(map(lambda x: re.sub('[^a-z]', '', x.lower()), paragraphs))
print(f'--searchables:\n{searchable_paras}')
index = 0
for comment_entry in comments.json():
    quoted_para = comment_entry['paragraph']
    para_to_search = re.sub('[^a-z]', '', quoted_para.lower())
    print(f'--para_to_search:\n{para_to_search}')
    if (para_to_search in searchable_paras):
        print(f'para of comment #{index} found')
    else:
        print(f'not found: para of comment #{index}')
    index += 1
