from setuptools import setup, find_packages

setup(
    name='common_pyservice',
    version='2023.09.11',
    url='https://github.com/i7c/common-pyservice',
    author='Constantin Michael Weisser',
    author_email='i7c@posteo.de',
    description='Common code for python microservices on AWS',
    packages=find_packages(),
    install_requires=[
        "cryptography==41.0.5",
        "boto3==1.28.74",
        "flask-cors==4.0.0",
        "flask==3.0.0",
        "pyjwt==2.8.0"
    ],
)
