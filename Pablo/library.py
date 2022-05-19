import os
import pandas as pd
import numpy as np
import yaml
import bibtexparser

# Função para criar um lista dos arquivos BibTex existentes no diretório de entrada 
def get_files(dir, ext) -> list:

    # carregando os arquivos da pasta entrada
    dir_list = os.listdir(dir)
    files_list = []
 
    for file in dir_list:
    
        # validar se o arquivo do diretório possui a extensao = ext
        if ext.upper() not in file.upper():
            continue

        files_list.append(file)
    
    return files_list


# função para carregar o arquivo em um DF
def read_file_bib(dir, file) -> pd.DataFrame:

    with open(dir + "/" + file, encoding = "utf_8" ) as bibtex_file:

        bib_database = bibtexparser.load(bibtex_file)

        # retornando um DF do arquivo 
        df = pd.DataFrame(bib_database.entries)

    return df


def read_file_csv(dir, file) -> pd.DataFrame:

  df = pd.read_csv(dir + "/" + file, low_memory = False, sep = ";")

  return df


# Função para criar um novo DF com as colunas do escopo baseado no DF Geral
def select_col(df_geral, columns_out) -> pd.DataFrame:
  
  new_df = pd.DataFrame()

  for value in columns_out.values():

  # interar lista de todos os tipos de colunas
    for col in value:
      # verificar se um item do tipo existe no DF
      if col in df_geral.columns:
        # se existir criar um nova coluna no new_DF com o rótulo do primeiro item da lista do tipo da coluna
        new_df[value[0]] = df_geral[col]
        break
      else:
        # se a coluna não existir então verificar se é a última coluna da lista do tipo
        # isso significa que não existe a coluna no DF, então criar um coluna com o rótulo do primeiro item 
        # com conteúdo em branco
        if col == value[-1]:
          new_df[value[0]] = np.nan

  return new_df


# funcao para ler o arquivo externo YAML
def get_config() -> dict:

  with open('config\config.yaml', 'r') as config:
    file_yaml = yaml.safe_load(config)

  return file_yaml


# funcao para gerar um arquivo texto no formato dedinido no arquivo de configuração
def write_file(df_final, folder_output, file_name, ext) -> None:

  arquivo_saida = "{}/{}.{}".format(folder_output, file_name, ext)

  if ext == "json":
    dados_arquivo = df_final.to_json(orient = "table")

    with open(arquivo_saida, "w") as arquivo:
      arquivo.write(dados_arquivo)

  elif ext == "csv":
    df_final.to_csv(arquivo_saida, sep = ";", header = True, index=False)

  elif ext == "yaml":
    dict_final = df_final.to_dict()

    with open(arquivo_saida, 'w') as file:
      yaml.dump(dict_final, file)

  return None



 