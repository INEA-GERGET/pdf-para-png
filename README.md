# Gerar imagens de Antes e Depois a partir de PDFs

## Descrição

Repositório com para gerar as imagens de Antes e Depois dos laudos e embargos a partir de PDFs.

## Uso
Para utilizar os scripts deste repositório é necessário ter um ou mais PFDs na pasta de entrada nomeados como `{id-do-alerta}.pdf`. Dependendo do posicionamento das imagens de interesse no PDF, um dos scripts será melhor do que outro, portanto, verifique a seção Exemplos.

É necessário trocar os caminhos para os arquivos de entrada e saída:
```python
    # CAMINHO DOS AQUIVOS
    pasta_dos_pdfs = r"C:\Users\Nome de Usuário\Desktop\pdf-para-png\Antes_Depois"    # TROCAR
    pasta_das_imagens_geradas = r"C:\Users\Nome de Usuário\Desktop\pdf-para-png\Imagens"    # TROCAR
```

## Instalação

Para utilizar os scripts é necessária a instalação das bibliotecas Python:

* **configparser**: Para ler arquivos de configuração.
* **os**: Esta é uma biblioteca padrão do Python, então você não precisa instalá-la separadamente. Ela é usada para interagir com o sistema operacional, como manipular caminhos de arquivos e diretórios (os.path.exists, os.makedirs, os.path.join, os.listdir).
* **pdf2image**: Esta biblioteca é essencial para a conversão de PDF para imagem.
* **Pillow**: Usada para processar as imagens após a conversão.

## Requisitos Adicionais

Além das bibliotecas Python, esta função tem uma dependência externa crucial:

Poppler: É um utilitário de software para renderização de PDFs. A biblioteca pdf2image precisa do [Poppler 24.08.0](https://github.com/oschwartz10612/poppler-windows/releases/tag/v24.08.0-0) para funcionar. Sem o Poppler, a função não conseguirá converter os PDFs.
Você deve baixar os binários do Poppler e fornecer o caminho para eles na variável caminho_poppler dentro da sua função:
```python
# CAMINHO DA \Library\bin DO POPPLER 
caminho_poppler = r"C:\Users\Nome de Usuário\Downloads\poppler-24.08.0\Library\bin"    # TROCAR
```
