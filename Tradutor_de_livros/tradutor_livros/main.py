import os
from utils import (
    verificar_pdf_com_texto,
    extrair_texto_pdf,
    extrair_texto_ocr,
    traduzir_texto,
    salvar_txt
)

# Função principal do tradutor
# Esta função coordena o processo de:
# - Solicitação de arquivo do usuário.
# - Verificação do tipo de arquivo (PDF com texto digital, PDF escaneado ou imagem).
# - Extração do texto adequado.
# - Tradução do texto extraído.
# - Salvamento do texto traduzido em um arquivo.
def tradutor_livros():
    # Garante que a pasta de saída exista
    os.makedirs("output", exist_ok=True)

    # Solicita o caminho do arquivo PDF ou imagem
    arquivo = input("Digite o caminho do arquivo (PDF ou imagem): ").strip()
    if not os.path.exists(arquivo):
        print("Arquivo não encontrado.")
        return

    # Seleciona método de extração com base no tipo de arquivo
    if arquivo.lower().endswith('.pdf'):
        # Se o PDF contiver texto digital, extrai o texto diretamente
        if verificar_pdf_com_texto(arquivo):
            print("PDF com texto digital. Extraindo...")
            texto = extrair_texto_pdf(arquivo)
        # Se o PDF for escaneado, aplica OCR
        else:
            print("PDF escaneado. Aplicando OCR...")
            texto = extrair_texto_ocr(arquivo)
    # Se o arquivo for uma imagem (JPEG, PNG), aplica OCR
    elif arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
        print("Imagem detectada. Aplicando OCR...")
        texto = extrair_texto_ocr(arquivo)
    else:
        print("Formato não suportado. Use PDF ou imagem.")
        return

    # Traduz o texto extraído
    print("Traduzindo texto...")
    texto_traduzido = traduzir_texto(texto)

    # Salva o texto traduzido em arquivo .txt
    txt_path = os.path.join("output", "livro_traduzido.txt")
    salvar_txt(texto_traduzido, txt_path)
    print(f"Texto traduzido salvo em: {os.path.abspath(txt_path)}")


# Execução principal do script
# Chama a função tradutor_livros() se o script for executado diretamente.
if __name__ == "__main__":
    tradutor_livros()

