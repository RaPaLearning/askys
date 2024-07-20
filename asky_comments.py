import requests
import sys
import os

app_script_urlbase = 'https://script.google.com/macros/s'
text_from_asky_appid = 'AKfycbxte9Euu8Mc3pXOjTWMaZYqJpfXcPPl2F-b_jAI8S8L1v4B35Zn9V_-XnlaV4Vf3x2O'
json_from_asky_appid = 'AKfycbykc9T9NyobDaaf5Xfdtj0AojmbyIM5amNVz-gh6md6CWONIMBkUgb267VZQlr_KZq_aQ'


def app_resp_to_file(appid, doc_id, file_name):
    with open(file_name) as f:
        app_url = f'{app_script_urlbase}/{appid}/exec'
        resp_as_text = requests.get(app_url, params={'id': doc_id})
        f.write(resp_as_text)
        print(f'wrote to {file_name}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        document_id = sys.argv[1]
        out_folder = 'output'
        app_resp_to_file(text_from_asky_appid, document_id, os.join(out_folder, 'asky_as_text.txt'))
        app_resp_to_file(json_from_asky_appid, document_id, os.join(out_folder, 'asky_comments.json'))
    else:
        print('Usage: python asky_comments.py document_id')
