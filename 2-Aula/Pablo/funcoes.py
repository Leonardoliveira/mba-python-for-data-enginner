import os
import bibtexparser
import pandas as pd
import numpy as np
import yaml

"""
Função para criar um lista dos arquivos BibTex existentes no diretório de entrada 
"""
def get_files(dir):

    # carregando os arquivos da pasta entrada
    dir_list = os.listdir(dir)
    files_list = []
    
    for file in dir_list:
    
        # validar se o arquivo do diretório possui a extensao .bib
        if '.BIB' not in file.upper():
            continue

        files_list.append(file)
    
    return files_list


"""
função para carregar o arquivo em um DF
"""
def read_file(dir, file):
    
    with open(dir + file, encoding = "utf_8" ) as bibtex_file:
        
        bib_database = bibtexparser.load(bibtex_file)
        
        # retornando um DF do arquivo 
        df = pd.DataFrame(bib_database.entries)

    return df


# Função para criar um novo DF com as colunas do escopo baseado no DF Geral
def select_col(df_geral):
    
    # criando um lista com as colunas do escopo do projeto
    col_types = [["author"],["title"],["keywords"],["abstract"],["year"],
                 ["type_publication","ENTRYTYPE"],["doi"]]
    
    new_df = pd.DataFrame()

    # interar lista de todos os tipos de colunas
    for col_type in col_types:

        # interar uma lista de um tipo de coluna apenas
        for col in col_type:

            # verificar se um item do tipo existe no DF
            if col in df_geral.columns:
                # se existir criar um nova coluna no new_DF com o rótulo do primeiro item da lista do tipo da coluna
                new_df[col_type[0]] = df_geral[col]
                break
            else:
                # se a coluna não existir então verificar se é a última coluna da lista do tipo
                # isso significa que não existe a coluna no DF, então criar um coluna com o rótulo do primeiro item 
                # com conteúdo em branco
                if col == col_type[-1]:
                    new_df[col_type[0]] = np.nan
  
    return new_df


# funcao para ler o parametro "export_to" setado no arquivo externo YAML
def get_config_export(parameter):

  with open('config/config.yaml', 'r') as config:
    valor_parametro = yaml.load(config, Loader=yaml.FullLoader)[parameter]

  return valor_parametro    


# funcao para gerar um arquivo texto no formato dedinido no arquivo de configuração
def gerar_arquivo(formato, df_final, saida):

  arquivo_saida = saida + "arquivo_final." + formato

  match formato:
    case "json":
      dados_arquivo = df_final.to_json(orient = "table")

      with open(arquivo_saida, "w") as arquivo:
        arquivo.write(dados_arquivo)

    case "csv":
      df_final.to_csv(arquivo_saida, sep = ";", header = True)
  
    case "yaml":
      dict_final = df_final.to_dict()

      with open(arquivo_saida, 'w') as file:
        yaml.dump(dict_final, file)  