'''
Information Gathering - Tools
'''

# Imports
import random

from time import sleep as wait

# --- Utils
from src.utils.functions import update, install, clone, cc
from src.utils.languages import lang
from src.utils.colorFunc import colorTreatment

# Tools
# 01 | Nmap
def nmap():
  update()
  install('nmap')
  cc('Nmap has been successfully installed...')
  return 'restart'

# 02 | Th3inspector
def Th3inspector():
  clone(
    author='Moham3dRiahi', 
    repo='Th3inspector',
    installer='shell',
    script='chmod +x ./install.sh && ./install.sh'
  )
  cc('Th3inspector has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 03 | angryFuzzer
def angryFuzzer():
  clone(
    author='ihebski', 
    repo='angryFuzzer',
    installer='pip3',
    script='-r requirements.txt'
  )
  cc('AngryFuzzer has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 04 | PhoneInfoga
def PhoneInfoga():
  clone(
    author='sundowndev',
    repo='PhoneInfoga',
    installer='pip'
  )
  cc('PhoneInfoga has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 05 | FBI
def FBI():
  clone(
    author='KnightSec-Official',
    repo='FBI',
    installer='pip'
  )
  install('python')
  cc('FBI has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 06 | Infoga
def Infoga():
  clone(
    author='m4llok',
    repo='Infoga',
    installer='python3',
    script='setup.py install'
  )
  cc('Infoga has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 07 | InfoSploit
def InfoSploit():
  clone(
    author='CybernetiX-S3C',
    repo='InfoSploit',
    installer='shell'
  )
  cc('Infosploit has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'
# 08 | BillCipher
def BillCipher():
  update()
  install('ruby python python-pip python3 python3-pip httrack whatweb')
  clone(
    author='GitHackTools',
    repo='BillCipher',
    installer='pip3',
    script='-r requirements.txt && pip3 -r requirements.txt'
  )
  cc('Infosploit has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 09 | gasmask
def gasmask():
  clone(
    author='twelvesec',
    repo='gasmask',
    installer='pip'
  )
  cc('Infosploit has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 10 | OSIF
def OSIF():
  clone(
    author='twelvesec',
    repo='gasmask',
    installer='pip'
  )
  cc('Infosploit has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 11 | inmux
def inmux():
  clone(
    author='Indonesia-Security-Lite',
    repo='inmux'
  )
  cc('Inmux has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 12 | IPTracer
def IPTracer():
  clone(
    author='twRajkumrdusadelvesec',
    repo='IP-Tracer',
    installer='shell'
  )
  cc('IPTracer has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 13 | RED_HAWK
def RED_HAWK():
  clone(
    author='Tuhinshubhra',
    repo='RED_HAWK'
  )
  cc('RED_HAWK has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 14 | TMscanner
def TMscanner():
  clone(
    author='TechnicalMujeeb',
    repo='TM-scanner'
  )
  cc('TMscanner has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 15 | sqlmx_termux
def sqlmx_termux():
  clone(
    author='CYB3RMX',
    repo='sqlmx_termux'
  )
  cc('Infosploit has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 16 | reconspider
def reconspider():
  clone(
    author='bhavsec',
    repo='reconspider'
  )
  cc('Reconspider has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 17 | ReconDog
def ReconDog():
  clone(
    author='s0md3v',
    repo='ReconDog'
  )
  cc('ReconDog has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 18 | userrecon
def userrecon():
  clone(
    author='thelinuxchoice',
    repo='userrecon'
  )
  cc('Userrecon has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 19 | IPGeolocation
def IPGeolocation():
  clone(
    author='JohnLuca12',
    repo='IPGeolocation'
  )
  cc('IPGeolocation has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 20 | OptivaFramework
def OptivaFramework():
  clone(
    author='joker25000',
    repo='Optiva-Framework'
  )
  cc('Infosploit has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 21 | wpscan
def wpscan():
  clone(
    author='wpscanteam',
    repo='wpscan'
  )
  cc('Infosploit has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 22 | theHarvester
def theHarvester():
  clone(
    author='laramies',
    repo='theHarvester'
  )
  cc('TheHarvester has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 23 | KnockMail
def KnockMail():
  clone(
    author='4w4k3',
    repo='KnockMail'
  )
  cc('KnockMail has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 24 | SCANNERINURLBR
def SCANNERINURLBR():
  clone(
    author='googleinurl',
    repo='SCANNER-INURLBR'
  )
  cc('ScannerInURLBr has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 25 | dmitry
def dmitry():
  clone(
    author='jaygreig86',
    repo='dmitry'
  )
  cc('Dmitry has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 26 | ShodanHat
def ShodanHat():
  clone(
    author='HatBashBR',
    repo='ShodanHat'
  )
  cc('ShodanHat has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 27 | Hatwitch
def Hatwitch():
  clone(
    author='HatBashBR',
    repo='Hatwitch'
  )
  cc('Hatwitch has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 28 | URLextractor
def URLextractor():
  clone(
    author='eschultze',
    repo='URLextractor'
  )
  cc('URLextractor has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 29 | webkiller
def webkiller():
  clone(
    author='ultrasecurity',
    repo='webkiller'
  )
  cc('Webkiller has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 30 | creepy
def creepy():
  clone(
    author='ilektrojohn',
    repo='creepy'
  )
  cc('Creepy has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# 31 | seeker
def seeker():
  clone(
    author='thewhiteh4t',
    repo='seeker',
    installer='sh',
    script='chmod 777 termux_install.sh && ./termux_install.sh'
  )
  cc('Seeker has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'
# 32 | twifo_cli
def twifo_cli():
  update()
  install('nodejs')
  clone(
    author='CodeDotJS',
    repo='twifo_cli',
    installer='npm',
    script='--global twifo-cli'
  )
  cc('Twifo_cli has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 33 | sherlock
def sherlock():
  clone(
    author='sherlock-project',
    repo='sherlock',
    installer='pip3'
  )
  cc('Sherlock has been successfully cloned and installed... To access it go to the tools folder.')
  return 'restart'

# 34 | osi_ig
def osi_ig():
  clone(
    author='th3unkn0n',
    repo='osi_ig'
  )
  cc('Osi_ig has been cloned successfully... To access it go to the tools folder.')
  return 'restart'

# Menu
def menu():
  tips = lang()['tips']
  
  tools = [
    '            ',
    '=== {}'.format(lang()['tools']['infoGathering']),
    '  {}[1]{} Nmap                 '.format('_CYAN_', '_RESET_'),
    '  {}[2]{} Th3inspector         '.format('_CYAN_', '_RESET_'),
    '  {}[3]{} angryFuzzer          '.format('_CYAN_', '_RESET_'),
    '  {}[4]{} PhoneInfoga          '.format('_CYAN_', '_RESET_'),
    '  {}[5]{} FBI                  '.format('_CYAN_', '_RESET_'),
    '  {}[6]{} Infoga - Email OSINT '.format('_CYAN_', '_RESET_'),
    '  {}[7]{} InfoSploit           '.format('_CYAN_', '_RESET_'),
    '  {}[8]{} BillCipher           '.format('_CYAN_', '_RESET_'),
    '  {}[9]{} gasmask              '.format('_CYAN_', '_RESET_'),
    '  {}[10]{} OSIF                '.format('_CYAN_', '_RESET_'),
    '  {}[11]{} inmux               '.format('_CYAN_', '_RESET_'),
    '  {}[12]{} IP-Tracer           '.format('_CYAN_', '_RESET_'),
    '  {}[13]{} RED_HAWK            '.format('_CYAN_', '_RESET_'),
    '  {}[14]{} TM-scanner          '.format('_CYAN_', '_RESET_'),
    '  {}[15]{} sqlmx_termux        '.format('_CYAN_', '_RESET_'),
    '  {}[16]{} reconspider         '.format('_CYAN_', '_RESET_'),
    '  {}[17]{} ReconDog            '.format('_CYAN_', '_RESET_'),
    '  {}[18]{} userrecon           '.format('_CYAN_', '_RESET_'),
    '  {}[19]{} IPGeolocation       '.format('_CYAN_', '_RESET_'),
    '  {}[20]{} Optiva-Framework    '.format('_CYAN_', '_RESET_'),
    '  {}[21]{} wpscan              '.format('_CYAN_', '_RESET_'),
    '  {}[22]{} theHarvester        '.format('_CYAN_', '_RESET_'),
    '  {}[23]{} KnockMail           '.format('_CYAN_', '_RESET_'),
    '  {}[24]{} dmitry              '.format('_CYAN_', '_RESET_'),
    '  {}[25]{} ShodanHat           '.format('_CYAN_', '_RESET_'),
    '  {}[26]{} Hatwitch            '.format('_CYAN_', '_RESET_'),
    '  {}[27]{} URLextractor        '.format('_CYAN_', '_RESET_'),
    '  {}[28]{} webkiller           '.format('_CYAN_', '_RESET_'),
    '  {}[29]{} creepy              '.format('_CYAN_', '_RESET_'),
    '  {}[30]{} Seeker              '.format('_CYAN_', '_RESET_'),
    '  {}[31]{} Twifo-cli           '.format('_CYAN_', '_RESET_'),
    '  {}[32]{} Sherlock            '.format('_CYAN_', '_RESET_'),
    '  {}[33]{} osi.ig              '.format('_CYAN_', '_RESET_'),
    '  {}[00]{} {}                  '.format('_CYAN_', '_RESET_', lang()['goBack']),
    '                               ',
    '  {}[{}{}{}]{}: {}         {}\n'.format('_CYAN_', '_GREEN_', tips['title'], '_CYAN_', '_WHITE_', random.choice(tips['DoS']), '_RESET_'),
  ]

  for tool in tools:
    print(colorTreatment(tool))
    wait(0.01)

  choice = input('  ' + lang()['input'])

  if choice.replace(' ', '') != '':
    if choice in ['0', '00']:   return 'restart'
    elif choice in ["1", "01"]: return nmap()
    elif choice in ["2", "02"]: return Th3inspector()
    elif choice in ["3", "03"]: return angryFuzzer()
    elif choice in ["4", "04"]: return PhoneInfoga()    
    elif choice in ["5", "05"]: return FBI()    
    elif choice in ["6", "06"]: return Infoga()
    elif choice in ["7", "07"]: return InfoSploit()
    elif choice in ["8", "08"]: return BillCipher()
    elif choice in ["9", "09"]: return gasmask()
    elif choice in "10": return OSIF()
    elif choice in "11": return inmux()
    elif choice in "12": return IPTracer()
    elif choice in "13": return RED_HAWK()
    elif choice in "14": return TMscanner()
    elif choice in "15": return sqlmx_termux()
    elif choice in "16": return reconspider()
    elif choice in "17": return ReconDog()
    elif choice in "18": return userrecon()
    elif choice in "19": return IPGeolocation()
    elif choice in "20": return OptivaFramework()
    elif choice in "21": return wpscan()
    elif choice in "22": return theHarvester()
    elif choice in "23": return KnockMail()
    elif choice in "24": return dmitry()
    elif choice in "25": return ShodanHat()
    elif choice in "26": return Hatwitch()
    elif choice in "27": return URLextractor()
    elif choice in "28": return webkiller()
    elif choice in "29": return creepy()
    elif choice in "30": return seeker()
    elif choice in "31": return twifo_cli()
    elif choice in "32": return sherlock()
    elif choice in "33": return osi_ig()
    else: return 'error'
  else: return 'error'
  