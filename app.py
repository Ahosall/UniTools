'''
Functions & Tools by Zian25
Program by Ahosall (Feh's)
'''

# Imports
import sys
import random

from time import sleep as wait

from src.utils import functions, languages, colorFunc, configs
from src.tools import infoGathering, DoS, phishing, exploit, bruteForce, panels

# Vars

# Main Function
def main():
  functions.banner()
  tips = languages.lang()['tips']
  
  items = [
    '{}  ╔═════════════{} MENU     {}'.format('_RED_', '_WHITE_', '_RESET_'),
    '{}  ║                         {}'.format('_RED_', '_RESET_'),
    '{}  ╠══════{} {}              {}'.format('_RED_', '_WHITE_', languages.lang()['mainMenu']['tools']['subtitle'], '_RESET_'),
    '{}  ║                         {}'.format('_RED_', '_RESET_'),
    '{}  ╠══{}[1]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['tools']['value'][0], '_RESET_'),
    '{}  ╠══{}[2]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['tools']['value'][1], '_RESET_'),
    '{}  ╠══{}[3]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['tools']['value'][2], '_RESET_'),
    '{}  ╠══{}[4]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['tools']['value'][3], '_RESET_'),
    '{}  ╠══{}[5]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['tools']['value'][4], '_RESET_'),
    '{}  ║                         {}'.format('_RED_', '_RESET_'),
    '{}  ╠══════{} {}              {}'.format('_RED_', '_WHITE_', languages.lang()['mainMenu']['others']['subtitle'], '_RESET_'),
    '{}  ║                         {}'.format('_RED_', '_RESET_'),
    '{}  ╠══{}[6]{}: {} {}         {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['others']['value'][0], '_YELLOW_DEV', '_RESET_'),
    '{}  ╠══{}[7]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['others']['value'][1], '_RESET_'),
    '{}  ╠══{}[8]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['others']['value'][2], '_RESET_'),
    '{}  ╠══{}[9]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['others']['value'][3], '_RESET_'),
    '{}  ╚══{}[0]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', languages.lang()['mainMenu']['others']['value'][4], '_RESET_'),
    '',
    '{}  [{}{}{}]{}: {}            {}\n'.format('_CYAN_', '_GREEN_', tips['title'], '_CYAN_', '_WHITE_', random.choice(tips['mainMenu']), '_RESET_'),
  ]

  for item in items:
    print(colorFunc.colorTreatment(item))
    wait(0.01)

  choice = input('  ' + languages.lang()['input'])

  if choice.replace(' ', '') != '' and choice.isnumeric():
    choice = int(choice)
    functions.banner()
    if choice == 0: return 'exit'
    elif choice == 1: return infoGathering.menu()
    elif choice == 2: return DoS.menu()
    elif choice == 3: return phishing.menu()
    elif choice == 4: return exploit.menu()
    elif choice == 5: return bruteForce.menu()
    elif choice == 6: return panels.menu()
    elif choice == 7: return configs.menu()
    elif choice == 8: return functions.checkUpdates()
    elif choice == 9: return functions.credit()
    else: return 'error'
  else: return 'error'

# --- Check Lang
functions.checkLang()

# Init
while True:
  try:
    if __name__ == '__main__':  
      func = main()

      if func == 'error':
        functions.error('  _RED_[Err]_RESET_: ' + languages.lang()['errors']['errChoice'])
      elif func == 'exit':
        functions.banner()
        print(' ', languages.lang()['exit'])
        sys.exit(1)
  except KeyboardInterrupt:
    functions.banner()
    print(' ', languages.lang()['exit'])
    sys.exit(1)