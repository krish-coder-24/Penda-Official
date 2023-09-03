from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data
from files import get
import getopt, sys, os, pathlib

argumentList = sys.argv[1:]
options = "hVf:SU"
long_options = ["help", "version", "file", "shell", "update", "uninstall"]

__path = os.getcwd()
base = Data()

try:
   if sys.argv[1] == "help":
      get.help()
      
   arguments, values = getopt.getopt(argumentList, options, long_options)
   for currentArgument, currentValue in arguments:
       if currentArgument in ('-h', "--help"):
          get.help()
          exit(0)
       elif currentArgument in ('-V', "--version"):
          get.version()
          exit(0)

       elif currentArgument in ('-f', "--file"):
          file_name = str(currentValue)
          file = open(file_name, 'r')
          for line in file:
              line = line.strip()
              tokenizer = Lexer(line)
              tokens = tokenizer.tokenize()
              parser = Parser(tokens)
              tree = parser.parse()

              interpreter = Interpreter(tree, base)
              result = interpreter.interpret()
              if result is not None:
                  print (result)

          file.close()

       elif currentArgument in ('-S', "--shell"):
          os.system(f"python {__path}/shell.py")
          
       elif currentArgument in ('-U', "--update"):
         if os.path.isfile("/usr/share"):
            os.system(f"bash /root/.penda/update.sh")
         elif os.path.isfile("/data/data/com.termux"):
            os.system("bash ~/.penda/update.sh")
         elif os.path.isfile("C:/Windows/System32"):
            os.system(f"bash {__path}/update.sh")
          
       elif currentArgument in ("--uninstall"): 
          os.system(f"sudo bash {__path}/uninstall.sh")


except getopt.error as err:
    err = str(err)
    err = err.replace('option', '')
    if "-f requires argument" in err:
        print ("No file Specified !!")
    elif "requires argument" in err:
        err = err.replace("requires argument", "")
        print ("Option " + err + " Requires an Argument !!")
    elif "not recognized" in err:
        err = err.replace("not recognized", "")
        print ("No such Option: " + err)
    exit(1)

except FileNotFoundError:
  pass
  print ("No such [File or Directory]")

except IndexError:
   print("No argument Given")

except Exception as e:
  print ("\nError: ", e ,'\n')
  # print ("No File Specified !!")
  # print ("For shell use --shell")
  # os.system(f"python {__path}/shell.py")
