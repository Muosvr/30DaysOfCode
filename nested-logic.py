labels = ["day", "month", "year"]
date_returned = {x:int(y) for x,y in zip(labels,input().split(" "))}
date_due = {x:int(y) for x,y in zip(labels, input().split(" "))}

year_difference = date_returned["year"] - date_due["year"]
month_difference = date_returned["month"] - date_due["month"]
day_difference = date_returned["day"] - date_due["day"]

if year_difference > 0:
    print(10000)
elif month_difference > 0 and year_difference==0:
    print(500*month_difference)
elif day_difference > 0 and month_difference==0 and year_difference==0:
    print(15*day_difference)
else:
    print(0)
