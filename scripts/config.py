#Este archivo carga la configuración desde el archivo config.yaml. Usamos el módulo yaml para leer el archivo YAML y convertirlo en un diccionario de Python.

import yaml  # Importa el módulo yaml para trabajar con archivos YAML

def load_config(config_path="../config.yaml"):  # Define una función para cargar la configuración
    with open(config_path, 'r') as file:  # Abre el archivo de configuración
        config = yaml.safe_load(file)  # Carga el contenido del archivo y lo convierte en un diccionario
    return config  # Devuelve el diccionario de configuración