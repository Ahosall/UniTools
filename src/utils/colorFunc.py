'''
ColorFunctions - Utils
'''

# Vars
reset = '\033[00m'
bold = '\033[01m' 
underline ='\033[04m'
flashing = '\033[05m'
reverse='\033[07m'
hidden = '\033[08m'

black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'

# Main Function
def colorTreatment(string):

  result = string
  
  result = result.replace('_RESET_', reset)
  result = result.replace('_BOLD_', bold)
  result = result.replace('_UNDERLINE_', underline)
  result = result.replace('_FLASHING_', flashing)
  result = result.replace('_REVERSE_', reverse)
  result = result.replace('_HIDDEN_', hidden)
  
  result = result.replace('_BLACK_', black)
  result = result.replace('_RED_', red)
  result = result.replace('_GREEN_', green)
  result = result.replace('_YELLOW_', yellow)
  result = result.replace('_BLUE_', blue)
  result = result.replace('_MAGENTA_', magenta)
  result = result.replace('_CYAN_', cyan)
  result = result.replace('_WHITE_', white)

  return result