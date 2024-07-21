import json
import sys
import os
import shutil
from line_to_speech import text_to_speech

playables_dir = 'playables'


def make_playable_dir_name(para_comments):
    return para_comments[0]['line'].lower().replace(' ', '_')

def make_empty_playable_dir(para_comments):
    playable_dir_path = os.path.join(playables_dir, make_playable_dir_name(para_comments))
    if os.path.exists(playable_dir_path):
        shutil.rmtree(playable_dir_path)
    os.makedirs(playable_dir_path)
    return playable_dir_path


def para_comment_tts(one_line, playable_dir_path):
    speech_file_name = text_to_speech(one_line['line'], playable_dir_path)
    one_line['speech'] = speech_file_name

def make_askys_with_speech(playable_dir_path, lines_with_comment):
    for one_line in lines_with_comment:
        para_comment_tts(one_line, playable_dir_path)
    return lines_with_comment


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as para_comments_file:
            para_comments = json.load(para_comments_file)
            playable_path = make_empty_playable_dir(para_comments)
            playable_lines = make_askys_with_speech(playable_path, para_comments)
            with open(os.path.join(playable_path, 'playable.json'), 'w') as playable_file:
                json.dump(playable_lines, playable_file)
            print('wrote to playable.json')
    else:
        print('Usage: python make_playable.py para_comments_file_name')
