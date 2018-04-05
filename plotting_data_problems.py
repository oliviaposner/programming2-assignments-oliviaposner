import csv
import matplotlib.pyplot as plt



# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors (15pts)
# open and read in the "Libraries_-_2018_Visitors_by_Location.csv" file into a list (use file located in the file folder, read in using csv library).
# calculate (and make a list of) the total visitors to Chicago libraries each month.  
# Do not plot every library individually.  Instead, find the total for all libraries each month and plot that.
# Make a BAR GRAPH with the total visitors on the y and month on the x.  
# label the x with the month.  Rotate the text so we can read it.  (see example problem).  Use the tight_fit command to show all text.
# label axes, title the graph as necessary.

with open("files/Libraries_-_2017_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

month_numbers = [x for x in range(12)]
print(month_numbers)

month_names = data[0][1:-1]
print(month_names)




jan = [x[1] for x in data][1:]
jan = [int(x) for x in jan]
print(sum(jan))

feb = [x[2] for x in data][1:]
feb = [int(x) for x in feb]
print(sum(feb))

mar = [x[3] for x in data][1:]
mar = [int(x) for x in mar]
print(sum(mar))

apr = [x[4] for x in data][1:]
apr = [int(x) for x in apr]
print(sum(apr))

may = [x[5] for x in data][1:]
may = [int(x) for x in may]
print(sum(may))

jun = [x[6] for x in data][1:]
jun = [int(x) for x in jun]
print(sum(jun))

jul = [x[7] for x in data][1:]
jul = [int(x) for x in jul]
print(sum(jul))

aug = [x[8] for x in data][1:]
aug = [int(x) for x in aug]
print(sum(aug))

sept = [x[9] for x in data][1:]
sept = [int(x) for x in sept]
print(sum(sept))

oct = [x[10] for x in data][1:]
oct = [int(x) for x in oct]
print(sum(oct))

nov = [x[11] for x in data][1:]
nov = [int(x) for x in nov]
print(sum(nov))

dec = [x[12] for x in data][1:]
dec = [int(x) for x in dec]
print(sum(dec))

visitors = [sum(jan), sum(feb), sum(mar), sum(apr), sum(may), sum(jun), sum(jul), sum(aug), sum(sept), sum(oct), sum(nov), sum(dec)]

plt.bar(month_numbers, visitors)

plt.xticks(month_numbers, month_names, rotation=45, color="red")

plt.figure(1, figsize=(-10, 20), tight_layout=True, facecolor="yellow")
# plt.bar(month_numbers, month_names, color='red')
plt.title("Usage of Chicago Libraries Per Month - 2017", color="red")
plt.ylabel("Computer Users", color="red")




# MATPLOTLIB PROBLEM # 2 
# Chicago Public Transit Usership Graph (20pts)
# go to https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
# download the CTA ridership data as a csv.
# Read the data into a list using the csv library.
# Make a plot of paratransit, bus, rail, and total numbers by year (all on the same graph).
# Make each line, points, and color different for the four graphs.
# Make a legend to identify each line.
# Label axes and give your graph a title.  Change it in any other way you see necessary to give it a clean look.

with open("search_files/CTA_-_Ridership_-_Annual_Boarding_Totals.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)



year_names = [x[0] for x in data][1:]
print(year_names)

year_numbers = [x for x in range(len(year_names))]
print(year_numbers)



bus = [x[1] for x in data][1:]
bus = [int(x) for x in bus]

paratransit = [x[2] for x in data][1:]
paratransit = [int(x) for x in paratransit]

rail = [x[3] for x in data][1:]
rail = [int(x) for x in rail]

total = [x[4] for x in data][1:]
total = [int(x) for x in total]

plt.figure(2, tight_layout=True)

plt.plot(year_numbers, bus, label="Bus")
plt.plot(year_numbers, paratransit, label="Paratransit")
plt.plot(year_numbers, rail, label="Rail")
plt.plot(year_numbers, total, label="Total")
plt.xticks(year_numbers, year_names, rotation=45)

plt.legend(bbox_to_anchor=(0, 1), loc="upper left")
plt.xlabel("Years")
plt.ylabel("Transit Boarding Totals")
plt.title("CTA Ridership Annual Boarding Totals")


plt.show()