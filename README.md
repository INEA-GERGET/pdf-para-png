# Gerar imagens de Antes e Depois a partir de PDFs

## Descrição

Repositório com para gerar as imagens de Antes e Depois dos [laudos](https://github.com/INEA-GERGET/ONV-laudo-do-alerta) e [embargos](https://github.com/INEA-GERGET/ONV-laudo-de-embargo-cautelar) a partir de PDFs de fontes diferentes: OVNpadrão, ONVantigo (não padronizado, antes de Outubro de 2025), MapBiomas e BrasilMAIS.

## Uso
Para utilizar os scripts deste repositório é necessário colocar os PFDs nas pastas de entradas de acordo com sua origem, cada pasta cria uma sessão de corte diferente nos arquivos, portanto, atente-se à isso. Os PDFs devem estar nomeados como `{id-do-alerta}.pdf`. 

É necessário trocar os caminhos para os arquivos de entrada e saída:
```python
# MODIFIQUE OS CAMINHOS ABAIXO PARA AS SUAS PASTAS
    pasta_MapBiomas_ONVpadrao = r"C:\Users\Nome-do-Usuário\Desktop\pdf_para_png\AD_MapBiomas_ONVpadrao"
    pasta_ONVantigo = r"C:\Users\Nome-do-Usuário\Desktop\pdf_para_png\AD_ONVantigo"
    pasta_BrasilMAIS = r"C:\Users\Nome-do-Usuário\Desktop\pdf_para_png\AD_BrasilMAIS"
    pasta_das_imagens_geradas = r"C:\Users\Nome-do-Usuário\Desktop\pdf_para_png\antes_depois"
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
Você deve baixar os binários do Poppler e fornecer o caminho `...\Libary\bin` na variável caminho_poppler dentro da sua função:
```python
# MODIFIQUE O CAMINHO DO SEU PROPPLER
caminho_poppler = r"C:\Users\barbarabic\Downloads\poppler-24.08.0\Library\bin"
```

## Exemplos 

O scripts pode ter as seguintes saídas de corte de imagens: 
* **Map Biomas e ONV padrão** -> Os arquivos do MapBiomas deverão ser salvos junto com os gerados pelo ONV com o modelo padrão em uma pasta chamada `AD_MapBiomas_ONVpadrao` e terão o seguinte recorte:
<img src="/arquivo-readme/corte-MapBiomas.png"/>

* **ONV antigo** -> Os arquivos anteriores à Outubro de 2025 deverão ser salvos na pasta `AD_ONVantigo` e terão os seguintes recortes:
<img src="/arquivo-readme/corte-ONVantigo.png"/>

* **Brasil MAIS** -> Os arquivos retirados do Brasil MAIS deverão ser salvos na pasta `AD_BrasilMAIS` e terão o seguinte recorte:
<img src="/arquivo-readme/corte-BrasilMAIS.png"/>
