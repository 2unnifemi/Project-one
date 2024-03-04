from setuptools import find_packages,setup
from typing import List

Remove_e = '-e .'
def get_requirements(file_path:str) -> List[str] :
    """ 
    This function will return a list of libraries
    """
    Requirement = []
    with open(file_path) as file_obj:
        Requirement = file_obj.readlines()
        Requirement =[req.replace("\n", "") for req in Requirement]
        #Requirement = [req for req in Requirement if req != '-e .']

        if Remove_e in Requirement:

            Requirement.remove(Remove_e)
    return Requirement




setup(
    name = "Project_1",
    version = "0.0.1",
    author = "Tunnifemi",
    author_email = "Ayodeji.oyada@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")

)