import datetime
s = "17 Apr"
print(datetime.datetime.strptime("{0} 2023".format(s), "%d %b %Y").strftime("%Y-%m-%d"))