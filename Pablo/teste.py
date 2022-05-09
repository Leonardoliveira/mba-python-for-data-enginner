import yaml
import pandas as pd


with open('config/config.yaml', 'r') as config:
    file_yaml = yaml.safe_load(config)
    
input_file = file_yaml["directors"]["input_file"]
output_file = file_yaml["directors"]["output_file"]
export_to = file_yaml["export_to"]
columns_aula2 = file_yaml["columns_aula2"]







    

  