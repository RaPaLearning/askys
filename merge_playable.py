import json
import os
import sys
import make_playable as playable
import line_to_speech as speech

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as para_comments_file:
            para_comments = json.load(para_comments_file)
            playable_path = os.path.join(playable.playables_dir, playable.make_playable_dir_name(para_comments))
            for one_line in para_comments:
                speech_file_name = speech.make_file_name_from_text(one_line['line'])
                one_line['speech'] = speech_file_name

            with open(os.path.join(playable_path, 'playable.json'), 'w') as playable_file:
                json.dump(para_comments, playable_file)
            print('wrote to playable.json')
    else:
        print('Usage: python merge_playable.py para_comments_file_name')
