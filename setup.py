from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    """Return requirements from requirements.txt file."""
    requirements=[]
    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ML_Project',
    version='0.1.0',
    description='ML_Project',
    author='Maaz Alam',
    author_email='itsmaaz39@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)