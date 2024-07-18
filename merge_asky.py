import json
import re

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
    return map(lambda line: {'line': line, **find_linkage(line, comment_json)}, nonblank_lines)
