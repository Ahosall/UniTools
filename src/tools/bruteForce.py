'''
Brute Force - Tools
'''

# Imports
from time import sleep as wait

# --- Utils
from src.utils.configs import getSttsTool
from src.utils.functions import update, install, clone, cc
from src.utils.languages import lang
from src.utils.colorFunc import colorTreatment

# Tools
# 01 | FacebookBruteForce
def FacebookBruteForce():
	clone(
		author="IAmBlackHacker",
		repo="Facebook-BruteForce"
	)
	cc(('bForce', 'FacebookBruteForce'), 'Facebook-BruteForce has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 02 | Hydra
def Hydra():
  update()
  install("hydra")
  cc(('bForce', 'Hydra'), 'Hydra has been successfully installed...')
  return 'restart'
# 03 | facebookcracker
def facebookcracker():
	clone(
		author="Ha3MrX",
		repo="facebook-cracker"
	)
	cc(('bForce', 'facebookcracker'), 'Facebook-cracker has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 04 | Instahack
def Instahack():
	clone(
		author="fuck3erboy",
		repo="instahack"
	)
	cc(('bForce', 'Instahack'), 'Instahack has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 05 | hashcat
def hashcat():
	clone(
		author="hashcat",
		repo="hashcat"
	)
	cc(('bForce', 'hashcat'), 'Hashcat has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 06 | BlackHydra
def BlackHydra():
	clone(
		author="Gameye98",
		repo="Black-Hydra"
	)
	cc(('bForce', 'BlackHydra'), 'Black-Hydra has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 07 | HashBuster
def HashBuster():
	clone(
		author="s0md3v",
		repo="Hash-Buster"
	)
	cc(('bForce', 'HashBuster'), 'Hash-Buster has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 08 | Facebom
def Facebom():
	clone(
		author="Oseid",
		repo="Facebom",
		installer="pip",
		script="requests mechanize"
	)
	cc(('bForce', 'Facebom'), 'Facebom has been successfully cloned and installed... To access it go to the tools folder.')
	return 'restart'
# 09 | brutespray
def brutespray():
	clone(
		author="hanshaze",
		repo="brutespray",
		installer="pip"
	)
	cc(('bForce', 'brutespray'), 'Brutespray has been successfully cloned and installed... To access it go to the tools folder.')
	return 'restart'
# 10 | hyprPulse
def hyprPulse():
	clone(
		author="Pure-L0G1C",
		repo="hyprPulse",
		installer="shell",
		script="chmod +x install.sh && bash install.sh"
	)
	cc(('bForce', 'hyprPulse'), 'HyprPulse has been successfully cloned and installed... To access it go to the tools folder.')
	return 'restart'
# 11 | lazybee
def lazybee():
	clone(
		author="noob-hackers",
		repo="lazybee",
		installer="pip",
		script="lolcat"
	)
	cc(('bForce', 'lazybee'), 'Lazybee has been successfully cloned and installed... To access it go to the tools folder.')
	return 'restart'

# Menu
def menu():
  stts = getSttsTool()['bForce']
  items = [
    '            ',
    '=== {}'.format(lang()['tools']['bruteForce']),
    '  {}[01]{} FacebookBruteForce   {}'.format('_CYAN_', stts['FacebookBruteForce']['Status'], '_RESET_'),
    '  {}[02]{} Hydra                {}'.format('_CYAN_', stts['Hydra']['Status'], '_RESET_'),
    '  {}[03]{} facebookcracker      {}'.format('_CYAN_', stts['facebookcracker']['Status'], '_RESET_'),
    '  {}[04]{} Instahack            {}'.format('_CYAN_', stts['Instahack']['Status'], '_RESET_'),
    '  {}[05]{} hashcat              {}'.format('_CYAN_', stts['hashcat']['Status'], '_RESET_'),
    '  {}[06]{} BlackHydra           {}'.format('_CYAN_', stts['BlackHydra']['Status'], '_RESET_'),
    '  {}[07]{} HashBuster           {}'.format('_CYAN_', stts['HashBuster']['Status'], '_RESET_'),
    '  {}[08]{} Facebom              {}'.format('_CYAN_', stts['Facebom']['Status'], '_RESET_'),
    '  {}[09]{} brutespray           {}'.format('_CYAN_', stts['brutespray']['Status'], '_RESET_'),
    '  {}[10]{} hyprPulse            {}'.format('_CYAN_', stts['hyprPulse']['Status'], '_RESET_'),
    '  {}[11]{} lazybee              {}'.format('_CYAN_', stts['lazybee']['Status'], '_RESET_'),
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

  if choice.replace(' ', '') != '':
    if choice in ['0', '00']:   return 'restart'
    elif choice in ["1", "01"]: return FacebookBruteForce()
    elif choice in ["2", "02"]: return Hydra()
    elif choice in ["3", "03"]: return facebookcracker()
    elif choice in ["4", "04"]: return Instahack()
    elif choice in ["5", "05"]: return hashcat()
    elif choice in ["6", "06"]: return BlackHydra()
    elif choice in ["7", "07"]: return HashBuster()
    elif choice in ["8", "08"]: return Facebom()
    elif choice in ["9", "09"]: return brutespray()
    elif choice in "10": return hyprPulse()
    elif choice in "11": return lazybee()
    else: return 'error'
  else: return 'error'