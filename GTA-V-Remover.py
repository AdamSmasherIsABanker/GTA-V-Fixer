from genericpath import isfile
from operator import truediv
import os
from sys import dllhandle
p = print

p("Hey there, thanks so much for using my tool!")
p("Just type in the number of the current supported tools, and it will delete the files.")
p("WARNING! PLEASE BE CAREFUL WITH YOUR MODS. WARNING!\n")
p("1. Scripthook V")
p("2. Scripthook .NET")
p("3. Trainer-V")
choice = int(input(":"))

if (choice == 1):
    if (isfile('ScriptHookV.dll') == True & isfile('dinput8.dll') == True & isfile('NativeTrainer.asi') == True):
        p("Scripthook V Has Been Removed.")
        os.remove('ScriptHookV.dll')
        os.remove('dinput8.dll')
        os.remove('NativeTrainer.asi')
    else:
        p("Mod Is Not Installed")
if (choice == 2):
    if (isfile('ScriptHookVDotNet.asi') == True & isfile('ScriptHookVDotNet2.dll') == True & isfile('ScriptHookVDotNet3.dll') == True): 
        p("Scripthook .NET Has Been Removed.")
        os.remove('ScriptHookVDotNet.asi')
        os.remove('ScriptHookVDotNet2.dll')
        os.remove('ScriptHookVDotNet3.dll')
    else:
        p("Mod Is Not Installed.")
if (choice == 3):
    if (isfile('trainerv.ini') == True & isfile('TrainerV.asi') == True):
        p("Trainer-V Has Been Removed.")
        os.remove('trainerv.ini')
        os.remove('TrainerV.asi')
    else:
        p("This Mod Is Not Installed.")
close = input("Press Enter To Close. ")