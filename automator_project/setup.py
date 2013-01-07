from setuptools import setup, find_packages
import os    
def read(fname):
  return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
  name='hal_automator',
  version = "1.0",
  author="Halicea.Co",
  author_email="costa@halicea.com",
  include_package_data=True, 
  package_dir={"":"src"},
  packages= find_packages('src'),
  scripts=["src/hal_automator.py"],
  long_description = read("README.rst")
)
