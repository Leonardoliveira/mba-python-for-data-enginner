import os
import pandas as pd
from library import get_config
from library import get_files
from library import read_file_csv
from library import select_col
from library import write_file

if __name__ == "__main__":

    os.system('cls')

    # carrega parametros
    config = get_config()

    input_file = config["directors"]["input_file"]
    output_file = config["directors"]["output_file"]
    columns_aula3 = config["columns_aula3"]
    file_class_2 = config["export_aula2"]["name"]
    import_ext = config["export_aula2"]["ext"]
    find_title = config["find"]["title"]
    find_keywords = config["find"]["keywords"]
    find_abstract = config["find"]["abstract"]
    find_year = config["find"]["year"]
    find_type_publication = config["find"]["type_publication"]
    find_doi = config["find"]["doi"]
    find_jcr_value = config["find"]["jcr_value"]
    find_scimago_value = config["find"]["scimago_value"]
    file_class_3 = config["export_aula3"]["name"]
    export_to = config["export_aula3"]["ext"]

    """ EXTRACT AULA 3"""
    # carrega a lista de arquivos alvos do ETL
    files = get_files(input_file, "CSV")

    lista_df = []

    """ TRANSFORMATION AULA 3"""
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

    """ EXTRACT AULA 2 """
    # ler CSV da aula 2
    df_class_2 = read_file_csv(output_file, file_class_2 + "." + import_ext) 
    
    """ TRANSFORMATION AULA 2 """
    df_class_2.drop_duplicates(keep = "first", inplace = True)

    #convertendo todas strings para maiusculo
    for col in df_class_2.columns:
        if df_class_2[col].dtype == "object" and col != "doi":
            df_class_2[col] = df_class_2[col].str.upper()
   
    df_class_2.fillna("BD", inplace = True)

    df_class_2.to_excel('output/df_class_2' + '.xlsx', index = False)
    
    # unir com a aula 3
    df_final = pd.merge(df_class_2, df_class_3, how = 'left', on = 'title')

    # filtrar
    if find_title is not None:
        find_title = df_final.title.str.contains(find_title)
        df_final = df_final.loc[find_title]

    if find_keywords is not None:
        find_keywords = df_final.keywords.str.contains(find_keywords)
        df_final = df_final.loc[find_keywords]
    
    if find_abstract is not None:
        find_abstract = df_final.abstract.str.contains(find_abstract)
        df_final = df_final.loc[find_abstract]   

    if find_year is not None:
        find_year = df_final.year == find_year
        df_final = df_final.loc[find_year]

    if find_type_publication is not None:
        find_type_publication = df_final.type_publication.str.contains(find_type_publication)
        df_final = df_final.loc[find_type_publication]
    
    if find_doi is not None:
        find_doi = df_final.doi.str.contains(find_doi)
        df_final = df_final.loc[find_doi]

    if find_jcr_value is not None:
        find_jcr_value = df_final.jcr_value == find_jcr_value
        df_final = df_final.loc[find_jcr_value]  

    if find_scimago_value is not None:
        find_scimago_value = df_final.scimago_value == find_scimago_value
        df_final = df_final.loc[find_scimago_value]  
               

    df_final.to_excel('output/df_final' + '.xlsx', index = False)
    print("Resultado {} linhas encontradas".format(df_final.shape[0]))

    # gerar arquivo final no formato configurado
    write_file(df_final, output_file, file_class_3, export_to)
    print("\nArquivo {} exportado no formato {} e disponivel na pasta {}"
    .format(file_class_3, export_to, output_file))
                        
    
