'''
Program by Ahosall (Feh's)
based in 
'''
from random import choice

from time import sleep

from src.tools import tools
from src.languages import Lang
from src.utils import banner, color

lang = Lang('en').lang

def main():
  banner()

  tips = lang['tips']

  menu = [
    '{}  ╔═════════════{} MENU     {}'.format('_RED_', '_WHITE_', '_RESET_'),
    '{}  ║                         {}'.format('_RED_', '_RESET_'),
    '{}  ╠══════{} {}              {}'.format('_RED_', '_WHITE_', lang['main']['tools']['subtitle'], '_RESET_'),
    '{}  ║                         {}'.format('_RED_', '_RESET_'),
    '{}  ╠══{}[1]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['tools']['value'][0], '_RESET_'),
    '{}  ╠══{}[2]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['tools']['value'][1], '_RESET_'),
    '{}  ╠══{}[3]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['tools']['value'][2], '_RESET_'),
    '{}  ╠══{}[4]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['tools']['value'][3], '_RESET_'),
    '{}  ╠══{}[5]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['tools']['value'][4], '_RESET_'),
    '{}  ║                         {}'.format('_RED_', '_RESET_'),
    '{}  ╠══════{} {}              {}'.format('_RED_', '_WHITE_', lang['main']['others']['subtitle'], '_RESET_'),
    '{}  ║                         {}'.format('_RED_', '_RESET_'),
    '{}  ╠══{}[6]{}: {} {}         {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['others']['value'][0], '_YELLOW_DEV', '_RESET_'),
    '{}  ╠══{}[7]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['others']['value'][1], '_RESET_'),
    '{}  ╠══{}[8]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['others']['value'][2], '_RESET_'),
    '{}  ╠══{}[9]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['others']['value'][3], '_RESET_'),
    '{}  ╚══{}[0]{}: {}            {}'.format('_RED_', '_BLUE_', '_WHITE_', lang['main']['others']['value'][4], '_RESET_'),
    '',
    '{}  [{}{}{}]{}: {}            {}\n'.format('_CYAN_', '_GREEN_', tips['title'], '_CYAN_', '_WHITE_', choice(tips['menu']), '_RESET_'),
  ]

  for m in menu:
    print(color(m))
    sleep(0.01)
  
  entry = input('  ' + lang['input'])

  if not entry.replace(' ', '') == '' and entry.isnumeric():
    entry = int(entry)
    banner()

    if entry == 0: 
      return 'exit'
    else:
      tools(int(entry) - 1)
  else:
    return 'entry.error'

while True:
  try:
    if __name__ == '__main__':
      r = main()

      if r == 'entry.error':
        print('\n  _RED_[Err]_RESET_: ' + lang['errors']['errChoice'])
      elif r == 'exit':
        banner()
        print(' ', lang['exit'], '\n')
        break
  except KeyboardInterrupt:
    banner()
    print(' ', lang['exit'], '\n')
    break

exit(0)