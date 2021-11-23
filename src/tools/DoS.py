'''
DoS - Tools
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
def xerxes():
  update()
  clone(
    author="sepehrdaddev",
    repo="Xerxes"
  )
  cc(('dos', 'xerxes'), 'Xerxes foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def slowloris():
  update()
  clone(
    author="llaera",
    repo="slowloris.pl"
  )
  cc(('dos', 'slowloris'), 'Slowloris.pl foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def hammer():
  update()
  clone(
    author="cyweb",
    repo="hammer"
  )
  cc(('dos', 'hammer'), 'Hammer foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def Hunner():
  update()
  clone(
    author="b3-v3r",
    repo="Hunner"
  )
  cc(('dos', 'Hunner'), 'Hunner foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def GoldenEye():
  update()
  clone(
    author="jseidl",
    repo="GoldenEye"
  )
  cc(('dos', 'GoldenEye'), 'GoldenEye foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def DDosAttack():
  update()
  clone(
    author="Ha3MrX",
    repo="DDos-Attack"
  )
  cc(('dos', 'DDosAttack'), 'DDos-Attack foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def Ddoser():
  update()
  clone(
    author="ZonePy",
    repo="Ddoser"
  )
  cc(('dos', 'Ddoser'), 'Ddoser foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def torshammer():
  update()
  clone(
    author="dotfighter",
    repo="torshammer"
  )
  cc(('dos', 'torshammer'), 'Torshammer foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def LITEDDOS():
  update()
  clone(
    author="4L13199",
    repo="LITEDDOS"
  )
  cc(('dos', 'LITEDDOS'), 'LITEDDOS foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def hulk():
  update()
  clone(
    author="grafov",
    repo="hulk"
  )
  cc(('dos', 'hulk'), 'hulk foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def MemcrashedDDoSExploit():
  update()
  clone(
    author="649",
    repo="Memcrashed-DDoS-Exploit"
  )
  cc(('dos', 'MemcrashedDDoSExploit'), 'Memcrashed-DDoS-Exploit foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def PlanetworkDDOS():
  update()
  clone(
    author="Hydra7",
    repo="Planetwork-DDOS"
  )
  cc(('dos', 'PlanetworkDDOS'), 'Planetwork-DDOS foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def ping_of_death():
  update()
  clone(
    author="ffmancera",
    repo="ping_of_death"
  )
  cc(('dos', 'ping_of_death'), 'Ping_of_death foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def IcmpiFlood():
  update()
  clone(
    author="pioneerhfy",
    repo="IcmpiFlood"
  )
  cc(('dos', 'IcmpiFlood'), 'IcmpiFlood foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def exploitblacknurse():
  update()
  clone(
    author="opsxcq",
    repo="exploit-blacknurse"
  )
  cc(('dos', 'exploitblacknurse'), 'Exploit-blacknurse foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def PyFlooder():
  update()
  clone(
    author="D4Vinci",
    repo="PyFlooder"
  )
  cc(('dos', 'PyFlooder'), 'PyFlooder foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def Saddam():
  update()
  clone(
    author="OffensivePython",
    repo="Saddam"
  )
  cc(('dos', 'Saddam'), 'Saddam foi clonado com sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def ntpdos():
  update()
  clone(
    author="vpnguy-zz",
    repo="ntpdos"
  )
  cc(('dos', 'ntpdos'), 'Ntpdos sucesso... Para acessa-lo vá para a pasta tools.')
  return 'restart'

def menu():
  stts = getSttsTool()['dos']

  tips = lang()['tips']
  items = [
    '\n',
    '=== {}                              '.format(lang()['tools']['dos']),
    '  {}[01]{} Xerxes                  {}'.format('_CYAN_', stts['xerxes']['Status'], '_RESET_'),
    '  {}[02]{} Slowloris               {}'.format('_CYAN_', stts['slowloris']['Status'], '_RESET_'),
    '  {}[03]{} Hammer                  {}'.format('_CYAN_', stts['hammer']['Status'], '_RESET_'),
    '  {}[04]{} Hunner                  {}'.format('_CYAN_', stts['Hunner']['Status'], '_RESET_'),
    '  {}[05]{} GoldenEye               {}'.format('_CYAN_', stts['GoldenEye']['Status'], '_RESET_'),
    '  {}[06]{} DDos-Attack             {}'.format('_CYAN_', stts['DDosAttack']['Status'], '_RESET_'),
    '  {}[07]{} Ddoser                  {}'.format('_CYAN_', stts['Ddoser']['Status'], '_RESET_'),
    '  {}[08]{} torshammer              {}'.format('_CYAN_', stts['torshammer']['Status'], '_RESET_'),
    '  {}[09]{} LITEDDOS                {}'.format('_CYAN_', stts['LITEDDOS']['Status'], '_RESET_'),
    '  {}[10]{} hulk                    {}'.format('_CYAN_', stts['hulk']['Status'], '_RESET_'),
    '  {}[11]{} Memcrashed-DDoS-Exploit {}'.format('_CYAN_', stts['MemcrashedDDoSExploit']['Status'], '_RESET_'),
    '  {}[12]{} Planetwork-DDOS         {}'.format('_CYAN_', stts['PlanetworkDDOS']['Status'], '_RESET_'),
    '  {}[13]{} Ping_of_death           {}'.format('_CYAN_', stts['ping_of_death']['Status'], '_RESET_'),
    '  {}[14]{} IcmpiFlood              {}'.format('_CYAN_', stts['IcmpiFlood']['Status'], '_RESET_'),
    '  {}[15]{} exploit-blacknurse      {}'.format('_CYAN_', stts['exploitblacknurse']['Status'], '_RESET_'),
    '  {}[16]{} PyFlooder               {}'.format('_CYAN_', stts['PyFlooder']['Status'], '_RESET_'),
    '  {}[17]{} Saddam                  {}'.format('_CYAN_', stts['Saddam']['Status'], '_RESET_'),
    '  {}[18]{} ntpdos                  {}'.format('_CYAN_', stts['ntpdos']['Status'], '_RESET_'),
    '  {}[00]{} {}                        '.format('_CYAN_', '_RESET_', lang()['goBack']),
    '                                     ',
    '  {}Green:{} Installed or Clonned    '.format('_GREEN_', '_RESET_'),
		'  {}White:{} Not Installed or Clonned'.format('_WHITE_', '_RESET_'),
		'                                     ',
    '  {}[{}{}{}]{}: {}              {}\n'.format('_CYAN_', '_GREEN_', tips['title'], '_CYAN_', '_WHITE_', random.choice(tips['DoS']), '_RESET_'),
  ]

  for item in items: 
    print(colorTreatment(item))
    wait(0.01)

  choice = input('  ' + lang()['input'])

  if choice.replace(' ', '') != '' and choice.isnumeric():
    if   int(choice) == 0: return 'restart'
    elif int(choice) == 1: return xerxes()
    elif int(choice) == 2: return slowloris()
    elif int(choice) == 3: return hammer()
    elif int(choice) == 4: return Hunner()
    elif int(choice) == 5: return GoldenEye()
    elif int(choice) == 6: return DDosAttack()
    elif int(choice) == 7: return Ddoser()
    elif int(choice) == 8: return torshammer()
    elif int(choice) == 9: return LITEDDOS()
    elif int(choice) == 10: return hulk()
    elif int(choice) == 11: return MemcrashedDDoSExploit()
    elif int(choice) == 12: return PlanetworkDDOS()
    elif int(choice) == 13: return ping_of_death()
    elif int(choice) == 14: return IcmpiFlood()
    elif int(choice) == 15: return exploitblacknurse()
    elif int(choice) == 16: return PyFlooder()
    elif int(choice) == 17: return Saddam()
    elif int(choice) == 18: return ntpdos()
    else: return 'error'
  else: return 'error'