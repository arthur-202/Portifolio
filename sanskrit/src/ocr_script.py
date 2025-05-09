import os
import requests

def obtemOcr(imagem):
    """
    Envia uma imagem para o serviço de OCR do Sanskrit Dictionary e retorna o texto reconhecido.

    Parâmetros:
    imagem (str): Nome do arquivo da imagem a ser processada (deve estar no diretório ./images)

    Retorno:
    str | bool: Texto reconhecido com quebras de linha ajustadas, ou False se o resultado for muito curto,
                ou uma string de erro em caso de falha na requisição.
    """
    # URL da API
    url = "https://ocr.sanskritdictionary.com/recognise"

    # Cabeçalhos HTTP usados na requisição
    headers = {
        "Accept": "*/*",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Origin": "https://ocr.sanskritdictionary.com",
        "Referer": "https://ocr.sanskritdictionary.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    # Cookies necessários para autenticação da sessão
    cookies = {
        "_ga": "GA1.2.1894011499.1732196530",
        "_gid": "GA1.2.1613495533.1745958463",
        "_gat": "1",
        "_ga_9WBCP9RPDZ": "GS1.2.1745958463.23.1.1745959251.0.0.0"
    }

    # Envia a imagem para o serviço OCR
    with open(f'./images/{imagem}', 'rb') as img_file:
        files = {
            'lang': (None, 'san'),
            'service': (None, 'google'),
            'image': ('image.png', img_file, 'image/png')
        }
        try:
            response = requests.post(url, headers=headers, cookies=cookies, files=files)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return f"Erro na requisição: {e}"

    # Processa a resposta
    if response.status_code == 200:
        texto = response.json().get("text", "")
        if len(texto) > 50:
            return texto.replace("<br />", "\n")
        else:
            return False
    else:
        return f"Erro HTTP {response.status_code}"

def transformar_resposta(texto_resposta):
    """
    Formata o texto OCR para adicionar quebras de linha após os sinais de fim de frase '।' e '।।'.

    Parâmetros:
    texto_resposta (str): Texto retornado pelo OCR

    Retorno:
    str: Texto formatado com quebras de linha apropriadas
    """
    resultado = []
    i = 0
    while i < len(texto_resposta):
        if texto_resposta[i] == "।":
            # Verifica se é "।।"
            if i + 1 < len(texto_resposta) and texto_resposta[i + 1] == "।":
                resultado.append("।।\n")
                i += 2
            else:
                resultado.append("।\n")
                i += 1
                if i < len(texto_resposta) and texto_resposta[i] == " ":
                    i += 1  # pula espaço após "।"
        else:
            resultado.append(texto_resposta[i])
            i += 1
    return ''.join(resultado)

# Garante que o diretório "ocrs" exista
os.makedirs("./ocrs", exist_ok=True)

# Lê imagens do diretório e processa OCR
local = "./images"
for image in os.listdir(local):
    ocr = obtemOcr(image)
    with open(f"./ocrs/ocr_{image}.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(transformar_resposta(ocr))
    print(f"Foi para {image}")

