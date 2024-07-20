import json
import re
import sys
import os

def only_alphabets(s):
    return re.sub('[^a-z]', '', s.lower())


def content_matches(line1, line2):
    return only_alphabets(line1) == only_alphabets(line2)


def comment_to_dict(comment):
    comment_as_jsonstr = comment.replace('link: ', '{"link": "').replace(',show:', '","show": "') + '"}'
    comment_with_show_as_string = json.loads(comment_as_jsonstr)
    comment_as_dict = {'link': comment_with_show_as_string['link'], 'show': comment_with_show_as_string['show'].split()}
    return comment_as_dict


def find_linkage(line, comment_json):
    matched_comments = [comment_entry for comment_entry in comment_json if content_matches(comment_entry['paragraph'], line)]
    if len(matched_comments) == 1:
        source = comment_to_dict(matched_comments[0]['comment'])
        return source
    else:
        return {}


def merge_paras_with_comments(text, comment_json_str):
    comment_json = json.loads(comment_json_str.replace('\nshow', ',show'))
    nonblank_lines = [line for line in text.split('\n') if len(line.strip()) > 0]
    merged_para_comments = list(map(lambda line: {'line': line, **find_linkage(line, comment_json)}, nonblank_lines))
    merged_comment_count = len([e for e in merged_para_comments if 'link' in e])
    if merged_comment_count != len(comment_json):
        raise ValueError(f'some comments not matched')
    return merged_para_comments

if __name__ == '__main__':
    if len(sys.argv) == 3:
        text_file_name = sys.argv[1]
        comments_json_file_name = sys.argv[2]
        output_json_file_name = os.join('output', 'merged_para_comments.json')
        with open (text_file_name, 'r') as text_file, open(comments_json_file_name, 'r') as comments_json_file,\
          open(output_json_file_name, 'w') as merged_json_file:
            json.dump(
                merge_paras_with_comments(text_file.read(), comments_json_file.read()),
                merged_json_file
            )
        print(f'merged to {output_json_file_name}')
    else:
        print('Usage: python merge_asky.py text_file_name comment_json_file_name')
