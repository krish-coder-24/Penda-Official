from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data
from files import get
import getopt, sys, os, pathlib
from uninstall import Uninstaller

argumentList = sys.argv[1:]
options = "hVf:SUp"
long_options = ["help", "version", "file", "shell", "update", "uninstall", "path"]

__path = os.getcwd()
base = Data()

try:
    if sys.argv[1] == "help":
        get.help()
    if sys.argv[1] == "uninstall":
      if "--full" in sys.argv[2]:
         Uninstaller("Full")
      else:
        Uninstaller("Safe")
        

    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            get.help()
            exit(0)
        elif currentArgument in ("-V", "--version"):
            get.version()
            exit(0)

        elif currentArgument in ("-f", "--file"):
            file_name = str(currentValue)
            file = open(file_name, "r")
            for line in file:
                line = line.strip()
                tokenizer = Lexer(line)
                tokens = tokenizer.tokenize()
                parser = Parser(tokens)
                tree = parser.parse()

                interpreter = Interpreter(tree, base)
                result = interpreter.interpret()
                if result is not None:
                    print(result)

            file.close()

        elif currentArgument in ("-S", "--shell"):
            os.system(f"python {__path}/shell.py")

        elif currentArgument in ("-p","--path"):
            os.getcwd()

        elif currentArgument in ("-U", "--update"):
            if os.path.isfile("/usr/share/penda_pl/penda_file.py"):
                os.system(f"bash /root/.penda/update.sh")
            elif os.path.isfile(
                "/data/data/com.termux/files/usr/share/penda_pl/penda_file.py"
            ):
                os.system("bash ~/.penda/update.sh")
            elif os.path.isfile("C:/Windows/System32"):
                os.system(f"bash {__path}/update.sh")

        elif currentArgument in ("--full"):
            pass


except getopt.error as err:
    err = str(err)
    err = err.replace("option", "")
    if "-f requires argument" in err:
        print("Error:  No file Specified !!")
        print()
    elif "requires argument" in err:
        err = err.replace("requires argument", "")
        print("Error:  Option " + err + " Requires an Argument !!\n")
    elif "not recognized" in err:
        err = err.replace("not recognized", "")
        print("Error:  No such Option: " + err)
        print()
    exit(1)

except FileNotFoundError:
    pass
    print("\nError:  No such [File or Directory]\n")

except IndexError as err:
    print("Error" ,err)
    print("\nNo argument Given")
    print()
    print(
        'Use [ -h or --help ] to see Full help message or Use "man penda" to see Penda manual page'
    )
    print("For file specify '-f' in Argument ..")
    print()

except Exception as e:
    print("\nError: ", e, "\n")
    # print ("No File Specified !!")
    # print ("For shell use --shell")
    # os.system(f"python {__path}/shell.py")
