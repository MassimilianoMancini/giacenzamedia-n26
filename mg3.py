import csv
import datetime

# Settings
filename = 'n26-csv-transactions.csv'
totalBalance = 0
initialDate = '2018-03-28'
endDate =  '2019-02-20'
header = True
showDetails = False


file = open(filename)
csv = csv.reader(file, delimiter=',')

date = initialDate
totalNum = 0
dayBalance = 0
totalDays = (datetime.datetime.strptime(endDate, '%Y-%m-%d') - datetime.datetime.strptime(initialDate, '%Y-%m-%d')).days



for row in csv:

    if header:
        header = False
        continue

    if date == row[0]:
        dayBalance += float(row[6])
        continue

    if dayBalance == 0:
        date = row[0]
        dayBalance = float(row[6])
        continue


    d1 = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(date, '%Y-%m-%d')
    days = ( d2 - d1).days
    rowNum = totalBalance * days

    if showDetails:
        print ("%s %8.2f %3d %8.2f" % (date, totalBalance, days, rowNum))

    totalBalance += dayBalance
    initialDate = date
    date = row[0]
    dayBalance = float(row[6])
    totalNum += rowNum
        
d1 = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
d2 = datetime.datetime.strptime(endDate, '%Y-%m-%d')  
days = (d2 - d1).days
rowNum = totalBalance * days
totalNum += rowNum
if showDetails:
    print ("%s %8.2f %3d %8.2f" % (endDate, totalBalance, days, rowNum))
    
print ("-----")
print ("totale numeri: %.3f giorni: %d" % (totalNum, totalDays))
print ("-----")

print("Giacenza media: %.2f" % (totalNum/totalDays))