import sys
from setuptools import setup, find_packages


with open('requirements.txt') as f:
    deps = [dep for dep in f.read().split('\n') if dep.strip() != ''
            and not dep.startswith('-e')]
    install_requires = deps


setup(name='myservice',
      version="0.1",
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=install_requires)
