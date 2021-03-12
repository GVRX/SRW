import os
from  setuptools import setup, find_packages
from setuptools import setup
import site;


setup(name='srw',
      packages=['srw'],
      package_data = {
            'static': ['env/work/srw_python/*','*.so']}
     )

# I am sure that there is a better way to do this with independence from c make process:
os.symlink('/opt/SRW/env/work/srw_python/srwlpy.so', os.path.join(site.getsitepackages()[0],'srwlpy.so'))