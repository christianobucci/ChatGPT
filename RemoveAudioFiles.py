import os

def remove_audio():
    if os.path.exists("C:\\Python310\\ChatGPT-Audio\\answer.mp3"):
        os.remove(("C:\\Python310\\ChatGPT-Audio\\answer.mp3"))
    if os.path.exists("C:\\Python310\\ChatGPT-Audio\\ask.mp3"):
        os.remove(("C:\\Python310\\ChatGPT-Audio\\ask.mp3"))