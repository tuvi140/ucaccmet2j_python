import json
import csv
res = {}

#making the stations dictionaries!!
with open ('stations.csv') as file:
    stations= list(csv.DictReader (file))
print (stations)

with open ('precipitation.json',encoding='utf-8') as file:
    contents= json.load(file)
    
precipitation_info={}

#make sure all the stations have their data !!
for station in stations:
    station_number = station['Station']
    state=station['State']
    city_name=station['Location']

    city_data=[] #cumulativeeeee
    for measurements in contents:
        if (measurements['station'])== station_number:
            city_data.append(measurements)

    #calc by month the prec
    total_monthly_precipitation={}
    for measurement in city_data:
        #separating per month!
        month= (int(measurement['date'].split('-')[1]))#split to isolate the month, choosing it
        precipitation = measurement['value'] #to simplify
        #summing per month 
        if month in total_monthly_precipitation:
            total_monthly_precipitation[month] += precipitation
        else:
            total_monthly_precipitation [month]= 0

    total_yearly_precipitation= sum(total_monthly_precipitation.values())

    #dictionary for the relative precipitations
    relative_monthly_precipitation = {}

    #calculate for the relative precipitations!!
    for month, monthly_total in total_monthly_precipitation.items():
        relative_monthly_precipitation[month] = (
            total_monthly_precipitation[month] / total_yearly_precipitation
        )

    #station results put into the file itselfff
    precipitation_info[city_name]= {
        'station': station_number,
        'state':state,
        'total_monthly_precipitation':list(total_monthly_precipitation.values()),
        'total_yearly_precipitation': total_yearly_precipitation,
        'relative_monthly_precipitation': list(relative_monthly_precipitation.values())
    }


with open ('results.json','w') as file:
    json.dump(precipitation_info,file,indent=4)
