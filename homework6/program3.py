# Prompt user to enter a start path and file name, search recursively for the given file name starting at the given path, when file is found, display the full path to the file. 
import os

def search_file(file_name, start_path):
   file_found = []

   for root, dir, files in os.walk(start_path):
      if file_name in files:
         file_found.append(os.path.join(root, file_name))
   return file_found

start_path=input("Enter a start path : ")
file_name=input("Enter file name : ")
print(search_file(file_name,start_path))
