# By Feh's (Ahosall)

import json

# Vars
LANGUAGES = None
with open('.\\datas\\languages.json', encoding='utf-8') as f:
  LANGUAGES = json.load(f)

# Language class
class Lang:
  def __init__(self, lang):
    self.lang = LANGUAGES[lang]
  
  def changeLanguage(self, newLang):
    pass

