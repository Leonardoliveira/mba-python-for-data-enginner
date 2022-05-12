import os
import pandas as pd
from library import get_config
from library import get_files
from library import read_file_csv
from library import select_col


if __name__ == "__main__":

    os.system('cls')

    # carrega parametros
    config = get_config()

    input_file = config["directors"]["input_file"]
    output_file = config["directors"]["output_file"]
    columns_aula3 = config["columns_aula3"]
    file_class_2 = config["export_aula2"]["name"]
    export_to = config["export_aula2"]["ext"]
    find_title = config["find"]["title"]
    find_keywords = config["find"]["keywords"]
    find_abstract = config["find"]["abstract"]
    find_year = config["find"]["year"]
    find_type_publication = config["find"]["type_publication"]
    find_doi = config["find"]["doi"]
    find_jcr_value = config["find"]["jcr_value"]
    find_scimago_value = config["find"]["scimago_value"]
    
    # carrega a lista de arquivos alvos do ETL
    files = get_files(input_file, "CSV")

    lista_df = []
    
    # para cada arquivo repetir
    for file in files:

        # ler
        df_file = read_file_csv(input_file, file)
                
        # padronizar coluna title
        if file[0:3] == "jcs":
            df_file.rename(columns = {"Full Journal Title": "title"}, inplace = True)
        else:
            df_file.rename(columns = {"Title": "title"}, inplace = True)

        # convertendo dados da coluna para maiusculo
        df_file['title'] = df_file['title'].str.upper()
        
        # guarda o df na lista
        lista_df.append(df_file)

    #  join dfs por title criando novo df
    df_class_3 = pd.merge(lista_df[0], lista_df[1], how = 'inner', on = 'title')

    # padronizar colunas
    df_class_3 = select_col(df_class_3, columns_aula3)
  
    # deduplicacao de dados usando todas colunas
    df_class_3.drop_duplicates(keep = "first", inplace = True)
    df_class_3.to_excel('output/df_class_3' + '.xlsx', index = False)
   
    # ler CSV da aula 2
    df_class_2 = read_file_csv(output_file, file_class_2 + "." + export_to) 

    for col in df_class_2.columns:
        if df_class_2[col].dtype == "object":
            df_class_2[col] = df_class_2[col].str.upper()


    """ for col in df_class_2.columns:
        if df_class_2[col].str:
            df_class_2[col] = df_class_2[col].str.upper()

        print(col) """
        
    
    
    