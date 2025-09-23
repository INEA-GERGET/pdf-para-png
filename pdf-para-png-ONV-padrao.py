import os
from pdf2image import convert_from_path
from PIL import Image

def converter_pdfs_da_pasta(pasta_entrada, pasta_saida, formato='PNG'):
   """
    Converte a primeira página de todos os arquivos PDF de uma pasta para um formato de imagem,
    corta a imagem gerada e a salva em uma pasta de saída.

    A função itera sobre todos os arquivos PDF na `pasta_entrada`, converte a
    primeira página de cada PDF em uma imagem (PNG por padrão), e então corta
    a imagem para reter apenas uma seção específica. A imagem cortada
    é salva na `pasta_saida`. O caminho para o executável Poppler deve
    ser especificado dentro da função.

    Args:
        pasta_entrada (str): O caminho para o diretório contendo os arquivos PDF a serem processados.
        pasta_saida (str): O caminho para o diretório onde as imagens convertidas e cortadas serão salvas.
                           Se o diretório não existir, ele será criado.
        formato (str, opcional): O formato de saída para as imagens. 'PNG' por padrão.
                                 Outros formatos como 'JPEG' podem ser usados.

    Returns:
        None: A função não retorna nenhum valor. Ela realiza a operação de conversão
              e salvamento diretamente nos diretórios especificados.

    Raises:
        Exception: Captura e imprime mensagens de erro caso ocorram problemas
                   durante a conversão do PDF (ex: arquivo corrompido) ou o corte da imagem.
                   Note que o caminho do Poppler (`caminho_poppler`) deve ser ajustado
                   manualmente no código para o seu sistema.
    """
    
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    print(f"Procurando por arquivos PDF em: {pasta_entrada}")

    # Itera sobre todos os arquivos na pasta de entrada
    for nome_arquivo in os.listdir(pasta_entrada):
        if nome_arquivo.lower().endswith('.pdf'):
            caminho_completo_pdf = os.path.join(pasta_entrada, nome_arquivo)
            print(f"\nProcessando arquivo: {nome_arquivo}...")

            try:
                # CAMINHO DA \Library\bin DO POPPLER 
                caminho_poppler = r"C:\Users\Nome de Usuário\Downloads\poppler-24.08.0\Library\bin"    # TROCAR
                
                # Modificação: Adiciona first_page=1 e last_page=1 para converter apenas a primeira página.
                imagens = convert_from_path(caminho_completo_pdf, poppler_path=caminho_poppler, dpi=200, first_page=1, last_page=1)

                # O loop 'for' agora irá rodar apenas uma vez, pois a lista 'imagens' conterá somente uma imagem.
                for i, imagem in enumerate(imagens):
                    nome_base = os.path.splitext(nome_arquivo)[0]
                    caminho_saida_imagem = os.path.join(pasta_saida, f"{nome_base}.{formato.lower()}")
                    imagem.save(caminho_saida_imagem, formato.upper())
                    print(f"   -> Página {i + 1} salva como: {caminho_saida_imagem}")

                    # SEÇÃO PARA CORTAR A IMAGEM
                    try:
                        img = Image.open(caminho_saida_imagem)
                        largura, altura = img.size

                        # Calcular a coordenada Y inicial
                        y_inicial = int(altura * 0.135)

                        # Calcular a coordenada Y final 
                        y_final = int(altura * 0.445) 

                        # Definir a caixa de corte (mantém a largura e corta as partes superior e inferior)
                        # A caixa de corte é definida por (esquerda, topo, direita, base)
                        caixa_corte = (0, y_inicial, largura, y_final)

                        # Cortar a imagem
                        img_cortada = img.crop(caixa_corte)

                        # Salvar a imagem cortada, substituindo a original
                        img_cortada.save(caminho_saida_imagem, formato.upper())
                        print(f"    -> Imagem cortada. Dimensões: {img_cortada.size[0]}x{img_cortada.size[1]} pixels.")

                    except Exception as e:
                        print(f"    -> ERRO ao cortar a imagem: {e}")
            except Exception as e:
                print(f"ERRO ao processar o arquivo {nome_arquivo}: {e}")

if __name__ == "__main__":
    
    # CAMINHO DOS AQUIVOS
    pasta_dos_pdfs = r"C:\Users\Nome de Usuário\Desktop\pdf-para-png\Antes_Depois"    # TROCAR
    pasta_das_imagens_geradas = r"C:\Users\Nome de Usuário\Desktop\pdf-para-png\Imagens"    # TROCAR

    converter_pdfs_da_pasta(pasta_dos_pdfs, pasta_das_imagens_geradas, formato='PNG')

    print("\nConversão concluída!")
