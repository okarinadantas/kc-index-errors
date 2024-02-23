import json
import re

resultados = []

with open('campos_message.json', 'r') as json_file:
    data = json.load(json_file)

if 'campos_message' in data:
    for campo in data['campos_message']:
        id_match = re.search(r'id=(\d+)', campo)
        if id_match:
            id_numero = id_match.group(1)
            id_formatado = id_numero.zfill(4)
            value_match = re.search(r'value=(.+)', campo)
            if value_match:
                value = value_match.group(1)
                resultado = f"KC-SERVICES{id_formatado} {value}"
                resultados.append(resultado)
            else:
                resultados.append(f"KC-SERVICES{id_formatado} (sem valor)")
else:
    print("Não foram encontrados campos @Message e @LogMessage no arquivo JSON.")

with open('resultados.json', 'w') as json_output:
    json.dump(resultados, json_output, indent=4)

print("Os resultados foram exportados para 'resultados.json'.")
