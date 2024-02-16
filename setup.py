from setuptools import find_packages,setup
from typing import List

HYPEN_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this func will return the list of requirements
    :param file_path:
    :return:
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
        return requirements


setup(
    name='ml_projects2',
    version='0.0.1',
    author='Pavi',
    author_email='pavithra2832@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)
