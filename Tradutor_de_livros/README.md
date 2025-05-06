# Tradutor de Livros

Este projeto tem como objetivo traduzir o conteúdo de arquivos **PDF** ou **imagens** (com OCR). O código extrai o texto, traduz para o idioma português e salva o texto traduzido em um arquivo `.txt`.

## Estrutura do Projeto

	Tradutor_de_livros/
	│
	├── README.md # Documentação do projeto
	├── requirements.txt # Dependências do projeto
	├── tradutor_livros/ # Código-fonte
	│ ├── main.py # Arquivo principal para execução
	│ ├── utils.py # Funções auxiliares


## Bibliotecas Necessárias

Este projeto depende das seguintes bibliotecas Python:

- **pytesseract**: Para realizar OCR (Reconhecimento Óptico de Caracteres) em imagens.
- **PyMuPDF**: Para manipulação e extração de texto de arquivos PDF.
- **pdf2image**: Para converter páginas de PDF em imagens.
- **deep-translator**: Para realizar a tradução do texto extraído para o português.
  
Para instalar as dependências, basta rodar o comando:

```bash
pip install -r requirements.txt
```
Nota: Para usar o OCR do pytesseract, você precisa ter o Tesseract OCR instalado no seu sistema.

# Como Usar
1. Prepare o ambiente
	Clone o repositório e instale as dependências:

	git clone [https://github.com/arthur-202/Tradutor_de_livros.git](https://github.com/arthur-202/Portifolio/tree/main/Tradutor_de_livros)
	
 	cd Tradutor_de_livros
	pip install -r requirements.txt

2. Execute o Programa
   
	Após instalar as dependências, você pode executar o tradutor diretamente utilizando o arquivo main.py:
	python tradutor_livros/main.py

O programa solicitará o caminho do arquivo PDF ou imagem (JPG, PNG, JPEG). Ele irá verificar o tipo de arquivo, extrair o texto e traduzi-lo. O texto traduzido será salvo em um arquivo livro_traduzido.txt dentro da pasta output.

3. Arquivo de Entrada

	O programa suporta os seguintes formatos de entrada:

	PDFs com texto digital: O programa extrai o texto diretamente.
	PDFs escaneados: O texto é extraído utilizando OCR.
	Imagens (JPG, PNG, JPEG): O texto é extraído utilizando OCR.

4. Resultado
	O texto traduzido será salvo em um arquivo livro_traduzido.txt dentro da pasta output.


# Tradutor de Livros

## Explicação do Código

### Funções Principais

#### `tradutor_livros()`
Esta é a função principal que coordena todo o processo. Ela:

1. Solicita ao usuário o caminho de um arquivo PDF ou imagem.
2. Verifica se o arquivo existe.
3. Determina o método adequado para extrair o texto do arquivo (usando OCR ou extração direta de texto de PDF).
4. Traduz o texto extraído utilizando o Google Translator.
5. Salva o texto traduzido no arquivo `livro_traduzido.txt`.

#### `verificar_pdf_com_texto(pdf_path)`
Verifica se o arquivo PDF contém texto digital, ou se ele é apenas uma imagem escaneada.

#### `extrair_texto_pdf(pdf_path)`
Extrai o texto de um PDF que contém texto digital. Utiliza a biblioteca PyMuPDF para abrir o PDF e ler o texto das páginas.

#### `extrair_texto_ocr(pdf_path)`
Realiza a extração de texto utilizando OCR (Reconhecimento Óptico de Caracteres) para arquivos escaneados (ou imagens). Usa o pytesseract para fazer o OCR e a biblioteca pdf2image para converter as páginas do PDF em imagens.

#### `dividir_texto_em_blocos(texto, tamanho_maximo=4000)`
Divide o texto em blocos menores para que ele possa ser processado pela API de tradução, que tem um limite de caracteres por requisição.

#### `traduzir_texto(texto)`
Utiliza o GoogleTranslator da biblioteca deep-translator para traduzir o texto em blocos. A tradução é feita para o português.

#### `salvar_txt(texto, output_path)`
Salva o texto traduzido em um arquivo `.txt` na pasta de saída.

---

## Exemplo de Uso

1. Execute o programa:
   ```bash
   python tradutor_livros/main.py

2. Digite o caminho do arquivo:
	Se for um PDF com texto, o texto será extraído diretamente.
	Se for um PDF escaneado ou uma imagem, o OCR será aplicado.
3. O programa irá traduzir o texto e salvar o arquivo traduzido em output/livro_traduzido.txt.

#Contribuições
Este é um projeto open-source. Contribuições são bem-vindas! Para contribuir:
1. Faça um fork deste repositório.
2. Crie uma branch para sua funcionalidade ou correção:

git checkout -b feature/nova-funcionalidade
git commit -am 'Adiciona nova funcionalidade'
git push origin feature/nova-funcionalidade

Abra um pull request.

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
