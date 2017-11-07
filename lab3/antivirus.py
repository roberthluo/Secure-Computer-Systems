import os
import sys
import ntpath

file_list = []
virus_definition = ""

def read_virus_definition(virus_definition_file):
  global virus_definition
  with open(virus_definition_file, "rb") as f:
    virus_definition = f.read()
    virus_definition = virus_definition.rstrip('\n')
    print("Virus signature is:", virus_definition)
  
def check_file(file_path):
  global virus_definition
  is_infected = False

  neutralized_text = ""
  #deactivate virus
  print(file_path)

  with open(file_path, 'rw') as f:
    global virus_definition
    text = f.read()
    print("file text:", text, " virus definition", virus_definition)
    if virus_definition in text:
      print("neutralizing the virus")
      neutralized_text = text.replace(virus_definition, "xxxxxxxx")
      print("neutralized the virus", text)
      is_infected = True
    else:
      print("This file is not infected.")
      return False

  # Safely write the changed content, if found in the file
  with open(file_path, 'w') as f:
      f.write(neutralized_text)
  return True

def virus_scan(root_path):
  global file_list
  for path, subdirs, files in os.walk(root_path):
    for name in files:
       file_path = os.path.join(root_path, name)
       print file_path
       if(check_file(file_path)):
          file_list.append(file_path)

  quarantine_files("/home/robert/Git/Secure-Computer-Systems/lab3/quarantined_folder") 

def quarantine_files(quarantine_directory):
  global file_list
  print("new quarantine directory", quarantine_directory)
  for f in file_list:
    head, tail = ntpath.split(f)
    quarantine_file = quarantine_directory +"/" + tail
    print("New Path", quarantine_file)
    os.rename(f, quarantine_file)
    print("Finished quarantine of infected file:", f)

if __name__ == "__main__":
    #Reading current directory
    read_virus_definition("virus_definition")
    virus_scan("/home/robert/Git/Secure-Computer-Systems/lab3/scanning_folder")
    #quarantine_files("/home/robert/Git/Secure-Computer-Systems/lab3/quarantined_folder")
