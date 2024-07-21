from pathlib import Path
from time import sleep
from merge_asky import only_alphabets
from openai import OpenAI, RateLimitError
import os

client = OpenAI()
counter_for_unique = 0

def make_file_name_from_text(text):
   global counter_for_unique
   words = text.split()
   counter_for_unique += 1
   unique_prefix = '{:02d}'.format(counter_for_unique)
   return f'{unique_prefix}_{only_alphabets(words[0])}_{only_alphabets(words[-1])}.mp3'


def text_to_speech(line_to_convert, speech_dir_path):
  speech_file_name = make_file_name_from_text(line_to_convert)
  file_path = os.path.join(speech_dir_path, speech_file_name)
  for i in range(3):
    try:
      with client.audio.speech.with_streaming_response.create(
        model="tts-1-hd",
        voice="onyx",
        input=line_to_convert
      ) as response:
          response.stream_to_file(file_path)
          print(f'wrote to {file_path}')
          return speech_file_name
    except RateLimitError:
      print('rate limit hit! waiting 30s...')
      sleep(30)
