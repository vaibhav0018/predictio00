from setuptools import setup, find_packages
from typing import List


PROJECT_NAME = "Machine Learning Project"
VERSION ="0.0.1"
DESCRIPTION = "this is ml project in modular coding"
AUTHOR_NAME = "Vaibhav Patil"
AUTHOR_EMAIL = "patilvaibhva0018@gmail.com"


REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_E_DOT = "-e ."
#requriments.txt file open
#read
#
def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "")for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list




setup(
    name=PROJECT_NAME,
    description=DESCRIPTION,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requres = get_requirements_list

)