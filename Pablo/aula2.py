import pandas as pd
from library import get_files
from library import read_file
from library import select_col
from library import gerar_arquivo
from library import get_config_export


"""
read config
"""
config = get_config_export()

input_file = config["directors"]["input_file"]
output_file = config["directors"]["output_file"]
export_to = config["export_to"]
columns_aula2 = config["columns_aula2"]

# carregando a lista de arquivos de dados
files = get_files(input_file)

# criando um DF em branco para armazenar todos os arquivos
df_final = pd.DataFrame()

# para cada arquivo repetir
for file in files:
    
    # carregando dados do arquivo para um DF
    df_geral = read_file(input_file, file)
    
    print("\nArquivo {} carregado: {} linhas e {} colunas"
    .format(file, df_geral.shape[0], df_geral.shape[1] ))
    
    # criando um novo DF selecionando colunas
    new_df = select_col(df_geral, columns_aula2)
    print("Novo DF criado, dimensões: {}".format(new_df.shape))
  
    # concatendando cada novo DF no DF Final
    df_final = pd.concat([df_final, new_df]) 
    print("DF Final {}".format(df_final.shape))

# gerar arquivo final no formato configurado
gerar_arquivo(export_to, df_final, output_file)
print("\nArquivo exportado no formato {} e disponivel na pasta {}"
.format(export_to, output_file))