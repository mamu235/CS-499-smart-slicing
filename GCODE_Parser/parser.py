# 3D Printing GCODE Parser

# Purpose: This Python script is for parsing 3D printing GCODE in order to apply a sinusoidal fill pattern to a test cube for a CS 499 Senior Design Project at the University of Kentucky

# Authors: Christopher Guallpa, Mitch Mullins, Robert Williams
# Date: 4/1/2018

import array

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
  if lower == 0:
    print("The Lower layer cannot be 0, as it is a protected Layer")
    return -1
  # Checking to guard against protected upper layer maniuplation
  upper = lower + 2
  if upper == max(data)+1:
    print("The upper layer cannot be manipulated as it is a protected layer")

# Main Fucntion
def main():
  # Getting the File Path
  print("Please enter the URL path of the GCODE file you wish to adjust")
  URL = input(" : ")
  # Variable for GCODE contents
  data = []
  data = readIn(URL)


  

main()
