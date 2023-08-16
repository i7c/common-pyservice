from setuptools import setup, find_packages

setup(
    name='common_pyservice',
    version='2023.08.15',
    url='https://github.com/michael-D-Fly/common-pyservice',
    author='Michael Weisser',
    author_email='michael@decentrafly.com',
    description='Common code for python microservices',
    packages=find_packages(),    
    install_requires=['flask==2.3.2', 'pyjwt==2.8.0'],
)