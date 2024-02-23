import requests
from bs4 import BeautifulSoup
import re
import json

def extrair_campos_message(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        html_content = response.text
        
        soup = BeautifulSoup(html_content, 'html.parser')
        textos = soup.find_all(text=re.compile(r'(@Message|@LogMessage)'))
        campos_message = []
        for texto in textos:
            campos_message.append(texto.strip())
        
        return campos_message
    else:
        print("Falha do retorno do request:", response.status_code)
        return None

url = "https://www.keycloak.org/docs-api/23.0.6/javadocs/org/keycloak/services/ServicesLogger.html"

campos_message = extrair_campos_message(url)

if campos_message:
    data = {'campos_message': campos_message}
    
    with open('campos_message.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print("As informações foram salvas em 'campos_message.json' com sucesso.")
else:
    print("Não foi possível extrair os campos @Message e @LogMessage.")
