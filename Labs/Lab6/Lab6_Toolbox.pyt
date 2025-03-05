import arcpy
import time

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"
        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]

class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "graduatedcolor"
        self.description = "Create a graduated color map based on a specific attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define the tool parameters."""
        # Getting the original project name
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name",
            name="aprxInputName",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )

        # Which layer do you want to use as the classification of the graduated color map
        param1 = arcpy.Parameter(
            displayName="Layer Classification",
            name="LayertoClassify",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )
        # Location you would like the file to end up (output location)
        param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputLocation",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )
        # Name of the output file
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # Progressor Variables
        readTime = 3
        start = 0
        max = 100
        step = 33

        # Progressor Setup
        arcpy.SetProgressor("step", "Validating Project File...", start, max, step)
        time.sleep(readTime) # Pauses the execution for 3 seconds as stated above by the readTime variable
        
        arcpy.AddMessage("Validating Project File...")

        # Project File
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)
        
        # Grabs the first instance of a map from the .aprx
        campus = project.listMaps('Map')[0]

        # Processor Increment
        arcpy.SetProgressorPosition(start+step) 
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Finding your map layer...")

        # Loop code for running through the map layers
        for layer in campus.listLayers():

            if layer.isFeatureLayer:  # Checks to see if the layer is a Feature Layer
                # Copy the Symbology from the layer
                symbology = layer.symbology
                # Make sure the symbology has a renderer attribute
                if hasattr(symbology, 'renderer'):
                    # Check the layer name
                    if layer.name == parameters[1].valueAsText: # Check if the layer name matches the input layer

                        # Progressor Increment
                        arcpy.SetProgressorPosition(start+step) # Now it will show 33% complete
                        arcpy.SetProgressorLabel("Calculating and classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")


                        symbology.updateRenderer('GraduatedColorsRenderer') # Update the copy's renderer to "Graduated Colors Renderer"


                        symbology.renderer.classificationField = "Shape_Area" # Telling ArcPy which field we want to base the chloropleth off of

                        # Progressor Increment
                        arcpy.SetProgressorPosition(start+step*2) # Will now show 66% complete
                        arcpy.SetProgressorLabel("Cleaning up...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Cleaning up...")

                        symbology.renderer.breakCount = 5 # This is the amount of classes we want to have for the map


                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0] # Setting the color ramp


                        layer.symbology = symbology # Set layer's actual symbology equal to the copy's

                        arcpy.AddMessage("Finish Genrating Layer...")
                    else:
                        print("NO FEATURE LAYERS FOUND")

        # Progressor Increment
        arcpy.SetProgressorPosition(start+step*3) # Will now show 99% complete
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")

        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx")
        # Parameter 2 is the folder location from earlier
        # Parameter 3 is the name of the new project file from earlier
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and added to the display."""
        return
