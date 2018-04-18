# 3D Printing GCODE Parser

# Purpose: This Python script is for parsing 3D printing GCODE in order to apply a sinusoidal fill pattern to a test cube for a CS 499 Senior Design Project at the University of Kentucky

# !!! NOTE !!!
# In order for this program to run correctly, we are assuming a 24mm x 24mm x 24mm cube that was sliced in Slic3r with Verbose Comments (a setting checked within the Program)

# Authors: Christopher Guallpa, Mitch Mullins, Robert Williams
# Date: 4/1/2018

import array
import numpy

URL = r'C:\Users\Mitch\source\repos\CS-499-smart-slicing\GCODE_parser\24x24x24cube_comments.gcode'
writeURL = r'C:\Users\Mitch\source\repos\CS-499-smart-slicing\GCODE_parser\24x24x24cube_comments_modified.gcode'

# Function: readIn() - This function reads in the data of a GCODE file
#   Parameters: URL of Data File

# Status: DONE
def readIn(URL):
  # Reading In the GCODE file by line
  with open(URL) as f:
    lines = f.readlines()
    # Tokenizing each word delimited by blank space
    for i in range(len(lines)):
      lines[i] = lines[i].split(' ')

  f.close()
  return lines

# Function: writeOut() - This function writes the data of a GCODE file
#   Parameters: data - array with the data to be written to a Data File

# Status: DONE
def writeOut(data):
  with open(writeURL, "w") as f:
    for line in range(0,len(data)):
      for i in range(0,len(data[line])):
        if i != len(data[line]):
          f.write(data[line][i])
          f.write(" ")
        else:
          f.write(data[line][i])
  return


# Function: layerID() - This function will find the GCODE keyword 'LAYER' and return the Indicies of the Layer Commands
#   Parameters: data - which is where all of the GCODE is stored

# Status: DONE
def layerID(data):
  # Checking Keywords that ID layer numbers
  keywrd1 = ';'
  keywrd2 = 'move'
  keywrd3 = 'to'
  keywrd4 = 'next'
  keywrd5 = 'layer'
  counter = 0
  # Passing through all lines
  for i in range(0,len(data)):
    # Passing through all words in each line
    for j in range(0, len(data[i])):
      # Checking if the line contains the needed keywords
      if data[i][j] == keywrd1 and data[i][j+1] == keywrd2 and data[i][j+2] == keywrd3 and data[i][j+4] == keywrd5:
        layer = str(counter)
        # Counter for counting number of layers
        counter += 1
  return counter

# Function: layerFlip() - This function will find the first GCODE lines with the keyword '; infill' to get their paths so we can have all layers follow the same path
#   Parameters: data - which is where all of the GCODE is stored, run_length - the number of different layers

# Status: DONE
def layerFlip(data, run_length):
  # Layer Array
  returnLayer = []
  # Keywords for infill layers
  keywrd1 = ';'
  keywrd2 = 'infill\n'
  # Flag to indicate that we have captured  the infill paths of the first layer
  flagwrd1 = ';'
  flagwrd2 = 'move'
  flagwrd3 = 'to'
  flagwrd4 = 'next'
  flagwrd5 = 'layer'
  flagwrd6 = '(1)\n'
  # Passing through all lines
  for i in range(0,len(data)):
    # Checking if the last 2 tokens match those of the infill layers
    if data[i][-1] == keywrd2:
      # Must have this because putting on a single if statement cant handle empty lines
      if data[i][-2] == keywrd1:
        returnLayer.append([data[i][1], data[i][2]])
    if data[i][-1] == flagwrd6:
      if data[i][-2] == flagwrd5 and data[i][-3] == flagwrd4 and data[i][-4] == flagwrd3 and data[i][-5] == flagwrd2 and data[i][-6] == flagwrd1:
        return returnLayer, i

  return -1

# Function: layerReplace() - This function will find the first GCODE lines with the keyword '; infill' to get their paths so we can have all layers follow the same path
#   Parameters: data - which is where all of the GCODE is stored, replacements - the array that contains the X and Y paths to follow, pos - position after which all infill layers need replaced

# Status: IN PROGRESS
def layerReplace(data, replacements, pos):
  # Identifiers for Keywords
  keywrd1 = ';'
  keywrd2 = 'infill\n'

  infill_max = len(replacements)
  infill_index = 0
  for i in range(pos,len(data)):
    if infill_index == infill_max:
      infill_index = 0
    if data[i][-1] == keywrd2:
      if data[i][-2] == keywrd1:
        data[i][1] = replacements[infill_index][0]
        data[i][2] = replacements[infill_index][1]
        infill_index += 1
    else:
        infill_index = 0


  return data

# Main Fucntion
def main():
  # Getting the File Path
  print("Starting Processing of file: ")
  print()
  print(URL)
  print()
  # Variable for GCODE contents
  data = []
  data = readIn(URL)

  run_length = layerID(data)
  print("File Read. There are ", run_length, "layers.")
  print()

  val_array, startRepPos = layerFlip(data, run_length)

  print("Replacing Values:")
  data = layerReplace(data, val_array, startRepPos)
  print()

  print("Values Replaced. Writing to file: ")
  print()
  print(writeURL)
  print()
  writeOut(data)  

  print("Parsing Complete.")
  print()
  print("File,", writeURL, " ready for printing!")
  print()

main()

