import os
import sys
import pandas as pd
# I chose a data set for past himalayan expeditions

def check_csv_exists(csv) -> bool: # function for checking if the csv I want to access exists in CWD

  for item in os.scandir(): # use the scandir() function from the os module to scan the CWD
    if item.is_file() and (item.name == csv): # verify if the scanned item is a file
      return True
  
  print("An error has occured: csv provided doesn't exist in current working directory") # just for informing the user they've made an oopsie
  return False

def totalRecords(file_name) -> int:
  file = open(file_name) # open expedition csv in current working directory
  nextRec = True  

  records = 0 # initialize the variable

  while nextRec: # use a while loop to go through the records
    recLine = file.readline()
    records += 1

    if '' == recLine:
      nextRec = False

  file.close()
  return records


#Outputs

def main() -> int: # created a main function as my entry point using ints as the return type
  user_input = input("Enter csv name: ") # this is for my own reusability and so I don't have to input the csv file name in code
  
  try:
    if check_csv_exists(user_input):
      print(f"total records found for '{user_input}': {totalRecords(user_input)}") # function call to fetch total records
      return 0
  except Exception as error: # using the built-in exceptions for describing what error im getting (work-in-progress)
    print(f"An error has occured: {error}") # for when the error isn't related to check_csv_exists() function

  return 1 # lonely 1 for when an error has occured

if __name__ == "__main__":
  sys.exit(main())



