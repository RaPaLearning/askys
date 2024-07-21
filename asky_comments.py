import json
import requests
import sys
import os

app_script_urlbase = 'https://script.google.com/macros/s'
text_appid = 'AKfycbxte9Euu8Mc3pXOjTWMaZYqJpfXcPPl2F-b_jAI8S8L1v4B35Zn9V_-XnlaV4Vf3x2O'
comments_json_appid = 'AKfycbykc9T9NyobDaaf5Xfdtj0AojmbyIM5amNVz-gh6md6CWONIMBkUgb267VZQlr_KZq_aQ'


def write(s, file_name):
    out_folder = 'output'
    file_path = os.path.join(out_folder, file_name)
    with open(file_path, 'w') as f:
        f.write(s)
        print(f'wrote to {file_path}')

def get(appid, doc_id):
    app_url = f'{app_script_urlbase}/{appid}/exec'
    return requests.get(app_url, params={'id': doc_id})


if __name__ == '__main__':
    if len(sys.argv) == 2:
        document_id = sys.argv[1]
        write(get(text_appid, document_id).text, 'asky_as_text.txt')
        comments_json_str = json.dumps(get(comments_json_appid, document_id).json(), indent=2)
        write(comments_json_str, 'asky_comments.json')
    else:
        print('Usage: python asky_comments.py document_id')
