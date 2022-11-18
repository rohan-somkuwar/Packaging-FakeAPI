from setuptools import setup
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(name = "fakedata",
version = 0.2,
description = "This code is fetching data through the fakedata api",
author = "Rohan",
author_email = "rohansomkuwar97@gmail.com",
packages = ['fake'],
install_requires = [requirements],
python_requires = ">=3.7",

)