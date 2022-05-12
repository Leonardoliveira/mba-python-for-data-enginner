from library import get_config
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
