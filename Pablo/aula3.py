import os
import pandas as pd
from library import get_files
from library import read_file_csv
from library import select_col
from library import write_file
from config.config import *
from library import * 

if __name__ == "__main__":

    os.system('cls')

    print("\nCarregando a lista de arquivos CSV na pasta {} ...".format(input_file))
    files = get_files(input_file, "CSV")

    lista_df = []

    print("\nIniciando a transformacao ...")
    for file in files:

        print("\nLendo fonte de dados {} ...".format(file))
        df_file = read_file_csv(input_file, file) 

        print("Padronizando coluna {} ...".format(title_default))
        if file[0:3] == "jcs":
            title_source = title_jcs
        else:
            title_source = title_scm

        df_file.rename(columns = {title_source: title_default}, inplace = True)
        
        print("Padronizando para maiusculo ...")
        df_file[title_default] = df_file[title_default].str.upper()

        lista_df.append(df_file)

        if show_excel:
            print("Gerando planilha excel para conferencia do {} ...".format(file))
            df_file.to_excel("output/etapa1_" + file[0:3] + ".xlsx", index = False)

    print("\nUnindo fonte de dados ...")
    df_class_3 = pd.merge(lista_df[0], lista_df[1], how = 'inner', on = title_default)

    print("Selecionando colunas de acordo com escopo ...")
    df_class_3 = select_col(df_class_3, columns_aula3)

    print("Limpando dados repetidos ...")
    df_class_3.drop_duplicates(keep = "first", inplace = True)

    if show_excel:
        print("Gerando planilha excel com dados unidos para conferencia ...")
        df_class_3.to_excel("output/etapa2_join.xlsx", index = False)
    
    print("\nLendo arquivo de dados da aula 2 {} ...".format(file_class_2))
    df_class_2 = read_file_csv(output_file, file_class_2) 
    df_class_2.drop_duplicates(keep = "first", inplace = True)

    print("Padronizando para maiusculo ...")
    for col in df_class_2.columns:
        if df_class_2[col].dtype == "object" and col != "doi":
            df_class_2[col] = df_class_2[col].str.upper()
   
    df_class_2.fillna("BD", inplace = True)

    if show_excel:
        print("Gerando planilha excel com dados de {} ...".format(file_class_2))
        df_class_2.to_excel('output/etapa3_aula2.xlsx', index = False)
    
    print("Unindo dados da aula 2 com os da aula 3 ...")
    df_final = pd.merge(df_class_2, df_class_3, how = 'left', on = 'title')

    print("\nFiltrando dados ...")
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
               
    print("\nResultado {} linhas encontradas".format(df_final.shape[0]))

    # gerar arquivo final no formato configurado
    write_file(df_final, output_file, file_class_3, export_to)
    print("\nArquivo {} exportado no formato {} e disponivel na pasta {}"
    .format(file_class_3, export_to, output_file))

    if show_excel:
        print("Gerando planilha excel dos dados do final do processo ...")
        df_final.to_excel('output/etapa4_final.xlsx', index = False)
    
    print("\nConcluido :)")
                        
    
