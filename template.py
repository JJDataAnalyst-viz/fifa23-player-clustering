import os
from pathlib import Path
from typing import List
from logs import logger, setup_logging

setup_logging()

# Set project name
project_name = "Fifa23"


# Set template for data_science project (alternative way - cookiecutter)
template = [
    ".gitignore",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "research/research.ipynb",
    "templates/index.html",
    "app.py",
    "requirements.txt",
    "logs.py",
    ".flaskenv",
    ".dockerignore",
]


def make_files(template: List) -> None:
    """
    Create directories and files as a template for data sience project

    Args:
        template (List) : list of path for creating dirs and files
    """

    logger.info("Loading files from template..")
    for filepath in template:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logger.info(f"Created dir : {filedir}")
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            try:
                with open(os.path.join(filedir, filename), "w",encoding="utf-8") as file:
                    pass
                logger.info(f"Created file : {file}")
            except Exception as e:
                print(e)
        else:

            print(f"{filepath} already exists!")


if __name__ == "__main__":
    make_files(template)
