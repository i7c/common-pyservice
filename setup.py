from setuptools import setup, find_packages
import toml

setup(
    name='common_pyservice',
    version=toml.load("pyproject.toml")['project']['version'],
    url='https://github.com/michael-D-Fly/common-pyservice',
    author='Michael Weisser',
    author_email='michael@decentrafly.com',
    description='Common code for python microservices',
    packages=find_packages(),
    install_requires=[
        'aws-lambda-wsgi==0.0.6',
        'cryptography==41.0.7',
        'flask-cors==4.0.0',
        'flask==2.3.2',
        'pyjwt==2.8.0',
        'requests==2.31.0',
        'schema==0.7.5',
    ],
)
