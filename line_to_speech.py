from pathlib import Path
from time import sleep
from merge_asky import only_alphabets
from openai import OpenAI, RateLimitError
import os
import sys

client = OpenAI()
counter_for_unique = 0

def make_file_name_from_text(text):
   global counter_for_unique
   words = text.split()
   counter_for_unique += 1
   unique_prefix = '{:02d}'.format(counter_for_unique)
   return f'{unique_prefix}_{only_alphabets(words[0])}_{only_alphabets(words[-1])}.m4a'


def text_to_speech(line_to_convert, speech_dir_path, response_format='aac'):
  speech_file_name = make_file_name_from_text(line_to_convert)
  file_path = os.path.join(speech_dir_path, speech_file_name)
  for i in range(3):
    try:
      with client.audio.speech.with_streaming_response.create(
        model="tts-1-hd",
        voice="onyx",
        input=line_to_convert,
        response_format=response_format
      ) as response:
          response.stream_to_file(file_path)
          print(f'wrote {response_format} to {file_path}')
          return speech_file_name
    except RateLimitError:
      print('rate limit hit! waiting 30s...')
      sleep(30)


if __name__ == '__main__':
  if len(sys.argv) != 4:
    print('Usage: python line_to_speech.py "the words" . aac')
  else:
    text_to_speech(sys.argv[1], sys.argv[2], sys.argv[3])
