import arcpy

# Set up the Arcpy Environment and workspace
arcpy.env.workspace = r'C:\TexasA&M_Masters\GitHub\Lamson_online_GEOG676_spring2025\Labs\Lab4'
folder_path = r'C:\TexasA&M_Masters\GitHub\Lamson_online_GEOG676_spring2025\Labs\Lab4'
gdb_name = 'lab4.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

# Read the CSV to get the "X" and "Y" data from it
csv_path = r'C:\TexasA&M_Masters\GitHub\Lamson_online_GEOG676_spring2025\Labs\Lab4\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# Code to open the campus Geodatabase and copy the buildings feature class to our Geodatbase
campus = r'C:\TexasA&M_Masters\GitHub\Lamson_online_GEOG676_spring2025\Labs\Lab4\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'
arcpy.Copy_management(buildings_campus, buildings)

# Reprojecting 
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

# Garage Buffers
garage_buffers = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

# Intersection the garage bufferes with the buildings
arcpy.Intersect_analysis([garage_buffers, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

# Intersection Table Output
arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', 'C:\TexasA&M_Masters\GitHub\Lamson_online_GEOG676_spring2025\Labs\Lab4', 'nearbyBuildings.csv')