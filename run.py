import os

f = open('dbot.py')
t = f.read()
f.close()

te = t.replace("%TK%,"NTA5NzU2MDAzMTczMjY5NTA0.DsYF0Q.xotHK-dODPEqbwSqf7WpR7xiMkQ")

f = open('temp.py','w')
f.write(te)
f.close()

os.system('python3.6 temp.py')
os.remove('temp.py')
