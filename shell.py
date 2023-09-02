from lexer import Lexer
from parse import Parser
from interpreter import Interpreter
from data import Data
from files import get
import readline, os

base = Data()
print("This is Official Penda language interpreter!!")
print()


try:
   while True:
       text = input("penda>>> ")
       if text == "exit":
          print("\n Shell Exited!!")
          exit(0)
       if text == "help":
          get.help()
       if text != "":
           tokenizer = Lexer(text)
           tokens = tokenizer.tokenize()
           parser = Parser(tokens)
           tree = parser.parse()

           interpreter = Interpreter(tree, base)
           result = interpreter.interpret()
           if result is not None:
              print (result)
           else:
              print ("\nInvalid Syntax:")
              print (text)
              print ()
              pass

except Exception as e:
  pass
  print ()
  print (e)

except KeyboardInterrupt:
  print ("\n\nStopping..")
  pass
