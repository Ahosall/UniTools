'''
Phishing - Tools
'''

# Imports
from time import sleep as wait

# --- Utils
from src.utils.configs import getSttsTool
from src.utils.functions import update, install, clone, cc
from src.utils.languages import lang
from src.utils.colorFunc import colorTreatment

# Tools
# 00 | SocialFish
def SocialFish():
  clone(
    author="An0nUD4Y",
    repo="SocialFish"
    )
  cc(('phishing', 'SocialFish'), 'SocialFish  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 01 | SocialPhish
def SocialPhish():
  update()
  clone(
    author="xHak9x",
    repo="SocialPhish",
    installer="shell",
    script="cd ~/SocialPhish && chmod +x socialphish.sh"
   )
  cc(('phishing', 'SocialPhish'), 'SocialPhish  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 02 | Phisherman
def Phisherman():
  clone(
    author="FDX100",
    repo="Phisher-man"
   )
  cc(('phishing', 'Phisherman'), 'Phisher-man  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 03 | shellphish
def shellphish():
  clone(
    author="thelinuxchoice",
    repo="shellphish",
    installer="shell",
    script="cd ~/shellphish && pkg install php && pkg install curl && pkg install python2 && chmod +x shellphish.sh"
  )
  cc(('phishing', 'shellphish'), 'Shellphish  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 04 | gophish
def gophish():
  clone(
    author="gophish",
    repo="gophish"
    )
  cc(('phishing', 'gophish'), 'Gophish  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 05 | TurkSploit
def TurkSploit():
  clone(
    author="DoughBoiKush",
    repo="Turk-Sploit"
    )
  cc(('phishing', 'TurkSploit'), 'Turk-Sploit  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 06 | weeman
def weeman():
  clone(
    author="evait-security",
    repo="weeman"
    )
  cc(('phishing', 'weeman'), 'Weeman  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 07 | dnstwist
def dnstwist():
  clone(
    author="elceef",
    repo="dnstwist"
    )
  cc(('phishing', 'dnstwist'), 'DnsTwist  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 08 | Phlexish
def Phlexish():
  clone(
    author="KnightSec-Official",
    repo="Phlexish"
    )
  cc(('phishing', 'Phlexish'), 'Phlexish  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 09 | zphisher
def zphisher():
  clone(
    author="htr-tech",
    repo="zphisher",
    installer="shell",
    script="cd ~/zphisher && chmod +x zphisher.sh")
  cc(('phishing', 'zphisher'), 'Zphisher  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 10 | nexphisher
def nexphisher():
  clone(
    author="htr-tech",
    repo="nexphisher",
    installer="shell",
    script="cd ~/nexphisher && bash tmux_setup")
  cc(('phishing', 'nexphisher'), 'Nexphisher  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'
# 11 | grabcam
def grabcam():
  clone(
    author="noob-hackers", 
    repo="grabcam", 
    moveTo="../tools"
  )
  cc(('phishing', 'grabcam'), 'Grabcam  has been successfully cloned or installed... To access it go to the tools folder.')
  return 'restart'


def menu():
  stts = getSttsTool()['phishing']

  items = [
    '\n', 
    '=== {}                         '.format(lang()['tools']['phishing']),
    '  {}[01]{} SocialFish            {}'.format('_CYAN_', stts['SocialFish']['Status'], '_RESET_'),
    '  {}[02]{} SocialPhish           {}'.format('_CYAN_', stts['SocialPhish']['Status'], '_RESET_'),
    '  {}[03]{} Phisherman            {}'.format('_CYAN_', stts['Phisherman']['Status'], '_RESET_'),
    '  {}[04]{} Shellphish            {}'.format('_CYAN_', stts['shellphish']['Status'], '_RESET_'),
    '  {}[05]{} Gophish               {}'.format('_CYAN_', stts['gophish']['Status'], '_RESET_'),
    '  {}[06]{} TurkSploit            {}'.format('_CYAN_', stts['TurkSploit']['Status'], '_RESET_'),
    '  {}[07]{} Weeman                {}'.format('_CYAN_', stts['weeman']['Status'], '_RESET_'),
    '  {}[08]{} Dnstwist              {}'.format('_CYAN_', stts['dnstwist']['Status'], '_RESET_'),
    '  {}[09]{} Phlexish              {}'.format('_CYAN_', stts['Phlexish']['Status'], '_RESET_'),
    '  {}[10]{} PZphisher             {}'.format('_CYAN_', stts['zphisher']['Status'], '_RESET_'),
    '  {}[11]{} Nexphisher           {}'.format('_CYAN_', stts['nexphisher']['Status'], '_RESET_'),
    '  {}[12]{} Grabcam              {}'.format('_CYAN_', stts['grabcam']['Status'], '_RESET_'),
    '  {}[00]{} {}                     '.format('_CYAN_', '_RESET_', lang()['goBack']),
    '                                  ',
    '  {}Green:{} Installed or Clonned '.format('_GREEN_', '_RESET_'),
		'  {}White:{} Not Installed or Clonned '.format('_WHITE_', '_RESET_'),
		'                                  ',
  ]

  for item in items:
    print(colorTreatment(item))
    wait(0.01)
  
  choice = input('  ' + lang()['input'])
  if choice.replace(' ', '') != '' and choice.isnumeric():
    if int(choice) == 0: return 'restart'
    elif int(choice) == 1: return SocialFish()
    elif int(choice) == 2: return SocialPhish()
    elif int(choice) == 3: return Phisherman()
    elif int(choice) == 4: return shellphish()
    elif int(choice) == 5: return gophish()
    elif int(choice) == 6: return TurkSploit()
    elif int(choice) == 7: return weeman()
    elif int(choice) == 8: return dnstwist()
    elif int(choice) == 9: return Phlexish()
    elif int(choice) == 10: return zphisher()
    elif int(choice) == 11: return nexphisher()
    elif int(choice) == 12: return grabcam()
    else: 'error'
  else: return 'error'