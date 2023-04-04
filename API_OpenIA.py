def api_chatgpt(prompt: str) -> str:
    """
    :rtype: basestring
    """
    import requests
    import json
    import API_Key

    # Parâmetros da request para a API do ChatGPT

    url = 'https://api.openai.com/v1/chat/completions'
    apikey = API_Key.api_key()

    #Header

    headers = {
        # 'Connection':'keepalive',
        'Content-Type': 'application/json',
        'Authorization': apikey
    }

    #Payload

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    # print('Prompt: ',prompt)
    # data = {
    #        'prompt': prompt,
    #        'max_tokens': 50,
    #        'temperature': 0.7,
    #        'n': 1,
    #        'stop': '\n'
    #    }

    response_json = requests.post(url, headers=headers, data=json.dumps(data))
    response_dict = json.loads(response_json.content)

    if response_json.ok:
        if 'choices' in response_dict:
            if 'message' in response_dict['choices'][0]:
                # Retorna o texto da primeira escolha de resposta
                return response_dict['choices'][0]['message']['content'], response_dict['id']
                print(response_dict['choices'][0]['message']['content'], response_dict['id'])
            else:
                print('Faltando atributo [''choices''][0][''message''] dentro do response_dict[''choices''][0]')
        else:
            # Retorna uma mensagem de erro se a resposta não contém a chave 'choices'
            return "A resposta da API não contém as informações esperadas."
    else:
        # Retorna uma mensagem de erro se a request não foi bem-sucedida
        #return "Ocorreu um erro na request para a API."
        print("Ocorreu um erro na request para a API.")

#api_chatgpt('Qual o maior planeta universo?')
