# By Feh's (Ahosall)
from requests import get

URL_DATA = "https://gist.githubusercontent.com/Ahosall/055dfcac458801849b43be7efc59e25a/raw"

def tools(tType: int):
  r = get(URL_DATA)
  lines = r.text.split('\n')
  data = []

  for l in lines:
    dt = l.split(';')
    if int(dt[0]) == tType:
      data.append(dt)
  
  return data
