# By Ahosall!!
from platform import system
from os import system as execute, popen

def clear():
  execute('cls' if system().lower().startswith('win') else 'clear')

# Color Treatment
def color(string: str):
  string = string.replace('_RESET_', '\033[00m')
  string = string.replace('_BOLD_', '\033[01m')
  string = string.replace('_UNDERLINE_', '\033[04m')
  string = string.replace('_FLASHING_', '\033[05m')
  string = string.replace('_REVERSE_', '\033[07m')
  string = string.replace('_HIDDEN_', '\033[08m')
  
  string = string.replace('_BLACK_', '\033[30m')
  string = string.replace('_RED_', '\033[31m')
  string = string.replace('_GREEN_', '\033[32m')
  string = string.replace('_YELLOW_', '\033[33m')
  string = string.replace('_BLUE_', '\033[34m')
  string = string.replace('_MAGENTA_', '\033[35m')
  string = string.replace('_CYAN_', '\033[36m')
  string = string.replace('_WHITE_', '\033[37m')

  return string

# Banner UNITOOLS
def banner():
  clear()

  items = [
    "{}                                                                     ".format('_RESET_'),
    "{} ██╗   ██╗███╗   ██╗██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗ {}".format('_WHITE_', '_RESET_'),
    "{} ██║   ██║████╗  ██║██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝ {}".format('_WHITE_', '_RESET_'),
    "{} ██║   ██║██╔██╗ ██║██║   ██║   ██║   ██║██║   ██║██║     ███████╗ {}".format('_BLUE_', '_RESET_'),
    "{} ██║   ██║██║╚██╗██║██║   ██║   ██║   ██║██║   ██║██║     ╚════██║ {}".format('_BLUE_', '_RESET_'),
    "{} ╚██████╔╝██║ ╚████║██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║ {}".format('_RED_', '_RESET_'),
    "{}  ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ {}".format('_RED_', '_RESET_'),
    "{}                                                          {}       {}".format('_YELLOW_', 'v2023.08', '_RESET_')
  ]

  for i in items:
    print(color(i))

# Clone
def clone(author: str, repo: str):
  log = (f'cd .. && git clone https://github.com/{author}/{repo}.git && cd -')
  print('cmd =>', log)
  if not 'fatal' in log.lower():
    return True
  else:
    return False

def install(program: str):
  log = (f'sudo apt install {program} -y')

# Setup
def setup(tool: list):
  '''
  tool:
    - 0: type
    - 1: name
    - 2: author
    - 3: respository
    - 4: installer
    - 5: script
  '''
  banner()
  print('==' * 5, f'Setup for {tool[1]}...')
  
  print(tool)
  # Milenar logics
  if not tool[3] == '':
    # Is github repository, clone!
    r = clone(author=tool[2], repo=tool[3])
  elif tool[3] == '':
    r = install(program=tool[1])
  input()

  return 'restart'

  # 0;twifo-cli;CodeDotJS;twifo-cli;npm;--global