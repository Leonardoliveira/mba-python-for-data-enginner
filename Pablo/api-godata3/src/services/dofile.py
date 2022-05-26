import pandas as pd
import numpy as np
import bibtexparser


class Dofile():

    def read_file_bib(self, file):
        with open(f"input/{file}", encoding = "utf_8") as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
            df = pd.DataFrame(bib_database.entries)
        return df

    def select_col(self, df_geral):
        columns_out = {
            'author':['author'],
            'title':['title'],
            'keywords':['keywords'],
            'abstract':['abstract'],
            'year': ['year'],
            'type_publication': ['type_publication', 'ENTRYTYPE'],
            'doi': ['doi']
        }

        new_df = pd.DataFrame()
        for value in columns_out.values():
            for col in value:
                if col in df_geral.columns:
                    new_df[value[0]] = df_geral[col]
                    break
                else:
                    if col == value[-1]:
                        new_df[value[0]] = np.nan
        return new_df

    
    def get_file(self, df_final, file_name, ext):

        arquivo_saida = f"output/{file_name}.{ext}"

        if ext == "json":
            dados_arquivo = df_final.to_json(orient = 'split')

        elif ext == "csv":
            df_final.to_csv(arquivo_saida, sep = ";", header = True, index=False)

        return dados_arquivo
