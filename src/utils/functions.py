'''
Functions - Utils
'''

# Imports
import re

from os import system as execute, popen, path, mkdir
from time import sleep as wait

from src.utils.colorFunc import colorTreatment
from src.utils.configs import *
from src.utils.languages import lang

# Vars

# Functions

# --- Program banner
def banner():
  execute('clear')
  items = [
    "{}                                                                    ".format('_RESET_'),
    "{} ██╗   ██╗███╗   ██╗██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗ {}".format('_WHITE_', '_RESET_'),
    "{} ██║   ██║████╗  ██║██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝ {}".format('_WHITE_', '_RESET_'),
    "{} ██║   ██║██╔██╗ ██║██║   ██║   ██║   ██║██║   ██║██║     ███████╗ {}".format('_BLUE_', '_RESET_'),
    "{} ██║   ██║██║╚██╗██║██║   ██║   ██║   ██║██║   ██║██║     ╚════██║ {}".format('_BLUE_', '_RESET_'),
    "{} ╚██████╔╝██║ ╚████║██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║ {}".format('_RED_', '_RESET_'),
    "{}  ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝ {}".format('_RED_', '_RESET_'),
    "{}                                                                     ".format('_RESET_')
  ]

  for item in items:
    print(colorTreatment(item))

# --- Error functions
def error(msg):
  execute('clear')
  banner()
  print(colorTreatment(msg))
  wait(1)
  execute('clear')

# --- Check lang
def checkLang():
  language = getConfigs()['language']

  if language == 'None':
    
    items = [
      '                   === {}Select Language{} ===               '.format('_CYAN_', '_RESET_'),
      '                                                             ',
      '                [{}1{}]: English                             '.format('_GREEN_', '_RESET_'),
      '                [{}2{}]: Spanish                             '.format('_GREEN_', '_RESET_'),
      '                [{}3{}]: Portuguese (BRA)                    '.format('_GREEN_', '_RESET_'),
      '                                                             ',
    ]
    banner()
    for item in items:      
      print(colorTreatment(item))

    choice = input('    Select an language\n    >>> ')

    if choice.replace(' ', '') != '':
      if choice in ['1', '01']:
        print('    The language has been changed to English.')
        setLanguage('en')
        wait(1)
      elif choice in ['2', '02']:
        print('    El idioma se cambió al Español.')
        setLanguage('es')
        wait(1)
      elif choice in ['3', '03']:
        print('    O idioma foi alterado para Português (BRA).')
        setLanguage('pt')
        wait(1)
      else:
        items = [
          '    A correct option was not selected, setting to Portuguese-Brazilian',
          '    Change this language in the settings'
        ]

        for item in items:
          print(item)
        
        setLanguage('pt')        
        wait(1)
  
  execute('clear')

def cc(msg):
  execute('clear')
  print(colorTreatment(f'_YELLOW_[_GREEN_OK_YELLOW_]_RESET_: {msg}'))
  wait(5)

# --- Update pkgs
def update():
  print('\n=====] UPDATE')
  wait(2)
  execute('apt-get update -y && apt-get upgrade -y')
  print('\n=====] UPDATED\n')

# --- Install pkgs
def install(script):
  print('\n=====] INSTALL')
  wait(2)
  execute(f'apt-get install {script} -y')
  print('\n=====] INSTALLED\n')

# --- Clone repos
def clone(author, repo, branch=False, installer=False, script=False):
  print('\n=====] CLONE')
  wait(2)

  paste = getConfigs()['folders']['tools']

  if path.isdir(paste) == False: mkdir(paste)

  if branch:
    execute(f'cd {paste} && git clone -b {branch} https://github.com/{author}/{repo}.git')
  else: 
    execute(f'cd {paste} && git clone https://github.com/{author}/{repo}.git')

  input('Debugging')

  if installer:
    if installer.lower() == 'pip':
      if script:
        execute(f'cd {repo} && pip install {script}')
      else:
        execute(f'cd {repo} && pip install -r requirements.txt')
    elif installer.lower() == 'pip3':
      if script:
        execute(f'cd {repo} && pip3 install {script} -y')
      else:
        execute(f'cd {repo} && pip3 install -r requirements.txt -y')
    elif installer.lower() == 'shell':
      if script:
        execute(script)
      else:
        execute(f'cd {repo} && chmod +x install && ./install')
    elif installer.lower() == 'py':
      if script:
        execute(f'cd {repo} && python {script}')
      else:
        execute(f'cd {repo} && chmod +x install.py && python install.py')
    elif installer.lower() == 'py3':
      if script:
        execute(f'cd {repo} && python3 {script}')
      else:
        execute(f'cd {repo} && chmod +x install.py && python3 install.py')
  print('\n=====] CLONED\n')

# --- Credits
def credit():
  items = [
    "{}╔═══════════════════{} Credit's    ".format('_RED_', '_RESET_'),
    "{}║                                {}".format('_RED_', '_RESET_'),
    ('0', 'Zian25', 'Creator', 'https://github.com/Zian25'),
    ('0', 'Ahosall', 'Modifier', 'https://github.com/Ahosall'),
    ('0', 'Elias222228', 'Translator', 'https://github.com/elias222228'),
    ('0', 'SweetDoShock', 'Tester & Modifier', 'https://github.com/SweetDoShock'),
    ('0', 'Lursy', 'Tester & Modifier', 'https://github.com/Lursy'),
    "{}╠═════════════════{} Repo Owner's  ".format('_RED_', '_RESET_'),
    "{}║                                {}".format('_RED_', '_RESET_'),
    ('1', 'Moham3dRiahi',           'Th3inspector',    'https://github.com/Moham3dRiahi/Th3inspector'),
    ('1', 'ihebski',                'angryFuzzer',     'https://github.com/ihebski/angryFuzzer'),
    ('1', 'sundowndev',             'PhoneInfoga',     'https://github.com/sundowndev/PhoneInfoga'),
    ('1', 'Official',               'FBI',             'https://github.com/Official/FBI'),
    ('1', 'm4llok',                 'Infoga',          'https://github.com/m4llok/Infoga'),
    ('1', 'S3C',                    'InfoSploit',      'https://github.com/S3C/InfoSploit'),
    ('1', 'GitHackTools',           'BillCipher',      'https://github.com/GitHackTools/BillCipher'),
    ('1', 'twelvesec',              'gasmask',         'https://github.com/twelvesec/gasmask'),
    ('1', 'Lite',                   'inmux',           'https://github.com/Lite/inmux'),
    ('1', 'twRajkumrdusadelvesec',  'Tracer',          'https://github.com/twRajkumrdusadelvesec/Tracer'),
    ('1', 'Tuhinshubhra',           'RED_HAWK',        'https://github.com/Tuhinshubhra/RED_HAWK'),
    ('1', 'TechnicalMujeeb',        'scanner',         'https://github.com/TechnicalMujeeb/scanner'),
    ('1', 'CYB3RMX',                'sqlmx_termux',    'https://github.com/CYB3RMX/sqlmx_termux'),
    ('1', 'bhavsec',                'reconspider',     'https://github.com/bhavsec/reconspider'),
    ('1', 's0md3v',                 'ReconDog',        'https://github.com/s0md3v/ReconDog'),
    ('1', 'thelinuxchoice',         'userrecon',       'https://github.com/thelinuxchoice/userrecon'),
    ('1', 'JohnLuca12',             'IPGeolocation',   'https://github.com/JohnLuca12/IPGeolocation'),
    ('1', 'joker25000',             'Framework',       'https://github.com/joker25000/Framework'),
    ('1', 'wpscanteam',             'wpscan',          'https://github.com/wpscanteam/wpscan'),
    ('1', 'laramies',               'theHarvester',    'https://github.com/laramies/theHarvester'),
    ('1', '4w4k3',                  'KnockMail',       'https://github.com/4w4k3/KnockMail'),
    ('1', 'googleinurl',            'INURLBR',         'https://github.com/googleinurl/INURLBR'),
    ('1', 'jaygreig86',             'dmitry',          'https://github.com/jaygreig86/dmitry'),
    ('1', 'HatBashBR',              'ShodanHat',       'https://github.com/HatBashBR/ShodanHat'),
    ('1', 'HatBashBR',              'Hatwitch',        'https://github.com/HatBashBR/Hatwitch'),
    ('1', 'eschultze',              'URLextractor',    'https://github.com/eschultze/URLextractor'),
    ('1', 'ultrasecurity',          'webkiller',       'https://github.com/ultrasecurity/webkiller'),
    ('1', 'ilektrojohn',            'creepy',          'https://github.com/ilektrojohn/creepy'),
    ('1', 'thewhiteh4t',            'seeker',          'https://github.com/thewhiteh4t/seeker'),
    ('1', 'CodeDotJS',              'twifo_cli',       'https://github.com/CodeDotJS/twifo_cli'),
    ('1', 'project',                'sherlock',        'https://github.com/project/sherlock'),
    ('1', 'th3unkn0n',              'osi_ig',          'https://github.com/th3unkn0n/osi_ig'),
    '{}╚══════════════{}'.format('_RED_', '_RESET_'),
  ]

  for item in items:
    if item[0] == '0':
      print(colorTreatment('{}╠══ {}[NAME]  :{} {}   '.format('_RED_', '_CYAN_', '_RESET_', item[1])))
      wait(0.02)
      print(colorTreatment('{}╠══ {}[ROLE]  :{} {}   '.format('_RED_', '_CYAN_', '_RESET_', item[2])))
      wait(0.02)
      print(colorTreatment('{}╠═ {}[GITHUB] :{} {}\n{}║{}'.format('_RED_', '_CYAN_', '_RESET_', item[3], '_RED_', '_RESET_')))
      wait(0.02)
    elif item[0] == '1':
      print(colorTreatment('{}╠══ {}[NAME]  :{} {}   '.format('_RED_', '_CYAN_', '_RESET_', item[1])))
      wait(0.02)
      print(colorTreatment('{}╠══ {}[REPO]  :{} {}   '.format('_RED_', '_CYAN_', '_RESET_', item[2])))
      wait(0.02)
      print(colorTreatment('{}╠═ {}[GITHUB] :{} {}\n{}║{}'.format('_RED_', '_CYAN_', '_RESET_', item[3], '_RED_', '_RESET_')))
      wait(0.02)
    else: 
      print(colorTreatment(item))
      wait(0.1)  
  
  input('\n  ' + lang()['pressEnter'])
  return 'restart'

# --- Check Updates
def checkUpdates():
  print('\n ', lang()['messageUpdates']['check'])
  checker = popen('git pull').read()

  if re.search('Already up to date.', checker):
    print('\n ', lang()['messageUpdates']['noUpdate'])
    wait(3)
    return 'restart'
  else:
    print('\n ', lang()['messageUpdates']['hasUpdate'])
    wait(4)
    return 'restart'