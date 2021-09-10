'''
Phishing - Tools
'''

# Imports
from time import sleep as wait

# --- Utils
from src.utils.functions import update, install, clone, cc
from src.utils.languages import lang
from src.utils.colorFunc import colorTreatment

# Tools
# 00 | SocialFish
def SocialFish():
  update()
  clone(
    author="An0nUD4Y",
    repo="SocialFish"
    )
  cc('SocialFish foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
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
  cc('SocialPhish foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 02 | Phisherman
def Phisherman():
  update()
  clone(
    author="FDX100",
    repo="Phisher-man"
   )
  cc('Phisher-man foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 03 | shellphish
def shellphish():
  update()
  clone(
    author="thelinuxchoice",
    repo="shellphish",
    installer="shell",
    script="cd ~/shellphish && pkg install php && pkg install curl && pkg install python2 && chmod +x shellphish.sh"
  )
  cc('Shellphish foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 04 | gophish
def gophish():
  update()
  clone(
    author="gophish",
    repo="gophish"
    )
  cc('Gophish foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 05 | TurkSploit
def TurkSploit():
  update()
  clone(
    author="DoughBoiKush",
    repo="Turk-Sploit"
    )
  cc('Turk-Sploit foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 06 | weeman
def weeman():
  update()
  clone(
    author="evait-security",
    repo="weeman"
    )
  cc('Weeman foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 07 | dnstwist
def dnstwist():
  update()
  clone(
    author="elceef",
    repo="dnstwist"
    )
  cc('DnsTwist foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 08 | Phlexish
def Phlexish():
  update()
  clone(
    author="KnightSec-Official",
    repo="Phlexish"
    )
  cc('Phlexish foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 09 | zphisher
def zphisher():
  update()
  clone(
    author="htr-tech",
    repo="zphisher",
    installer="shell",
    script="cd ~/zphisher && chmod +x zphisher.sh")
  cc('Zphisher foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 10 | nexphisher
def nexphisher():
  update()
  clone(
    author="htr-tech",
    repo="nexphisher",
    installer="shell",
    script="cd ~/nexphisher && bash tmux_setup")
  cc('Nexphisher foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'
# 11 | grabcam
def grabcam():
  update()
  clone(
    author="noob-hackers", 
    repo="grabcam", 
    moveTo="../tools"
  )
  cc('Grabcam foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'


def menu():
  items = [
    '\n', 
    '=== {}                         '.format(lang()['tools']['phishing']),
    '  {}[1]{} SocialFish           '.format('_CYAN_', '_RESET_'),
    '  {}[2]{} SocialPhish          '.format('_CYAN_', '_RESET_'),
    '  {}[3]{} Phisherman           '.format('_CYAN_', '_RESET_'),
    '  {}[4]{} Shellphish           '.format('_CYAN_', '_RESET_'),
    '  {}[5]{} Gophish              '.format('_CYAN_', '_RESET_'),
    '  {}[5]{} TurkSploit           '.format('_CYAN_', '_RESET_'),
    '  {}[6]{} Weeman               '.format('_CYAN_', '_RESET_'),
    '  {}[7]{} Dnstwist             '.format('_CYAN_', '_RESET_'),
    '  {}[8]{} Phlexish             '.format('_CYAN_', '_RESET_'),
    '  {}[9]{} PZphisher            '.format('_CYAN_', '_RESET_'),
    '  {}[10]{} Nexphisher          '.format('_CYAN_', '_RESET_'),
    '  {}[11]{} Grabcam             '.format('_CYAN_', '_RESET_'),
    '  {}[00]{} {}                  '.format('_CYAN_', '_RESET_', lang()['goBack']),
    '                               '
  ]

  for item in items:
    print(colorTreatment(item))
    wait(0.01)
  
  choice = input('  ' + lang()['input'])
  if choice.replace(' ', '') != '':
    if choice in['0', '00']: return 'restart'
    elif choice in["1", "01"]: return SocialFish()
    elif choice in["2", "02"]: return SocialPhish()
    elif choice in["3", "03"]: return Phisherman()
    elif choice in["4", "04"]: return shellphish()
    elif choice in["5", "05"]: return gophish()
    elif choice in["6", "06"]: return TurkSploit()
    elif choice in["7", "07"]: return weeman()
    elif choice in["8", "08"]: return dnstwist()
    elif choice in["9", "09"]: return Phlexish()
    elif choice in "10": return zphisher()
    elif choice in "11": return nexphisher()
    elif choice in "12": return grabcam()
    else: 'error'
  else: return 'error'