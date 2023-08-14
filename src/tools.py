# By Feh's (Ahosall)

from src.utils import color, setup
from src.languages import Lang
from src.database import tools as dbTools

lang = Lang('en').lang

def tools(tType:int):
  fTools = dbTools(tType)

  menu = [
    '==== {}           '.format(list(lang['tools'].values())[tType]),
  ]

  count = 1
  for t in fTools:
    menu.append('  {}[{}]{} {}   {}'.format('_CYAN_', str(count if count > 9 else f'0{count}'), '_WHITE_', t[1], '_RESET_')) 
    count += 1

  menu.append('  {}[00]{} {} \n'.format('_CYAN_', '_RESET_', lang['go.back']),)
  
  for m in menu:
    print(color(m))

  entry = input('  ' + lang['input'])
  if not entry.replace(' ', '') == '' and entry.isnumeric():
    entry = int(entry)
    
    if entry == 0: 
      return 'restart'
    else:
      return setup(fTools[int(entry)-1])
  else:
    return 'entry.error'
  