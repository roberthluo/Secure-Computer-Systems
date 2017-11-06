import os
import sys

file_list = []


def read_directory(root_path):
  global file_list
  for path, subdirs, files in os.walk(root_path):
    for name in files:
       print os.path.join(root_path, name)
       file_path = os.path.join(root_path, name)
       file_list.append(read_path) 




if __name__ == "__main__":
  read_directory("/directory")
