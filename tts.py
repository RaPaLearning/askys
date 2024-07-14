from pathlib import Path
from openai import OpenAI
client = OpenAI()


def text_to_speech(text_to_convert):
  speech_file_path = Path(__file__).parent / "q_for_ramanuja.mp3"
  with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd",
    voice="onyx",
    input=text_to_convert
  ) as response:
      response.stream_to_file(speech_file_path)
      print(f'wrote to {speech_file_path}')
