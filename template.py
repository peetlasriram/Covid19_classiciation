from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s:%(message)s')


project="Classification"

list_files=[
    "github/workflow/gitkeep",
    f"src/{project}/__init__.py",
    f"src/{project}/config/configration.py",
    f"src/{project}/Constants/__init__.py",
    f"src/{project}/componennts/__init__.py",
    f"src/{project}/utils/__init__.py",
    f"src/{project}/Exception/__init__.py",
    f"src/{project}/pipelines/__init__.py",
    f"src/{project}/entity/__init__.py",
    "config/Config.yaml",
    "params.yaml",
    "dvc.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requiremets.txt",
    "setup.py",
    "research/trail.ipynb",
    "template/index.html"
    
]

for file_path in list_files:
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)
    
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir}and file_name: {file_name}")
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
        logging.info(f"Checking directory: {file_path} ")
    else:
        logging.info(f"already exists{file_name}")