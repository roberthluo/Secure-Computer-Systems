import os
import sys

file_list = []
virus_definition = ""

def read_virus_definition():
  virus_definition_file = ""
  global virus_definition
  f = open(virus_definition_file, 'r')
  virus_definition = f.read()
  
  
def check_file(file_path):
  
  
  #deactivate virus
  virus_file = open(file_path, 'w')
  
  return true


def virus_scan(root_path):
  global file_list
  for path, subdirs, files in os.walk(root_path):
    for name in files:
       file_path = os.path.join(root_path, name)
       print file_path
       if(check_file(file_path)):
          file_list.append(file_path) 

def quarantine_files():
  quarantine_directory = ""
  global file_list
  for f in file_list:
    os.rename(f, quarantine_directory)
    
  

if __name__ == "__main__":
  read_directory("/directory")
