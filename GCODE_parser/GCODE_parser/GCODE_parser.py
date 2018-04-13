# 3D Printing GCODE Parser

# Purpose: This Python script is for parsing 3D printing GCODE in order to apply a sinusoidal fill pattern to a test cube for a CS 499 Senior Design Project at the University of Kentucky

# Authors: Christopher Guallpa, Mitch Mullins, Robert Williams
# Date: 4/1/2018

import array

URL = r'C:\Users\Mitch\source\repos\CS-499-smart-slicing\GCODE_parser\24x24x24cube_comments.gcode'

# Function: readIn() - This function reads in the data of a GCODE file
def readIn(URL):
  # Reading In the GCODE file by line
  with open(URL) as f:
    lines = f.readlines()

  return lines

# Function: maxLayer() - This will Identify the number of layers of the print
def maxLayer(data):
  # Setting the Keyword
  keywrd = ';Layer count:'
  max = 0
  # iteration through the data to find the Keyword
  for i in range(0,len(data)):
    if data[i][0:13] == keywrd:
      # Assuming that the # of layers will fit in 3 digits we have an option for detecting the 3 digit number and calculationg it vs our normal case of 2 digits
      if data[i][-4] != ' ':
        max += int(data[i][-4])*100
        max += int(data[i][-3])*10
        max += int(data[i][-2])*1
      else:
        max += int(data[i][-3])*10
        max += int(data[i][-2])*1
      # Desired return outcome
      return max
  # Returning an error code of -1 if the above return doesn't work
  return -1

# Function: layerID() - This function will find the GCODE keyword 'LAYER' and return the Indicies of the Layer Commands
#   Parameters: data - which is where all of the GCODE is stored, lower - the lower layer to ID indicies
def layerID(data, lower):
  # Checking to guard against protected layer manipulation
  if lower < 2:
    print("The Lower layer cannot be 0 or 1, as they are protected Layers!")
    return -1
  # Checking to guard against protected upper layer maniuplation
  keywrd = '; move to next layer ('
  counter = 0
  for i in range(0,len(data)):
    for j in range(0, len(data[i])):
      if data[i][j:j+22] == keywrd:
        layer = str(counter)
        print(layer)
        counter += 1
  return

# Function: extrusionID() - This function will find the Indicies of the Extrusion value
#   Parameters: data - which is where all of the GCODE is stored, line - the line to ID indicies
def extrusionID(data, line):
  count = 0
  while count == 0:
    if data[line][i] == ' ':
      if data[line][i+1] == 'E':
        if data[line][i+2] == ':':
          count = i+3
        else:
          count = 0
      else:
        count = 0
    else:
      count = 0

  return count

def layerFlip():

  return

# Main Fucntion
def main():
  # Getting the File Path
  print("Starting Processing of file: ")
  print(URL)
  print()
  # Variable for GCODE contents
  data = []
  data = readIn(URL)

  layerID(data, 2)
  

main()

