import os
import sys
import shutil
import uuid
import tkinter as tk
from tkinter import filedialog

def select_solution_folder():
    print("---> Selecciona la ubicación de tu solución <---")
    path:str = filedialog.askdirectory()
    if path:
        print(f" {path}")
        return path
    else:
        sys.exit()

def select_project_name(path:str):
    print(f"---> Se creará un proyecto para la solución {path} <---")
    print("Cuando hayas acabado de introducir proyectos presiona q o Q para salir.")
    list_of_names:list = []
    aux:int = 1
    i:int = 1
    try:
        while aux == 1:
            name:str = input(f"{i}.- Escribe un nombre para tu proyecto: ")
            if name == "q" or name == "Q":
                aux = 0
                list_of_names = [*set(list_of_names)] # Remove duplicates
                return sorted(list_of_names) # Return sorted
            if name:
                i += 1
                list_of_names.append(name)
    except Exception as e:
        print("¡Asegúrate de que el valor introducido es correcto!")
        print(e)

def create_project(list_of_names:list, path:str):
    if list_of_names:
        print(f"\n---> Proyectos a crear: {list_of_names} <---")
        try:
            for name in list_of_names:
                shutil.copytree("../templates/", f"{path}/{name}")
                os.rename(f"{path}/{name}/example.csproj", f"{path}/{name}/{name}.csproj")
                with open(f'{path}/{os.path.basename(path)}.sln', 'a') as f:
                    txt:str = f"""
Project("{{{str(uuid.uuid1()).upper()}}}") = "{name}", "{name}\{name}.csproj", "{{{str(uuid.uuid1()).upper()}}}"
EndProject
                    """
                    f.write(txt)
        except Exception as e:
            print("Ha habido un error al crear el proyecto.")
            print(e)
    else:
        print("No se ha creado ningún proyecto.")
        sys.exit()

path:str = select_solution_folder()
list_of_names:list = select_project_name(path)
create_project(list_of_names, path)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
