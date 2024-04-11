from setuptools import setup, find_packages

setup(
    name='common_pyservice',
    version='2024.4.11.0',
    url='https://github.com/i7c/common-pyservice',
    author='Constantin Michael Weisser',
    author_email='cmw@weisser-se.com',
    description='Common code for python microservices based on Flask',
    packages=find_packages(),
    install_requires=[
        'aws-lambda-wsgi==0.0.6',
        'cryptography==42.0.2',
        'flask-cors==4.0.0',
        'flask==3.0.1',
        'json-logging==1.3.0',
        'pyjwt==2.8.0',
        'requests==2.31.0',
        'schema==0.7.5',
    ],
)
