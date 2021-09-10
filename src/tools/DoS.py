'''
DoS - Tools
'''

# Imports
import random

from time import sleep as wait

# --- Utils
from src.utils.functions import update, install, clone, cc
from src.utils.languages import lang
from src.utils.colorFunc import colorTreatment

# Tools
def xerxes():
  update()
  clone(
    author="sepehrdaddev",
    repo="Xerxes"
  )
  cc('Xerxes foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def slowloris():
  update()
  clone(
    author="llaera",
    repo="slowloris.pl"
  )
  cc('Slowloris.pl foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def hammer():
  update()
  clone(
    author="cyweb",
    repo="hammer"
  )
  cc('Hammer foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def Hunner():
  update()
  clone(
    author="b3-v3r",
    repo="Hunner"
  )
  cc('Hunner foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def GoldenEye():
  update()
  clone(
    author="jseidl",
    repo="GoldenEye"
  )
  cc('GoldenEye foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def DDosAttack():
  update()
  clone(
    author="Ha3MrX",
    repo="DDos-Attack"
  )
  cc('DDos-Attack foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def Ddoser():
  update()
  clone(
    author="ZonePy",
    repo="Ddoser"
  )
  cc('Ddoser foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def torshammer():
  update()
  clone(
    author="dotfighter",
    repo="torshammer"
  )
  cc('Torshammer foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def LITEDDOS():
  update()
  clone(
    author="4L13199",
    repo="LITEDDOS"
  )
  cc('LITEDDOS foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def hulk():
  update()
  clone(
    author="grafov",
    repo="hulk"
  )
  cc('hulk foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def MemcrashedDDoSExploit():
  update()
  clone(
    author="649",
    repo="Memcrashed-DDoS-Exploit"
  )
  cc('Memcrashed-DDoS-Exploit foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def PlanetworkDDOS():
  update()
  clone(
    author="Hydra7",
    repo="Planetwork-DDOS"
  )
  cc('Planetwork-DDOS foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def ping_of_death():
  update()
  clone(
    author="ffmancera",
    repo="ping_of_death"
  )
  cc('Ping_of_death foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def IcmpiFlood():
  update()
  clone(
    author="pioneerhfy",
    repo="IcmpiFlood"
  )
  cc('IcmpiFlood foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def exploitblacknurse():
  update()
  clone(
    author="opsxcq",
    repo="exploit-blacknurse"
  )
  cc('Exploit-blacknurse foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def PyFlooder():
  update()
  clone(
    author="D4Vinci",
    repo="PyFlooder"
  )
  cc('PyFlooder foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def Saddam():
  update()
  clone(
    author="OffensivePython",
    repo="Saddam"
  )
  cc('Saddam foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def ntpdos():
  update()
  clone(
    author="vpnguy-zz",
    repo="ntpdos"
  )
  cc('Ntpdos sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def menu():
  tips = lang()['tips']
  items = [
    '\n',
    '=== {}                              '.format(lang()['tools']['dos']),
    '  {}[1]{} Xerxes                    '.format('_CYAN_', '_RESET_'),
    '  {}[2]{} Slowloris                 '.format('_CYAN_', '_RESET_'),
    '  {}[3]{} Hammer                    '.format('_CYAN_', '_RESET_'),
    '  {}[4]{} Hunner                    '.format('_CYAN_', '_RESET_'),
    '  {}[5]{} GoldenEye                 '.format('_CYAN_', '_RESET_'),
    '  {}[6]{} DDos-Attack               '.format('_CYAN_', '_RESET_'),
    '  {}[7]{} Ddoser                    '.format('_CYAN_', '_RESET_'),
    '  {}[8]{} torshammer                '.format('_CYAN_', '_RESET_'),
    '  {}[9]{} LITEDDOS                  '.format('_CYAN_', '_RESET_'),
    '  {}[10]{} hulk                     '.format('_CYAN_', '_RESET_'),
    '  {}[11]{} Memcrashed-DDoS-Exploit  '.format('_CYAN_', '_RESET_'),
    '  {}[12]{} Planetwork-DDOS          '.format('_CYAN_', '_RESET_'),
    '  {}[13]{} Ping_of_death            '.format('_CYAN_', '_RESET_'),
    '  {}[14]{} IcmpiFlood               '.format('_CYAN_', '_RESET_'),
    '  {}[15]{} exploit-blacknurse       '.format('_CYAN_', '_RESET_'),
    '  {}[16]{} PyFlooder                '.format('_CYAN_', '_RESET_'),
    '  {}[17]{} Saddam                   '.format('_CYAN_', '_RESET_'),
    '  {}[18]{} ntpdos                   '.format('_CYAN_', '_RESET_'),
    '  {}[00]{} {}                       '.format('_CYAN_', '_RESET_', lang()['goBack']),
    '                                    ',
    '  {}[{}{}{}]{}: {}              {}\n'.format('_CYAN_', '_GREEN_', tips['title'], '_CYAN_', '_WHITE_', random.choice(tips['DoS']), '_RESET_'),
  ]

  for item in items: 
    print(colorTreatment(item))
    wait(0.01)

  choice = input('  ' + lang()['input'])

  if choice.replace(' ', '') != '':
    if choice in ['0', '00']: return 'restart'
    elif choice in ["1", "01"]: return xerxes()
    elif choice in ["2", "02"]: return slowloris()
    elif choice in ["3", "03"]: return hammer()
    elif choice in ["4", "04"]: return Hunner()
    elif choice in ["5", "05"]: return GoldenEye()
    elif choice in ["6", "06"]: return DDosAttack()
    elif choice in ["7", "07"]: return Ddoser()
    elif choice in ["8", "08"]: return torshammer()
    elif choice in ["9", "09"]: return LITEDDOS()
    elif choice in "10": return hulk()
    elif choice in "11": return MemcrashedDDoSExploit()
    elif choice in "12": return PlanetworkDDOS()
    elif choice in "13": return ping_of_death()
    elif choice in "14": return IcmpiFlood()
    elif choice in "15": return exploitblacknurse()
    elif choice in "16": return PyFlooder()
    elif choice in "17": return Saddam()
    elif choice in "18": return ntpdos()
    else: return 'error'
  else: return 'error'