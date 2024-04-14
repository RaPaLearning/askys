import re

patterns_to_remove = [
    r'^#.*\n',
    r'```shloka-sa\n(.*?)\n```',
    r'```shloka-sa-hk\n(.*?)\n```',
    r'`(.*?)`'
]

def md_to_english(md):
    english = md
    for pattern in patterns_to_remove:
        english = re.sub(pattern, '', english)
    english = re.sub(r'\u200b', ' ', english)
    english = re.sub(r'[\t\f\v ]{2,}', ' ', english) # 2 or more spaces become one
    return english.strip()


def md_paras_to_english_list(md):
    # md = re.sub(r'(?<!\n)\n(?!\n)', ' ', md) # stand-alone newline becomes space
    english = md_to_english(md)
    eng_no_space_bw_newlines = re.sub(r'\n\s*\n', '\n\n', english)
    english_list_with_newlines = re.split(r'\n\n', eng_no_space_bw_newlines)
    english_list_no_newlines = list(map(lambda e: re.sub(r'\n', ' ', e), english_list_with_newlines))
    print(english_list_no_newlines)
    return english_list_no_newlines
