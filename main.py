import time
import API_OpenIA #api_chatgpt()
import VoiceCommands
import TextToVoice

TextToVoice.text_to_speech("Oi, eu sou Atena!",'pt-br')

while True:
    ask = "Como posso ajudar?"
    print("ChatGPT: ",ask)
    TextToVoice.text_to_speech(ask)
    # Aguarda a entrada de voz do usuário
    input_text = VoiceCommands.recognize_speech()
    #input_text = "Qual é a árvore mais alta do mundo?"
    if input_text:
        # Envia a entrada para a API do ChatGPT
        #response_text = get_chatgpt_response(input_text)
        response_text = API_OpenIA.api_chatgpt(input_text)
        print("ChatGPT: ", response_text)
        # Chama função para converter o texto em áudio e reproduz o áudio
        TextToVoice.text_to_speech(response_text)
    time.sleep(5)

