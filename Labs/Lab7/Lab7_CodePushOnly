import arcpy


# Assigning the bands

source = r"C:\TexasA&M_Masters\GitHub\Lamson_online_GEOG676_spring2025\Labs\Lab7\Lab_7_Files"
band1 = arcpy.sa.Raster(source + r"\Band1.TIF")    # Blue
band2 = arcpy.sa.Raster(source + r"\Band2.TIF")    # Green
band3 = arcpy.sa.Raster(source + r"\Band3.TIF")    # Red
band4 = arcpy.sa.Raster(source + r"\Band4.TIF")    # NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")


# Hillshade

azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\DEM.tif", source + r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)


# Slope 

output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\DEM.tif", source + r"\output_Slope.tif", output_measurement, z_factor)

print("Success!!!")