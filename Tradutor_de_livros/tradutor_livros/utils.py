import os
import pytesseract
import fitz  # PyMuPDF
from pdf2image import convert_from_path
from deep_translator import GoogleTranslator

# Verifica se o PDF contém texto real
# Parâmetro: pdf_path (str) - Caminho do arquivo PDF.
# Retorno: True se o PDF contiver texto; False caso contrário.
def verificar_pdf_com_texto(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        texto = "".join(page.get_text() for page in doc)
        return len(texto) > 0
    except Exception:
        return False

# Extrai texto de um PDF com texto digital
# Parâmetro: pdf_path (str) - Caminho do arquivo PDF.
# Retorno: Texto extraído do PDF ou uma string vazia caso ocorra erro.
def extrair_texto_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        return "".join(page.get_text() for page in doc)
    except Exception:
        return ""

# Extrai texto de PDF escaneado usando OCR
# Parâmetro: pdf_path (str) - Caminho do arquivo PDF ou imagem.
# Retorno: Texto extraído da imagem via OCR ou uma string vazia caso ocorra erro.
def extrair_texto_ocr(pdf_path):
    try:
        imagens = convert_from_path(pdf_path, dpi=300)
        texto = ""
        for img in imagens:
            texto += pytesseract.image_to_string(img, lang='eng')
        return texto
    except Exception as e:
        print(f"[ERRO no OCR] {e}")
        return ""

# Divide texto em blocos para não exceder limite da API
# Parâmetro: texto (str) - Texto a ser dividido.
# Parâmetro: tamanho_maximo (int) - Tamanho máximo de cada bloco (padrão: 4000).
# Retorno: Lista de blocos de texto.
def dividir_texto_em_blocos(texto, tamanho_maximo=4000):
    blocos = []
    while len(texto) > tamanho_maximo:
        pos = texto.rfind(" ", 0, tamanho_maximo)
        pos = pos if pos != -1 else tamanho_maximo
        blocos.append(texto[:pos])
        texto = texto[pos:].strip()
    if texto:
        blocos.append(texto)
    return blocos

# Traduz texto em blocos usando GoogleTranslator
# Parâmetro: texto (str) - Texto a ser traduzido.
# Retorno: Texto traduzido.
def traduzir_texto(texto):
    try:
        blocos = dividir_texto_em_blocos(texto)
        traduzido = ""
        for bloco in blocos:
            traduzido += GoogleTranslator(source='auto', target='pt').translate(bloco) + "\n"
        return traduzido
    except Exception as e:
        print(f"[ERRO na tradução] {e}")
        return texto

# Salva texto em arquivo .txt
# Parâmetro: texto (str) - Texto a ser salvo.
# Parâmetro: output_path (str) - Caminho onde o arquivo será salvo.
# Retorno: Nenhum (salva o arquivo de texto no caminho especificado).
def salvar_txt(texto, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(texto)
    except Exception as e:
        print(f"[ERRO ao salvar TXT] {e}")

