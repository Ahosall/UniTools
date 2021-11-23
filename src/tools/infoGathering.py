'''
Information Gathering - Tools
'''

# Imports
import random

from time import sleep as wait

# --- Utils
from src.utils.configs import getSttsTool
from src.utils.functions import update, install, clone, cc
from src.utils.languages import lang
from src.utils.colorFunc import colorTreatment

# Tools
# 01 | Nmap
def nmap():
  update()
  install('nmap')
  cc(('infoGathering', 'nmap'), 'Nmap has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 02 | Th3inspector
def Th3inspector():
  clone(
    author='Moham3dRiahi', 
    repo='Th3inspector',
    installer='shell',
    script='chmod +x ./install.sh && ./install.sh'
  )
  cc(('infoGathering', 'Th3inspector'), 'Th3inspector has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 03 | angryFuzzer
def angryFuzzer():
  clone(
    author='ihebski', 
    repo='angryFuzzer',
    installer='pip3',
    script='-r requirements.txt'
  )
  cc(('infoGathering', 'angryFuzzer'), 'AngryFuzzer has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 04 | PhoneInfoga
def PhoneInfoga():
  clone(
    author='sundowndev',
    repo='PhoneInfoga',
    installer='pip'
  )
  cc(('infoGathering', 'PhoneInfoga'), 'PhoneInfoga has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 05 | FBI
def FBI():
  clone(
    author='KnightSec-Official',
    repo='FBI',
    installer='pip'
  )
  install('python')
  cc(('infoGathering', 'FBI'), 'FBI has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 06 | Infoga
def Infoga():
  clone(
    author='m4llok',
    repo='Infoga',
    installer='python3',
    script='setup.py install'
  )
  cc(('infoGathering', 'Infoga'), 'Infoga has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 07 | InfoSploit
def InfoSploit():
  clone(
    author='CybernetiX-S3C',
    repo='InfoSploit',
    installer='shell'
  )
  cc(('infoGathering', 'InfoSploit'), 'Infosploit has been successfully cloned or installed... To access it go to the tools folder.')
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
  cc(('infoGathering', 'BillCipher'), 'Infosploit has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 09 | gasmask
def gasmask():
  clone(
    author='twelvesec',
    repo='gasmask',
    installer='pip'
  )
  cc(('infoGathering', 'gasmask'), 'Infosploit has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 10 | OSIF
def OSIF():
  clone(
    author='twelvesec',
    repo='gasmask',
    installer='pip'
  )
  cc(('infoGathering', 'OSIF'), 'Infosploit has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 11 | inmux
def inmux():
  clone(
    author='Indonesia-Security-Lite',
    repo='inmux'
  )
  cc(('infoGathering', 'inmux'), 'Inmux has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 12 | IPTracer
def IPTracer():
  clone(
    author='twRajkumrdusadelvesec',
    repo='IP-Tracer',
    installer='shell'
  )
  cc(('infoGathering', 'IPTracer'), 'IPTracer has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 13 | RED_HAWK
def RED_HAWK():
  clone(
    author='Tuhinshubhra',
    repo='RED_HAWK'
  )
  cc(('infoGathering', 'RED_HAWK'), 'RED_HAWK has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 14 | TMscanner
def TMscanner():
  clone(
    author='TechnicalMujeeb',
    repo='TM-scanner'
  )
  cc(('infoGathering', 'TMscanner'), 'TMscanner has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 15 | sqlmx_termux
def sqlmx_termux():
  clone(
    author='CYB3RMX',
    repo='sqlmx_termux'
  )
  cc(('infoGathering', 'sqlmx_termux'), 'Infosploit has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 16 | reconspider
def reconspider():
  clone(
    author='bhavsec',
    repo='reconspider'
  )
  cc(('infoGathering', 'reconspider'), 'Reconspider has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 17 | ReconDog
def ReconDog():
  clone(
    author='s0md3v',
    repo='ReconDog'
  )
  cc(('infoGathering', 'ReconDog'), 'ReconDog has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 18 | userrecon
def userrecon():
  clone(
    author='thelinuxchoice',
    repo='userrecon'
  )
  cc(('infoGathering', 'userrecon'), 'Userrecon has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 19 | IPGeolocation
def IPGeolocation():
  clone(
    author='JohnLuca12',
    repo='IPGeolocation'
  )
  cc(('infoGathering', 'IPGeolocation'), 'IPGeolocation has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 20 | OptivaFramework
def OptivaFramework():
  clone(
    author='joker25000',
    repo='Optiva-Framework'
  )
  cc(('infoGathering', 'OptivaFramework'), 'Infosploit has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 21 | wpscan
def wpscan():
  clone(
    author='wpscanteam',
    repo='wpscan'
  )
  cc(('infoGathering', 'wpscan'), 'Infosploit has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 22 | theHarvester
def theHarvester():
  clone(
    author='laramies',
    repo='theHarvester'
  )
  cc(('infoGathering', 'theHarvester'), 'TheHarvester has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 23 | KnockMail
def KnockMail():
  clone(
    author='4w4k3',
    repo='KnockMail'
  )
  cc(('infoGathering', 'KnockMail'), 'KnockMail has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 24 | SCANNERINURLBR
def SCANNERINURLBR():
  clone(
    author='googleinurl',
    repo='SCANNER-INURLBR'
  )
  cc(('infoGathering', 'SCANNERINURLBR'), 'ScannerInURLBr has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 25 | dmitry
def dmitry():
  clone(
    author='jaygreig86',
    repo='dmitry'
  )
  cc(('infoGathering', 'dmitry'), 'Dmitry has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 26 | ShodanHat
def ShodanHat():
  clone(
    author='HatBashBR',
    repo='ShodanHat'
  )
  cc(('infoGathering', 'ShodanHat'), 'ShodanHat has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 27 | Hatwitch
def Hatwitch():
  clone(
    author='HatBashBR',
    repo='Hatwitch'
  )
  cc(('infoGathering', 'Hatwitch'), 'Hatwitch has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 28 | URLextractor
def URLextractor():
  clone(
    author='eschultze',
    repo='URLextractor'
  )
  cc(('infoGathering', 'URLextractor'), 'URLextractor has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 29 | webkiller
def webkiller():
  clone(
    author='ultrasecurity',
    repo='webkiller'
  )
  cc(('infoGathering', 'webkiller'), 'Webkiller has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 30 | creepy
def creepy():
  clone(
    author='ilektrojohn',
    repo='creepy'
  )
  cc(('infoGathering', 'creepy'), 'Creepy has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 31 | seeker
def seeker():
  clone(
    author='thewhiteh4t',
    repo='seeker',
    installer='sh',
    script='chmod 777 termux_install.sh && ./termux_install.sh'
  )
  cc(('infoGathering', 'seeker'), 'Seeker has been successfully cloned or installed... To access it go to the tools folder.')
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
  cc(('infoGathering', 'twifo_cli'), 'Twifo_cli has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 33 | sherlock
def sherlock():
  clone(
    author='sherlock-project',
    repo='sherlock',
    installer='pip3'
  )
  cc(('infoGathering', 'sherlock'), 'Sherlock has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# 34 | osi_ig
def osi_ig():
  clone(
    author='th3unkn0n',
    repo='osi_ig'
  )
  cc(('infoGathering', 'osi_ig'), 'Osi_ig has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'

# Menu
def menu():
  stts = getSttsTool()['infoGathering']
  tips = lang()['tips']
  
  tools = [
    '            ',
    '=== {}'.format(lang()['tools']['infoGathering']),
    '  {}[01]{} Nmap                 {}'.format('_CYAN_', stts['nmap']['Status'], '_RESET_'),
    '  {}[02]{} Th3inspector         {}'.format('_CYAN_', stts['Th3inspector']['Status'], '_RESET_'),
    '  {}[03]{} angryFuzzer          {}'.format('_CYAN_', stts['angryFuzzer']['Status'], '_RESET_'),
    '  {}[04]{} PhoneInfoga          {}'.format('_CYAN_', stts['PhoneInfoga']['Status'], '_RESET_'),
    '  {}[05]{} FBI                  {}'.format('_CYAN_', stts['FBI']['Status'], '_RESET_'),
    '  {}[06]{} Infoga - Email OSINT {}'.format('_CYAN_', stts['Infoga']['Status'], '_RESET_'),
    '  {}[07]{} InfoSploit           {}'.format('_CYAN_', stts['InfoSploit']['Status'], '_RESET_'),
    '  {}[08]{} BillCipher           {}'.format('_CYAN_', stts['BillCipher']['Status'], '_RESET_'),
    '  {}[09]{} gasmask              {}'.format('_CYAN_', stts['gasmask']['Status'], '_RESET_'),
    '  {}[10]{} OSIF                 {}'.format('_CYAN_', stts['OSIF']['Status'], '_RESET_'),
    '  {}[11]{} inmux                {}'.format('_CYAN_', stts['inmux']['Status'], '_RESET_'),
    '  {}[12]{} IP-Tracer            {}'.format('_CYAN_', stts['IPTracer']['Status'], '_RESET_'),
    '  {}[13]{} RED_HAWK             {}'.format('_CYAN_', stts['RED_HAWK']['Status'], '_RESET_'),
    '  {}[14]{} TM-scanner           {}'.format('_CYAN_', stts['TMscanner']['Status'], '_RESET_'),
    '  {}[15]{} sqlmx_termux         {}'.format('_CYAN_', stts['sqlmx_termux']['Status'], '_RESET_'),
    '  {}[16]{} reconspider          {}'.format('_CYAN_', stts['reconspider']['Status'], '_RESET_'),
    '  {}[17]{} ReconDog             {}'.format('_CYAN_', stts['ReconDog']['Status'], '_RESET_'),
    '  {}[18]{} userrecon            {}'.format('_CYAN_', stts['userrecon']['Status'], '_RESET_'),
    '  {}[19]{} IPGeolocation        {}'.format('_CYAN_', stts['IPGeolocation']['Status'], '_RESET_'),
    '  {}[20]{} Optiva-Framework     {}'.format('_CYAN_', stts['OptivaFramework']['Status'], '_RESET_'),
    '  {}[21]{} wpscan               {}'.format('_CYAN_', stts['wpscan']['Status'], '_RESET_'),
    '  {}[22]{} theHarvester         {}'.format('_CYAN_', stts['theHarvester']['Status'], '_RESET_'),
    '  {}[23]{} KnockMail            {}'.format('_CYAN_', stts['KnockMail']['Status'], '_RESET_'),
    '  {}[24]{} dmitry               {}'.format('_CYAN_', stts['SCANNERINURLBR']['Status'], '_RESET_'),
    '  {}[25]{} ShodanHat            {}'.format('_CYAN_', stts['dmitry']['Status'], '_RESET_'),
    '  {}[26]{} Hatwitch             {}'.format('_CYAN_', stts['ShodanHat']['Status'], '_RESET_'),
    '  {}[27]{} URLextractor         {}'.format('_CYAN_', stts['Hatwitch']['Status'], '_RESET_'),
    '  {}[28]{} webkiller            {}'.format('_CYAN_', stts['URLextractor']['Status'], '_RESET_'),
    '  {}[29]{} creepy               {}'.format('_CYAN_', stts['webkiller']['Status'], '_RESET_'),
    '  {}[30]{} Seeker               {}'.format('_CYAN_', stts['creepy']['Status'], '_RESET_'),
    '  {}[31]{} Twifo-cli            {}'.format('_CYAN_', stts['seeker']['Status'], '_RESET_'),
    '  {}[32]{} Sherlock             {}'.format('_CYAN_', stts['twifo_cli']['Status'], '_RESET_'),
    '  {}[33]{} osi.ig               {}'.format('_CYAN_', stts['sherlock']['Status'], '_RESET_'),
    '  {}[00]{} {}                   {}'.format('_CYAN_', stts['osi_ig']['Status'], '_RESET_', lang()['goBack']),
    '                                  ',
    '  {}Green:{} Installed or Clonned '.format('_GREEN_', '_RESET_'),
		'  {}White:{} Not Installed or Clonned '.format('_WHITE_', '_RESET_'),
		'                                  ',
    '  {}[{}{}{}]{}: {}         {}\n'.format('_CYAN_', '_GREEN_', tips['title'], '_CYAN_', '_WHITE_', random.choice(tips['DoS']), '_RESET_'),
  ]

  for tool in tools:
    print(colorTreatment(tool))
    wait(0.01)

  choice = input('  ' + lang()['input'])

  if choice.replace(' ', '') != '' and choice.isnumeric():
    if int(choice) == 0:   return 'restart'
    elif int(choice) == 1: return nmap()
    elif int(choice) == 2: return Th3inspector()
    elif int(choice) == 3: return angryFuzzer()
    elif int(choice) == 4: return PhoneInfoga()    
    elif int(choice) == 5: return FBI()    
    elif int(choice) == 6: return Infoga()
    elif int(choice) == 7: return InfoSploit()
    elif int(choice) == 8: return BillCipher()
    elif int(choice) == 9: return gasmask()
    elif int(choice) == 10: return OSIF()
    elif int(choice) == 11: return inmux()
    elif int(choice) == 12: return IPTracer()
    elif int(choice) == 13: return RED_HAWK()
    elif int(choice) == 14: return TMscanner()
    elif int(choice) == 15: return sqlmx_termux()
    elif int(choice) == 16: return reconspider()
    elif int(choice) == 17: return ReconDog()
    elif int(choice) == 18: return userrecon()
    elif int(choice) == 19: return IPGeolocation()
    elif int(choice) == 20: return OptivaFramework()
    elif int(choice) == 21: return wpscan()
    elif int(choice) == 22: return theHarvester()
    elif int(choice) == 23: return KnockMail()
    elif int(choice) == 24: return dmitry()
    elif int(choice) == 25: return ShodanHat()
    elif int(choice) == 26: return Hatwitch()
    elif int(choice) == 27: return URLextractor()
    elif int(choice) == 28: return webkiller()
    elif int(choice) == 29: return creepy()
    elif int(choice) == 30: return seeker()
    elif int(choice) == 31: return twifo_cli()
    elif int(choice) == 32: return sherlock()
    elif int(choice) == 33: return osi_ig()
    else: return 'error'
  else: return 'error'
  