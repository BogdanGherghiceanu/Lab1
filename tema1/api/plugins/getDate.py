import datetime

def get_date():
    todayDate=datetime.datetime.now()
    formatDate=str(todayDate.year)+"-"+str(todayDate.month)+"-"+str(todayDate.day)
    return formatDate
def get_date_now():
    todayDate = datetime.datetime.now()
    formatDate = str(todayDate.year) + "-" + str(todayDate.month) + "-" + str(todayDate.day) + " " +str(todayDate.hour) +" " +str(todayDate.second)
    jsonData={
        "data": formatDate
          }
    print(jsonData)
    return jsonData