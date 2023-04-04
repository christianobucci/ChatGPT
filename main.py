import API_OpenIA #api_chatgpt()
import SpeechRecognition
import TextToVoice
import time

spoken_language = 'pt-br'

TextToVoice.text_to_speech("Oi, eu sou Atena!", spoken_language)

while True:
    ask = "Como posso ajudar?"
    print("ChatGPT: ", ask)
    TextToVoice.text_to_speech(ask, spoken_language) #ask = Your Question, spoken_language = idiom
    # Aguarda a entrada de voz do usuário
    input_text = SpeechRecognition.recognize_speech()
    #input_text = "Qual é a árvore mais alta do mundo?"
    if input_text:
        # Envia a entrada para a API do ChatGPT
        #response_text = get_chatgpt_response(input_text)
        response_text = API_OpenIA.api_chatgpt(input_text)[0]
        print("ChatGPT: ", response_text)
        # Chama função para converter o texto em áudio e reproduz o áudio
        TextToVoice.text_to_speech(response_text, spoken_language)
    time.sleep(5)

