import Carteirinha_Insersor as c
import os

# CONFIGURAÇÕES:
students = [
    "ADRIAN RAFAEL LIMA MEDEIROS",
    "ARTHUR SILVA ESTACIO",
    "ELIZA DOS SANTOS GONÇALVES",
    "ERIKA EUFRASIO",
    "FRANCISCO DE ASSIS FLORIANO CORREA JUNIOR"
    ]

def delete_files(extension):
    directory = "./"
    files = os.listdir(directory)
    filtered = [file for file in files if file.endswith("." + extension)]
    for file in filtered:
        path = os.path.join(directory, file)
        os.remove(path)

def generate_cards():

    for student in students:
        card, hash = c.generate_card(student,"123.456.789-01")

        # Write test TEX and PDF files
        output_file = "Carteirinha_" + student + "_" + hash + ".tex"
        with open(output_file, 'w') as f:
            f.write("".join(card))
        os.system('xelatex -synctex=1 "' + output_file + '"')

generate_cards()
delete_files("log")
delete_files("out")
delete_files("gz")
delete_files("aux")
delete_files("csv")
