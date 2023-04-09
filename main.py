import API_OpenAI
import SpeechRecognition
import TextToVoice
import time
import RemoveAudioFiles

# Função para remover arquivos de aúdios de respostas e perguntas anteriores armazenadas em arquivos de áudio
#RemoveAudioFiles.remove_audio()

spoken_language = 'pt-br'

TextToVoice.text_to_speech("Oi, eu sou Atena!", spoken_language)
#time.sleep(3)

#Parâmetros da requisição

model="text-davinci-003"
prompt="Qual o carro mais rápido do mundo?"
temperature=0
max_tokens=500
top_p=1
frequency_penalty=0.0
presence_penalty=0.0
#api_stop=["\n"]

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
        #response_text = API_OpenAI.api_chatgpt(input_text)[0]
        response_text = API_OpenAI.openai_request(model,input_text,temperature,max_tokens, top_p, frequency_penalty, presence_penalty)
        response_text = response_text['choices'][0]['text']
        response_text = response_text.lstrip()
        response_text = response_text.rstrip()
        print("ChatGPT: ", response_text)

        # Função para remover arquivos de aúdios de respostas e perguntas anteriores armazenadas em arquivos de áudio
        RemoveAudioFiles.remove_audio()

        # Chama função para converter o texto em áudio e reproduz o áudio
        TextToVoice.text_to_speech(response_text, spoken_language)
    time.sleep(5)
