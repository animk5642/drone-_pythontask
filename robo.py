import os

# This tells Python to talk to your computer and create a new folder


if __name__=='__main__':

  while True:
      command= input("enter the thing you need to speak")
      if command =="q":
         break
      os.system(f'espeak " {command}"') 