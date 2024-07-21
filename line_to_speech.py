from pathlib import Path
import random
from merge_asky import only_alphabets
from openai import OpenAI
import os

client = OpenAI()


def make_file_name_from_text(text):
   words = text.split()
   unique_suffix = random.choice('bcdfghjklmnprstvwxyz') + random.choice('aeiou')
   return f'{only_alphabets(words[0])}_{only_alphabets(words[-1])}_{unique_suffix}.mp3'


def text_to_speech(line_to_convert, speech_dir_path):
  speech_file_name = make_file_name_from_text(line_to_convert)
  file_path = os.path.join(speech_dir_path, speech_file_name)
  with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd",
    voice="onyx",
    input=line_to_convert
  ) as response:
      response.stream_to_file(file_path)
      print(f'wrote to {file_path}')
      return speech_file_name
