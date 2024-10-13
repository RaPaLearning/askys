import json
import sys
import os

para_comments_path = os.path.join('output', 'merged_para_comments.json')
playable_path = os.path.join('playables', 'bring_the_best_in_you')
playables_json_path = os.path.join(playable_path, 'playable.json')

if __name__ == '__main__':
  if len(sys.argv) == 2:
    para_comments_path = sys.argv[1]
    playables_json_path = sys.argv[2]
  else:
    print(f'updating {playables_json_path}')

  with open(para_comments_path, 'r') as para_comments_file, open(playables_json_path, 'r') as playables_file:
    para_comments = json.load(para_comments_file)
    playables = json.load(playables_file)
    play_count = len(playables)
    for i in range(play_count):
      if playables[i]['line'] == para_comments[i]['line']:
        if 'show' in para_comments[i]:
          playables[i]['show'] = para_comments[i]['show']
      else:
        print(f"mismatch:\n{playables[i]['line']}\nvs\n{para_comments[i]['line']}")
        exit(1)
    with open(playables_json_path, 'w') as playable_file:
      json.dump(playables, playable_file)
      print(f'wrote to {playables_json_path}')

