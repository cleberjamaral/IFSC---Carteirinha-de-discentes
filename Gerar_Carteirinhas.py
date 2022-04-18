import Insersor_Carteirinha as c
import os
import pandas as pd

url_db = ('./consulta_geral_discente.csv')
df = pd.read_csv(url_db, sep=';', encoding='iso-8859-1')

def delete_files(directory,extension):
    files = os.listdir(directory)
    filtered = [file for file in files if file.endswith("." + extension)]
    for file in filtered:
        path = os.path.join(directory, file)
        os.remove(path)

def generate_cards():

    if not os.path.exists("./output"):
        os.makedirs("./output")
    os.chdir('./output')
    for student in df.index:
        card, hash = c.generate_card(df['Curso'][student],df['Nome'][student],df['Matrícula'][student])

        # Write test TEX and PDF files
        output_file = "Carteirinha_" + df['Curso'][student].replace(" ", "_") + "_" + df['Nome'][student].replace(" ", "_") + ".tex"
        with open(output_file, 'w') as f:
            f.write("".join(card))
        os.system('xelatex -synctex=1 "' + output_file + '"')

generate_cards()
delete_files("./","log")
delete_files("./","out")
delete_files("./","gz")
delete_files("./","aux")
delete_files("./","tex")
