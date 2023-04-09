import os
from dotenv import load_dotenv
import openai

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave de API da OpenAI a partir das variáveis de ambiente
api_key = os.getenv("OPENAI_API_KEY")

# Configura a API Key da OpenAI
openai.api_key = api_key

def openai_request(api_model, api_prompt, api_temperature, api_max_tokens, api_top_p, api_frequency_penalty, api_presence_penalty):
  response = openai.Completion.create(
    model=api_model,
    prompt=api_prompt,
    temperature=api_temperature,
    max_tokens=api_max_tokens,
    top_p=api_top_p,
    frequency_penalty=api_frequency_penalty,
    presence_penalty=api_presence_penalty,
    #stop=["\n"]
  )
  return response

#print(openai_request(model, prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty)['choices'][0]['text'])