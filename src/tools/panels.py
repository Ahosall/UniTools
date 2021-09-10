'''
Panels - Tools
'''

# Imports
from time import sleep as wait

# -- Utils
from src.utils.colorFunc import colorTreatment

# Vars

# Menu
def menu():
  print(colorTreatment('  {}Coming Soon~{}'.format('_GREEN_', '_RESET_')))
  wait(2)
  return 'restart'
