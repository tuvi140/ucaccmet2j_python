import json
with open('precipitation.json',encoding='utf-8') as file: 
    precipitation=json.load(file)
SEA="GHCND:US1WAKG0038"
CIN="GHCND:USW00093814"
MAU="GHCND:USC00513317"
SAN="GHCND:US1CASD0032"

seattle=[]

for measurement in precipitation :
    if measurement['station'] ==SEA:
        seattle.append(measurement)
#print(seattle)

#get the precipitation per month 
total_monthly_precipitation=[]

seattle_monthly={
    '01': [],
    '02': [],
    '03': [],
    '04':[],
    '05':[],
    '06':[],
    '07':[],
    '08':[],
    '09':[],
    '10':[],
    '11':[],
    '12':[]}

months = ['01', '02', '03','04','05','06','07','08','09','10','11','12']

for measurement in seattle:
    for month in months:
        if measurement['date'].startswith(f'2010-{month}'):
            seattle_monthly[month].append(measurement['value'])


# total_monthly_precipitation=[seattle_monthly]
for month in seattle_monthly:
     total_monthly_precipitation.append(sum(seattle_monthly[month]))

total_yearly_precipitation=[]

with open('results.json', 'w') as file:
    json.dump(total_monthly_precipitation, file, indent=4)

for month in total_monthly_precipitation:
    total


