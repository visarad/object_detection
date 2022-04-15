from setuptools import setup, find_packages

with open('README.md','r',encoding='utf-8') as file:
    long_desc = file.read()


setup(
    name = "src",
    version = "0.0.1",
    author= "visarad",
    description="A small package for dvc-ml pipeline",
    long_description=long_desc,
    long_description_content_type = "text/markedown",
    url= "https://github.com/visarad/object-detection",
    author_email="visarad@gmail.com",
    packages=['src'],
    python_requires = ">=3.7",
    install_requires = ['dvc','pandas','scikit-learn']
)

