Trazer as funçoes e transformar em classe

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
    write_file(df_final, output_file, file_name_exp, export_to)