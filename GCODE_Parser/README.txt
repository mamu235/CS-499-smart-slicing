Smart Slicing: G-Code Post-Processing Script

This script is designed to take a gcode file and introduce Non-Planar printing into the object.

---------------------------------------------------
        	Non-Planar Printing
---------------------------------------------------
In order to explain Non-Planar printing, traditional 3-D printing must be described. In traditional 3-D printing, a 3-D object is sliced into thin, equal layers, which are parallel to the printing plane. Using this process, if a user wants to print a triangular prism the slope of the prism will have clearly defined edges where one layer extends outward, in comparison to the layer printed after it. This will lead to an object that is more of a staircase rather than a smooth ramp. The "stair-step" effect is an undesirable side-effect of traditional printing.

Most modern slicing programs allow the user to define the thickness of all of the layers, and some are using a new technique called adaptive slicing. This technique analyzes the object as a whole and slices based on the slope of the shell. If the shell is more perpendicular to the printing plane, then it will use a thicker layer, while a more sloped shell will have a thinner layer. This technique will create smoother, and stronger object. However, this technique will still slice the object into layers that are parallel with the printing plane, and it only dampens the stair-step.  

Non-Planar printing is the idea that the object can be printed with layers that have a 3rd dimension. This will allow users to create objects that curve rather than hard edges. This can eliminate the stair-stepping that occurs in other printing techniques. We have implemented this technique by varying the Z dimension, and the extrusion amount in the gcode. 


---------------------------------------------------
        	  Gcode Parser
---------------------------------------------------
Using python version _._, we created a script that will open, read, and modify a pre-sliced object. The first version of this script was designed specifically for introducing sinusoidal waves into a small cube that has a full fill pattern. Upon confirming the script fulfills the desired outcomes (listed below), the parser will need to be modified to accommodate other types of objects. 


---------------------------------------------------
        	     Objectives
---------------------------------------------------
The overall object of this parser is to implement Non-Planar printing. However, certain group-imposed restrictions created specific objectives. 

* To create a small cube were, layer by layer, sinusoidal waves were introduced into the layers, building up the amplitude to its peak in the center of the cube, and then to slowly dampen the waves out, to create a flat cube. 
* In theory these waves will strengthen the strength of the object, and will lay the framework for create objects with printed cubes. This objective will be tested once the parser has been completed. 
