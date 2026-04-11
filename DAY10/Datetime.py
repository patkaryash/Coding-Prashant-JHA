import datetime
#datetime formatting
date= datetime.datetime.now()
print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))