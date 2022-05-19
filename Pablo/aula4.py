import requests
import pandas as pd
import psycopg2 as psg
from config.config import *
from library import *


if __name__ == "__main__":

    format = "json"
    max_records = 50
    start_record = 1
    sort_order = "asc"
    sort_field = "article_number"
   

    df_final_ieee = pd.DataFrame()
    total_records = 1

    while total_records > 0:

        api = config["api"][0]
        api += "format=json"
        api += "&apikey=" + config["apikey"][1]
        api += "&start_record=" + str(start_record)
        api += "&max_records=" + str(max_records)

        if abstract:
            api += "&abstract=" + abstract

        if title:
            api += "&article_title=" + title

        if author:
            api += "&author=" + author

        response = requests.get(api)

        if response.status_code == 200:

            dados_ieee = response.json()

            articles  = dados_ieee["articles"]
            df_articles = pd.DataFrame(articles)
            df_articles = select_col(df_articles, columns_aula4)

            df_articles = df_articles.replace("'", "", regex=True)                

            df_final_ieee = pd.concat([df_final_ieee, df_articles])

            if total_records == 1:
                total_records = dados_ieee["total_records"]

        os.system('cls')
        start_record += max_records
        total_records -= max_records
        ###
        #total_records = 0
        ###
        if total_records < 0:
            total_records = 0

        print("Total de registros faltantes: ", total_records)
        print("Total de registros minerados: ", df_final_ieee.shape[0])
        print("Total de registros encontrados: ", str(total_records + df_final_ieee.shape[0]))       

    if show_excel:
        print("Gerando planilha excel para conferencia ...")
        df_final_ieee.to_excel("output/df_final_ieee.xlsx", index = False)  

    # database
    try:
        connection = psg.connect(
        host = host,
        database = database,
        user = user,
        password = pwd)

        cursor = connection.cursor()

        for row in df_final_ieee.values:
            sql = """INSERT INTO publications (author, title, keywords, abstract, year, type_publication, doi ) 
                    VALUES("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}")""".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            #print(sql)
            #break
            #cursor.execute(sql)

            #connection.commit()

    except (Exception, psg.DatabaseError) as error:
        print(error, sql)    

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")              











    


