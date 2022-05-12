import pandas as pd
from library import get_files
from library import read_file_bib
from library import select_col
from library import gerar_arquivo
from library import get_config


if __name__ == "__main__":

    config = get_config()

    input_file = config["directors"]["input_file"]
    output_file = config["directors"]["output_file"]
    export_to = config["export_aula2"]["ext"]
    file_name_exp = config["export_aula2"]["name"]

    columns_aula2 = config["columns_aula2"]

    # carregando a lista de arquivos de dados
    files = get_files(input_file, "BIB")

    # criando um DF em branco para armazenar todos os arquivos
    df_final = pd.DataFrame()

    # para cada arquivo repetir
    for file in files:
        
        # carregando dados do arquivo para um DF
        df_geral = read_file_bib(input_file, file)
        
        print("\nArquivo {} carregado: {} linhas e {} colunas"
        .format(file, df_geral.shape[0], df_geral.shape[1] ))
        
        # criando um novo DF selecionando colunas
        new_df = select_col(df_geral, columns_aula2)
        print("Novo DF criado, dimensões: {}".format(new_df.shape))
    
        # concatendando cada novo DF no DF Final
        df_final = pd.concat([df_final, new_df])
        print("DF Final {}".format(df_final.shape))

    # gerar arquivo final no formato configurado
    gerar_arquivo(df_final, output_file, file_name_exp, export_to)
    print("\nArquivo {} exportado no formato {} e disponivel na pasta {}"
    .format(file_name_exp, export_to, output_file))