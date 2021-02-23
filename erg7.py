import urllib.request
import json
import datetime

d_date = datetime.date.today()
d_day = d_date.day
d_month = d_date.month
d_year = str(d_date.year)
if len(str(d_month)) == 1:
    d_month = "0" + str(d_month)
else:
    d_month = str(d_month)

for i in range(1, d_day+1):
    #Τα σημερινά νούμερα δεν παραμένουν σταθερά
    if i == d_day:
        extra = " (Όχι Τελικό)"
    else:
        extra = "\n"
    freq = [0] * 100
    if len(str(i)) == 1:
        date = d_year+"-"+d_month +"-0"+ str(i)
    else:
        date = d_year+"-"+ d_month +"-" + str(i)
    url = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + date + "/" + date
    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    data = json.loads(html,strict=False)
    for draw in data["content"]:
        for n in range(20):
            freq[draw["winningNumbers"]["list"][n]-1] += 1
    maxn = max(freq)
    print ("Συχνότερος αριθμός για " + date + ": " + str(freq.index(maxn)+1) + extra)
