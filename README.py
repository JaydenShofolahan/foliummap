#Name: Jayden Shofolahan 
#Date: 11/14/24
#Description: This program will take a csv file from the user and mark all of the traffic collisions 

import folium 
map_user = input("Enter a csv file") 
outFile = input("Enter an outfile") 
map_final = folium.Map(
