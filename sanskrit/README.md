# Sanskrit OCR Processor

Este script automatiza o envio de imagens para o OCR do site [sanskritdictionary.com](https://ocr.sanskritdictionary.com) e salva os resultados em arquivos `.txt`.

## 📦 Estrutura de diretórios

└── README.md
└── src
	├── images/ ← Coloque aqui as imagens para processar
	├── ocrs/ ← Resultados serão salvos aqui
	├── script.py ← Script principal
	
	
## ▶️ Como usar

1. Coloque todas as imagens que deseja processar na pasta `images/`
2. Execute o script:
   ```bash
   python script.py
3. Os arquivos de texto com o OCR formatado serão salvos na pasta ocrs/

#📌 Funcionalidades
	Usa a API pública do sanskritdictionary.com
	Trata a pontuação "।" e "।।" com quebras de linha apropriadas
	Verifica automaticamente se o texto extraído é significativo (mais de 50 caracteres)

#📋 Requisitos
	Python 3.x
	Biblioteca requests:
	```bash
	pip install requests
	
MIT License

Copyright (c) 2025 Arthur Pereira Tavares
 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS  
IN THE SOFTWARE.

