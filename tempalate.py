import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep", #for automatically deploy files gitkeep createdjust to maek folder non empty
    f"src/{project_name}/__init__.py",  # need to create for local installing packages __init__.py ia constructor
    f"src/{project_name}/components/__init__.py", # same as above
    f"src/{project_name}/utils/common.py", # same as above
    f"src/{project_name}/logging/__init__.py", # same as above
    f"src/{project_name}/config/__init__.py", # same as above
    f"src/{project_name}/config/configuration.py", # same as above
    f"src/{project_name}/pipeline/__init__.py", # same as above
    f"src/{project_name}/entity/__init__.py", # same as above
    f"src/{project_name}/constants/__init__.py", # same as above
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.pynb"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)   ## exist ok won't create if already exists
        logging.info(f"creating directory: {filedir} for file: {filename}")


    if(not os.path.exists(filepath) or os.path.getsize(filepath)==0):
         with open(filepath,'w') as f:
             pass
         logging.info(f"creating empty file: {filename} on {filepath}")

    else:
        logging.info(f"file already exists: {filename}")