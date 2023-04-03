# Função para reconhecimento de fala

import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # filename = r'C:\Python310\ChatGPT-Audio\ask.mp3' #local onde o arquivo de áudio será gravado
        # tts = gTTS(text=ask, lang='pt-br')
        # tts.save(filename)
        # playsound(filename)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pt-BR')
        print(f"Você: {text}")
        return text
    except:
        print("ChatGPT: Não entendi o que você disse.")
        return ""