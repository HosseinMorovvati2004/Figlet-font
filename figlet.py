from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
if len(sys.argv) ==1:
    isFontRandomize= True
elif len(sys.argv) ==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font"):
   isFontRandomize = False
else :
   sys.exit(1)
   
figlet.getFonts()

if isFontRandomize ==False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid")
        sys.exit(1)
else:
    font=random.choice(figlet.getFonts())

x = input("Input:")
print("Output:")
print(figlet.renderText(x))


