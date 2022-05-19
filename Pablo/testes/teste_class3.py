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
    title_default = config["columns_aula3"]["title"][0]
    title_jcs = config["column_title"]["jcs"]
    title_scm = config["column_title"]["scm"]


