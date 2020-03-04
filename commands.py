from Backpack import inv
from Backpack import itms
from Places import Lct
truecmds = ['>help', '>inventory', '>look', '>equip', '>inventory', '>backpack', '>bag', '>pencilcase']
self.inv
self.itms
self.currentlct
self.currentdesc
def cmd():
  cmd = ''
  cmd = input()
  if cmd in truecmds:
    if cmd == '>help':
      print('The commands currently avaiable are; >help, >inventory  >look, and >equip.')
    elif cmd == '>inventory' or '>backpack' or '>pencilcase':
      for itms in inv:
        print('  ' + itms)
      print (str(len([inv]) + 1 ) + '/20')
    elif cmd == '>look':
      print ('you stand in' + currentlct + ' ' + curentdesc+ '')
  else:
    print('Thats not a valid command.')
while True:
  cmd()
