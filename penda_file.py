#!/usr/bin/python3.11
# -*- coding: utf-8 -*-

from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data
from files import get
import getopt, sys, os, pathlib

argumentList = sys.argv[1:]
options = "hVf:S"
long_options = ["help", "version", "file", "shell"]

__path = os.getcwd()
base = Data()

try:
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
          
       elif currentArgument is None:
          print("No argument Given")

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

except Exception as e:
  print ("\nError: ", e ,'\n')
  # print ("No File Specified !!")
  # print ("For shell use --shell")
  # os.system(f"python {__path}/shell.py")
