# Função para reconhecimento de fala /

import speech_recognition as sr
import TextToVoice

spoken_language = 'pt-br'

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')
        print(f"Você: {text}")
        return text
    except:
        print("ChatGPT: Desculpe, não entendi!")
        TextToVoice.text_to_speech("Desculpe, não entendi!", spoken_language)  # ask = Your Question, spoken_language = idiom
        return ""