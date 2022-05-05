import pandas as pd
import numpy as np
from funcoes import get_files
from funcoes import read_file
from funcoes import select_col
from funcoes import gerar_arquivo
from funcoes import get_config_export


# definições de diretórios
entrada = "input/"
saida = "output/"

# carregando a lista de arquivos de dados
files = get_files(entrada)

# criando um DF em branco para armazenar todos os arquivos
df_final = pd.DataFrame()

# para cada arquivo repetir
for file in files:
    
    # carregando dados do arquivo para um DF
    df_geral = read_file(entrada, file)
    
    print("\nArquivo {} carregado: {} linhas e {} colunas"
    .format(file, df_geral.shape[0], df_geral.shape[1] ))
    
    # criando um novo DF selecionando colunas
    new_df = select_col(df_geral)
    print("Novo DF criado, dimensões: {}".format(new_df.shape))
    
    # concatendando cada novo DF no DF Final
    df_final = pd.concat([df_final, new_df]) 
    print("DF Final {}".format(df_final.shape))

# ler configuracao em arquivo externo para pegar o valor da tag export_to
formato = get_config_export("export_to")

# gerar arquivo final no formato configurado
gerar_arquivo(formato, df_final, saida)
print("\nArquivo exportado no formato {} e disponivel na pasta {}".format(formato, saida))