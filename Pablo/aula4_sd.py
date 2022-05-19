import requests
import pandas as pd
from config.config import *
from library import *


if __name__ == "__main__":

    df_final_sd = pd.DataFrame()
    total_records = 1

    while total_records > 0:

        api = config["api_sd"]["uri"]
        api += "apikey=" + config["api_sd"]["apiKey"]
        api += "&startPage=" + str(startPage)
        api += "&count=" + str(count)

        if config["api_sd"]["query"]:
            api += "&query=" + config["api_sd"]["query"]

        #if title:
         #   api += "&article_title=" + title

        #if author:
         #   api += "&author=" + author

        response = requests.get(api)

        if response.status_code == 200:

            dados_sd = response.json()

            articles  = dados_sd["search-results"]["entry"]
            df_articles = pd.DataFrame(articles)
            df_articles = select_col(df_articles, columns_aula4)
            df_articles["year"] = clean_year(df_articles["year"])
            df_final_sd = pd.concat([df_final_sd, df_articles])

            if total_records == 1:
                total_records = int(dados_sd["search-results"]["opensearch:totalResults"])

        os.system('cls')
        startPage += count
        total_records -= count


        if total_records < 0:
            total_records = 0

        print("Science Direct: " + api)
        print("Total de registros faltantes: ", total_records)
        print("Total de registros minerados: ", df_final_sd.shape[0])
        print("Total de registros encontrados: ", str(total_records + df_final_sd.shape[0]))       

    if show_excel:
        print("Gerando planilha excel para conferencia ...")
        df_final_sd.to_excel("output/df_final_sd.xlsx", index = False)  

    msg = insert_database(host, database, user, pwd, df_final_sd)

    print(msg)
