# Função para sintetizar voz a partir de um texto

from gtts import gTTS
from playsound import playsound

def text_to_speech(text, lng):
    # Local para gravar o áudio
    filename = r'C:\Python310\ChatGPT-Audio\answer.mp3'

    # Lingua usada para reconhecimento da fala
    # if lng = 1:
    #     lng = 'pt-br'
    # elif
    #     lng = 'en'

    tts = gTTS(text=text, lang=lng)
    tts.save(filename)
    playsound(filename)
