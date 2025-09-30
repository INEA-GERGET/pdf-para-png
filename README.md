# Gerar imagens de Antes e Depois a partir de PDFs

## Sumário
1. [Descrição](#Descrição)
2. [Uso](#Uso)
   - [Sobre os arquivos](#Sobre-os-arquivos)
4. [Instalação](#Instalação)
5. [Requisitos adicionais](#Requisitos-adicionais)
6. [Exemplos](#Exemplos)

## Descrição

Repositório com para gerar as imagens de Antes e Depois dos [laudos](https://github.com/INEA-GERGET/ONV-laudo-do-alerta) e [embargos](https://github.com/INEA-GERGET/ONV-laudo-de-embargo-cautelar) a partir de PDFs de fontes diferentes: OVNpadrão, ONVantigo (não padronizado, antes de Outubro de 2025), MapBiomas e BrasilMAIS.

## Uso
Para utilizar os scripts deste repositório é necessário colocar os PFDs nas pastas de entradas de acordo com sua origem, cada pasta cria uma sessão de corte diferente nos arquivos, portanto, atente-se à isso. Os PDFs devem estar nomeados como `{id-do-alerta}.pdf`. 

É necessário trocar os caminhos para os arquivos de entrada e saída:
```python
    # MODIFIQUE O CAMINHO DA PASTA RAIZ
    pasta_raiz = r"C:\Users\Nome-do-usuário\Desktop\pdf_para_png"
```

### Sobre os arquivos

* [**AD_BrasilMAIS**](/AD_BrasilMAIS): Nesta pasta ficarão os PDFs com origem do Brasil MAIS. O arquivo que está nela é apenas para teste e deve ser apagado após o teste do script.
* [**AD_MapBiomas_ONVpadrao**](/AD_MapBiomas_ONVpadrao): Nesta pasta ficarão os PDFs com origem do Map Biomas e os gerados a partir do modelo padrão do ONV ([`layout-ONVpadrao.pagx`](layout-ONVpadrao.pagx)). Os arquivos que estão nesta pasta são apenas para teste e devem ser apagados após o teste do script.
* [**AD_ONVantigo**](/AD_ONVantigo): Nesta pasta ficarão os PDFs com origem do ONV, mas que não foram gerados com o modelo padrão do ONV ([`layout-ONVpadrao.pagx`](layout-ONVpadrao.pagx)). O arquivo que está nela é apenas para teste e deve ser apagado após o teste do script.
* [**layout-ONVpadrao.pagx**](layout-ONVpadrao.pagx): É o modelo para gerar os PDFs ONVpadrão dentro do [ArcGISpro](https://pro.arcgis.com/en/pro-app/latest/get-started/download-arcgis-pro.htm).
* [**pdf-para-png.py**](pdf-para-png.py): É o script em Python para cortar e salvar as imagens dos PDFs.

## Instalação

Para utilizar os scripts é necessária a instalação das bibliotecas Python:

* **configparser**: Para ler arquivos de configuração.
* **os**: Esta é uma biblioteca padrão do Python, então você não precisa instalá-la separadamente. Ela é usada para interagir com o sistema operacional, como manipular caminhos de arquivos e diretórios (os.path.exists, os.makedirs, os.path.join, os.listdir).
* **pdf2image**: Esta biblioteca é essencial para a conversão de PDF para imagem.
* **Pillow**: Usada para processar as imagens após a conversão.

## Requisitos adicionais

Além das bibliotecas Python, esta função tem uma dependência externa crucial:

Poppler: É um utilitário de software para renderização de PDFs. A biblioteca pdf2image precisa do [Poppler 24.08.0](https://github.com/oschwartz10612/poppler-windows/releases/tag/v24.08.0-0) para funcionar. Sem o Poppler, a função não conseguirá converter os PDFs.
Você deve baixar os binários do Poppler e fornecer o caminho `...\Libary\bin` na variável caminho_poppler dentro da sua função:
```python
    # MODIFIQUE O CAMINHO DO SEU POPPLER
    caminho_poppler = r"C:\Users\Nome-do-usuário\Downloads\poppler-24.08.0\Library\bin"
```

## Exemplos 

O scripts pode ter as seguintes saídas de corte de imagens: 
* **Map Biomas e ONV padrão** -> Os arquivos do MapBiomas deverão ser salvos junto com os gerados pelo ONV com o modelo padrão em uma pasta chamada `AD_MapBiomas_ONVpadrao` e terão o seguinte recorte:
<img src="/arquivo-readme/corte-MapBiomas.png"/>

* **ONV antigo** -> Os arquivos anteriores à Outubro de 2025 deverão ser salvos na pasta `AD_ONVantigo` e terão os seguintes recortes:
<img src="/arquivo-readme/corte-ONVantigo.png"/>

* **Brasil MAIS** -> Os arquivos retirados do Brasil MAIS deverão ser salvos na pasta `AD_BrasilMAIS` e terão o seguinte recorte:
<img src="/arquivo-readme/corte-BrasilMAIS.png"/>
