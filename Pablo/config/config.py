from library import get_config

# carrega parametros
config = get_config() 

# directors
input_file = config["directors"]["input_file"]
output_file = config["directors"]["output_file"]

# columns
title_jcs = config["column_title"]["jcs"]
title_scm = config["column_title"]["scm"]
title_default = config["columns_aula3"]["title"][0]
columns_aula3 = config["columns_aula3"]
columns_aula2 = config["columns_aula2"]
columns_aula4 = config["columns_aula4"]

# files
file_class_2 = config["export_aula2"]["name"] + "." + config["export_aula2"]["ext"]
file_class_3 = config["export_aula3"]["name"]

# querys
find_title = config["find"]["title"]
find_keywords = config["find"]["keywords"]
find_abstract = config["find"]["abstract"]
find_year = config["find"]["year"]
find_type_publication = config["find"]["type_publication"]
find_doi = config["find"]["doi"]
find_jcr_value = config["find"]["jcr_value"]
find_scimago_value = config["find"]["scimago_value"]

# export file
export_to = config["export_aula3"]["ext"]
show_excel = config["show_excel"]

# api = config["api"]["ieee"] + "abstract=" + config["abstract"] + "&apikey=" + config["apikey"]["ieee"]
# api = config["api"][0]
 #"abstract=" + config["abstract"]
# "&apikey=" + config["apikey"][0]

#API IEEE
format = "json"
max_records = 50
start_record = 1
sort_order = "asc"
sort_field = "article_number"

# database:
host = config["srv_database"]["srv_host"]
database = config["srv_database"]["database"]
user = config["srv_database"]["user"]
pwd = config["srv_database"]["password"]

#Api SD
count = 50
startPage = 1

  



