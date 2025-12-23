from datetime import datetime,date,time,timedelta

print(datetime.now())

print(datetime.now()+timedelta(days=7))

formatted = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
year = datetime.now().strftime('%Y')
print("parsed date:",formatted)
print("year",year)

parse = datetime.strptime("2003-06-28",'%Y-%m-%d')
print(parse)