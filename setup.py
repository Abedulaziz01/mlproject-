from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:  
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n", "") for req in requirements]



        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='ml',
    version='0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='user',
    author_email='user@example.com',
    description='A small example package',
    install_requires=get_requirements('requirements.txt')
)
