'''
Energy Efficiency of Chicago Schools (35pts)

https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking-2016-Data-Reported-in-/fpwt-snya\

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2016 which was reported in 2017.

We will use this data to look at schools.  We will look to see if 

Make a scatterplot which has the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (15pts)
- Includes ONLY data for K-12 Schools. (2pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 5 highest and 5 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (2pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API. (5pts)


Challenge (for fun):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)

'''

import csv
import matplotlib.pyplot as plt
import numpy as np


with open("search_files/Chicago_Energy_Benchmarking_-_2016_Data_Reported_in_2017.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
schools_to_plot = []

new_data = []
for i in range(len(data)):
    try:
        ghg_intensity = float(data[i][21])
        new_data.append(data[i])
    except:
        pass

data = new_data[:]

for i in range(len(data)):
    if data[i][6] == "K-12 School" and data[i][21] != " ":
            schools_to_plot.append(data[i])

schools_to_plot.sort(key=lambda x: float(x[21]))

print(schools_to_plot)
print(len(schools_to_plot))

ghg_emissions = []
square_footage = []
school_names = []

for i in range(len(schools_to_plot)):
        try:
            emissions = float(schools_to_plot[i][20])
            ghg_emissions.append(emissions)
            footage = float(schools_to_plot[i][7])
            square_footage.append(footage)
            names = schools_to_plot[i][2]
            if names == "Francis W Parker School" or i < 5 or i > (len(schools_to_plot) - 5):
                school_names.append(names)
            else:
                school_names.append("")
        except:
             print(data[i][0], "has no data.")

plt.figure(1, figsize=(12, 7), facecolor="green")

plt.scatter(square_footage, ghg_emissions, s=4, c="yellow", marker='+')
plt.title("Energy Efficiency of Chicago Schools", color='yellow', fontsize=25)
plt.xlabel("School Square Footage", color='yellow')
plt.ylabel("Green House Gas Emissions", color='yellow')

m, b = np.polyfit(square_footage, ghg_emissions, 1) # 1 for linear, returns slope and y intercept

x = [0, 700000]
y = [m * point + b for point in x]
plt.plot(x, y, color='orange')

for i in range(len(school_names)):
    plt.annotate(school_names[i], xy=(square_footage[i], ghg_emissions[i]), fontsize=8) # text, xy =()

plt.show()
