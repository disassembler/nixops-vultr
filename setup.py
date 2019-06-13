import sys
import subprocess

from distutils.core import setup, Command


setup(name='nixops-vultr',
      version='@version@',
      description='NixOS cloud deployment tool, but for Vultr',
      url='https://github.com/disassembler/nixops-vultr',
      author='Samuel Leathers',
      author_email='disasm@gmail.com',
      packages=[ 'nixopsvultr', 'nixopsvultr.backends'],
      entry_points={'nixops': ['vultr = nixopsvultr.plugin']},
      py_modules=['plugin']
)
