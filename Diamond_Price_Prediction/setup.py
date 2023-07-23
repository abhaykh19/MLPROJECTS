from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements= [req.replace("\n",'') for req in requirements]
        return requirements

setup(
    name='DiamondPricePrediction',
    version= '0.0.1',
    author ='AbhayK',
    author_email='abhay.kwal.19@gmail.com',
    install_required=get_requirements('requirements.txt'),
    packagegs = find_packages()
)