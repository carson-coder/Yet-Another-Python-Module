from distutils.core import setup
import json
data = json.load(open('./YAPM/config.json'))
setup(
  name='YetAnotherModule',
  version=f"{data['version']}",
  description='Yet Another Python Module.',
  author="Carson",
  author_email="carsondpool@gmail.com",
  url='https://github.com/carson-coder/Yet-Another-Python-Module',
  license="LICENSE",
  long_description=open('README.md').read(),
  packages=['YAPM'],
  py_modules=[]
)
