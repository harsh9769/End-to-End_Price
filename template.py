import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s')

project_name="house_reg"    

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    "reseacrh/trail.ipynb",
    "templates/index.html",
    "dvc.yaml",
    "config/config.yaml",
    "params.yaml"

]

for dir in list_of_files:
    dir=Path(dir)
    dir_name,file_name=os.path.split(dir)
    if dir_name!="":
        os.makedirs(dir_name,exist_ok=True)
        logging.info(f"Creating Directory: {dir_name}")

    if (not os.path.exists(dir)) or (os.path.getsize(dir)==0):
        with open(dir,"w") as f:
            pass
            logging.info(f"Creating file:{dir}")

    else:
        logging.info(f"{dir} already exists")

