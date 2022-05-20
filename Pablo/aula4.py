import requests
import pandas as pd
from config.config import *
from library import *


if __name__ == "__main__":

    df_final_ieee = pd.DataFrame()
    total_records = 1

    while total_records > 0:

        api = config["api_ieee"]["uri"]
        api += "format=json"
        api += "&apikey=" + config["api_ieee"]["apikey"]
        api += "&start_record=" + str(start_record)
        api += "&max_records=" + str(max_records)

        if config["api_ieee"]["abstract"]:
            api += "&abstract=" + config["api_ieee"]["abstract"]

        if config["api_ieee"]["article_title"]:
            api += "&article_title=" + config["api_ieee"]["article_title"]

        if config["api_ieee"]["author"]:
            api += "&author=" + config["api_ieee"]["author"]

        response = requests.get(api)

        if response.status_code == 200:

            dados_ieee = response.json()

            articles  = dados_ieee["articles"]
            df_articles = pd.DataFrame(articles)
            df_articles = select_col(df_articles, columns_aula4)
            df_articles["author"] = explode_authors(df_articles["author"])  
            df_articles["keywords"] = explode_keywords(df_articles["keywords"])                        
            df_articles = df_articles.replace("'", "", regex=True)                
                     

            df_final_ieee = pd.concat([df_final_ieee, df_articles])

            if total_records == 1:
                total_records = dados_ieee["total_records"]

        os.system('cls')
        start_record += max_records
        total_records -= max_records

        if total_records < 0:
            total_records = 0

        print("Total de registros faltantes: ", total_records)
        print("Total de registros minerados: ", df_final_ieee.shape[0])
        print("Total de registros encontrados: ", str(total_records + df_final_ieee.shape[0]))       

    if show_excel:
        print("Gerando planilha excel para conferencia ...")
        df_final_ieee.to_excel("output/df_final_ieee.xlsx", index = False)  

    msg = insert_database(host, database, user, pwd, df_final_ieee)

    print(msg)
    
                











    


