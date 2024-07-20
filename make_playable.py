import sys

def make_playable_dir_name(para_comments):
    return 'the text of the first para, _ instead of spaces'

def para_comment_tts(one_para_comment, playable_dir_name):
    return 'create audio in playable_dir_name and link it to one_para_comment'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print('read para_comments json and generate playable')
    else:
        print('Usage: python make_playable.py para_comments_file_name')
