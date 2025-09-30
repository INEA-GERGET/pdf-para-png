import os
from pdf2image import convert_from_path
from PIL import Image

# 1. Configurações de Corte por Tipo de PDF
# A caixa de corte é definida como (x_inicial, y_inicial, x_final, y_final)
# Os valores são as proporções (0.0 a 1.0) da largura/altura total.

# MapBiomas / OVNpadrão: Corta Topo (44%) e Base (25%) -> Mantém 44% a 75% da altura.
CROP_CONFIGS = {
    "MapBiomas_ONVpadrao": {
        "x_initial": 0.0,
        "y_initial": 0.44,
        "x_final": 1.0,
        "y_final": 0.75
    },
    # BrasilMAIS: Corta de 4.5% a 32.5% da altura e de 6% a 85% da largura.
    "BrasilMAIS": {
        "x_initial": 0.06,
        "y_initial": 0.045,
        "x_final": 0.85,
        "y_final": 0.325
    },
    # ONVantigo: Corta de 3% a 55% da altura.
    "ONVantigo": {
        "x_initial": 0.0,
        "y_initial": 0.0,
        "x_final": 1.0,
        "y_final": 0.55
    }
}

def processar_pdfs(pasta_entrada: str, pasta_saida: str, caminho_poppler: str, crop_config: dict, formato: str = 'PNG'):
    """
    Processa todos os PDFs em uma pasta, convertendo a primeira página para imagem 
    e aplicando um corte baseado na configuração fornecida.

    Args:
        pasta_entrada (str): Caminho para a pasta que contém os arquivos PDF.
        pasta_saida (str): Caminho para a pasta onde as imagens PNG serão salvas.
        caminho_poppler (str): Caminho para o executável poppler (necessário para pdf2image).
        crop_config (dict): Dicionário com as proporções de corte (x_initial, y_initial, x_final, y_final).
        formato (str, optional): Formato de saída da imagem (ex: 'PNG', 'JPEG'). Padrão: 'PNG'.
    """
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # 2. Pré-calcula as extensões (para evitar chamadas de função no loop)
    extensao_formato = f".{formato.lower()}"
    formato_upper = formato.upper()
    
    print(f"--- Iniciando processamento ({list(crop_config.keys())[0]}) ---")
    print(f"Procurando por arquivos PDF em: {pasta_entrada}")

    # 3. Itera de forma mais segura com listdir + tratamento de erros
    for nome_arquivo in os.listdir(pasta_entrada):
        if nome_arquivo.lower().endswith('.pdf'):
            caminho_completo_pdf = os.path.join(pasta_entrada, nome_arquivo)
            print(f"\nProcessando arquivo: {nome_arquivo}...")

            try:
                # CONVERSÃO DE PDF PARA IMAGEM (Apenas a primeira página)
                # O dpi=200 pode ser ajustado para melhor qualidade/desempenho
                imagens = convert_from_path(
                    caminho_completo_pdf, 
                    poppler_path=caminho_poppler, 
                    dpi=200, 
                    first_page=1, 
                    last_page=1
                )

                if not imagens:
                     print(f" -> ⚠️Aviso: Não foi possível extrair a primeira página de {nome_arquivo}.")
                     continue

                # O loop 'for' roda apenas uma vez (para a primeira página)
                imagem = imagens[0]
                nome_base = os.path.splitext(nome_arquivo)[0]
                caminho_saida_imagem = os.path.join(pasta_saida, f"{nome_base}{extensao_formato}")
                
                # Salva a imagem temporariamente (ou diretamente na memória, mas manter o salvamento simplifica o fluxo)
                imagem.save(caminho_saida_imagem, formato_upper)
                print(f"  -> Imagem base salva: {caminho_saida_imagem}")

                # SEÇÃO PARA CORTAR A IMAGEM
                try:
                    # Reabre a imagem para cortar (poderia usar 'imagem' diretamente, mas reabrir garante que o formato foi aplicado)
                    img = Image.open(caminho_saida_imagem)
                    largura, altura = img.size

                    # Calcula as coordenadas de corte em pixels
                    x_inicial = int(largura * crop_config["x_initial"])
                    y_inicial = int(altura * crop_config["y_initial"])
                    x_final = int(largura * crop_config["x_final"])
                    y_final = int(altura * crop_config["y_final"])

                    # Definir a caixa de corte (esquerda, topo, direita, base)
                    caixa_corte = (x_inicial, y_inicial, x_final, y_final)

                    # Cortar e salvar, substituindo o arquivo original
                    img_cortada = img.crop(caixa_corte)
                    img_cortada.save(caminho_saida_imagem, formato_upper)
                    
                    print(f"    -> ✅Imagem cortada e salva. Dimensões: {img_cortada.size[0]}x{img_cortada.size[1]} pixels.")

                except Exception as e:
                    print(f"    -> ❌ERRO ao cortar a imagem: {e}")
            
            except Exception as e:
                print(f"❌ERRO ao processar o arquivo {nome_arquivo}: {e}")
    
    print(f"--- Processamento concluído ({list(crop_config.keys())[0]}) ---")

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    # MODIFIQUE O CAMINHO DO SEU POPPLER
    caminho_poppler = r"C:\Users\Nome-do-usuário\Downloads\poppler-24.08.0\Library\bin"

    # MODIFIQUE O CAMINHO DA PASTA RAIZ
    pasta_raiz = r"C:\Users\Nome-do-usuário\Desktop\pdf_para_png"
    
    # MODIFIQUE O NOME DAS PASTAS APENAS SE NECESSÁRIO
    pasta_MapBiomas_ONVpadrao = os.path.join(pasta_raiz, "AD_MapBiomas_ONVpadrao")
    pasta_ONVantigo = os.path.join(pasta_raiz, "AD_ONVantigo")
    pasta_BrasilMAIS = os.path.join(pasta_raiz, "AD_BrasilMAIS")
    pasta_das_imagens_geradas = os.path.join(pasta_raiz, "antes_depois")
    
    # 4. Chama a função única para cada tipo de configuração
    processar_pdfs(
        pasta_MapBiomas_ONVpadrao, 
        pasta_das_imagens_geradas, 
        caminho_poppler, 
        CROP_CONFIGS["MapBiomas_ONVpadrao"], 
        formato='PNG'
    )
    
    processar_pdfs(
        pasta_ONVantigo, 
        pasta_das_imagens_geradas, 
        caminho_poppler, 
        CROP_CONFIGS["ONVantigo"], 
        formato='PNG'
    )
    
    processar_pdfs(
        pasta_BrasilMAIS, 
        pasta_das_imagens_geradas, 
        caminho_poppler, 
        CROP_CONFIGS["BrasilMAIS"], 
        formato='PNG'
    )
    
    print("\n✅ ✨ TODAS AS CONVERSÕES CONCLUÍDAS! ✨")
