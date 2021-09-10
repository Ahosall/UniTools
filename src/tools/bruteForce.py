'''
Brute Force - Tools
'''

# Imports
from time import sleep as wait

# --- Utils
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
	cc('Facebook-BruteForce has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 02 | Hydra
def Hydra():
  update()
  install("hydra")
  cc('Hydra has been successfully installed...')
  return 'restart'
# 03 | facebookcracker
def facebookcracker():
	clone(
		author="Ha3MrX",
		repo="facebook-cracker"
	)
	cc('Facebook-cracker has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 04 | Instahack
def Instahack():
	clone(
		author="fuck3erboy",
		repo="instahack"
	)
	cc('Instahack has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 05 | hashcat
def hashcat():
	clone(
		author="hashcat",
		repo="hashcat"
	)
	cc('Hashcat has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 06 | BlackHydra
def BlackHydra():
	clone(
		author="Gameye98",
		repo="Black-Hydra"
	)
	cc('Black-Hydra has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 07 | HashBuster
def HashBuster():
	clone(
		author="s0md3v",
		repo="Hash-Buster"
	)
	cc('Hash-Buster has been cloned successfully... To access it go to the tools folder.')
	return 'restart'
# 08 | Facebom
def Facebom():
	clone(
		author="Oseid",
		repo="Facebom",
		installer="pip",
		script="requests mechanize"
	)
	cc('Facebom has been successfully cloned and installed... To access it go to the tools folder.')
	return 'restart'
# 09 | brutespray
def brutespray():
	clone(
		author="hanshaze",
		repo="brutespray",
		installer="pip"
	)
	cc('Brutespray has been successfully cloned and installed... To access it go to the tools folder.')
	return 'restart'
# 10 | hyprPulse
def hyprPulse():
	clone(
		author="Pure-L0G1C",
		repo="hyprPulse",
		installer="shell",
		script="chmod +x install.sh && bash install.sh"
	)
	cc('HyprPulse has been successfully cloned and installed... To access it go to the tools folder.')
	return 'restart'
# 11 | lazybee
def lazybee():
	clone(
		author="noob-hackers",
		repo="lazybee",
		installer="pip",
		script="lolcat"
	)
	cc('Lazybee has been successfully cloned and installed... To access it go to the tools folder.')
	return 'restart'

# Menu
def menu():
  items = [
    '            ',
    '=== {}'.format(lang()['tools']['bruteForce']),
    '  {}[1]{} FacebookBruteForce     '.format('_CYAN_', '_RESET_'),
    '  {}[2]{} Hydra                  '.format('_CYAN_', '_RESET_'),
    '  {}[3]{} facebookcracker        '.format('_CYAN_', '_RESET_'),
    '  {}[4]{} Instahack              '.format('_CYAN_', '_RESET_'),
    '  {}[5]{} hashcat                '.format('_CYAN_', '_RESET_'),
    '  {}[6]{} BlackHydra             '.format('_CYAN_', '_RESET_'),
    '  {}[7]{} HashBuster             '.format('_CYAN_', '_RESET_'),
    '  {}[8]{} Facebom                '.format('_CYAN_', '_RESET_'),
    '  {}[9]{} brutespray             '.format('_CYAN_', '_RESET_'),
    '  {}[10]{} hyprPulse             '.format('_CYAN_', '_RESET_'),
    '  {}[11]{} lazybee               '.format('_CYAN_', '_RESET_'),
    '  {}[00]{} {}                    '.format('_CYAN_', '_RESET_', lang()['goBack']),
    '                                 '
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