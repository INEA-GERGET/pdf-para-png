import os
from pdf2image import convert_from_path
from PIL import Image

def converter_pdfs_da_pasta(pasta_entrada, pasta_saida, formato='PNG'):
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    print(f"Procurando por arquivos PDF em: {pasta_entrada}")

    # Itera sobre todos os arquivos na pasta de entrada
    for nome_arquivo in os.listdir(pasta_entrada):
        if nome_arquivo.lower().endswith('.pdf'):
            caminho_completo_pdf = os.path.join(pasta_entrada, nome_arquivo)
            print(f"\nProcessando arquivo: {nome_arquivo}...")

            try:
                # 1. Cole o seu caminho exato do poppler aqui.
                caminho_poppler = r"C:\Users\barbarabic\Downloads\poppler-24.08.0\Library\bin"
                
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

                        # Calcular a coordenada Y inicial para cortar os 40% superiores
                        y_inicial = int(altura * 0.41)

                        # Calcular a coordenada Y final para cortar os 20% inferiores
                        y_final = int(altura * 0.75) 

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
    # Configure suas pastas aqui
    pasta_dos_pdfs = r"C:\Users\barbarabic\Desktop\Script fotos do pdf\Antes_Depois_Embargo_OPMAEP"
    pasta_das_imagens_geradas = r"C:\Users\barbarabic\Desktop\Script fotos do pdf\Antes_Depois_Embargo_OPMAEP\Imagens"

    converter_pdfs_da_pasta(pasta_dos_pdfs, pasta_das_imagens_geradas, formato='PNG')
    print("\nConversão concluída!")