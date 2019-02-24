import csv
import datetime
import os

# Settings
filename = 'n26-csv-transactions.csv'
totalBalance = 0
initialDate = ''
endDate =  ''
header = True
showDetails = False

filename = input('Nome del file [n26-csv-transactions.csv]: ')
if filename == '':
    filename = 'n26-csv-transactions.csv'

h = input ('Prima riga con intestazioni [S]: ')
header = (h == 'S' or h == 's' or h == '')
    
tb = input('Saldo iniziale [0]: ')
if tb == '':
    totalBalance = 0
else:
    totalBalance = int(tb)

id1 =  str(datetime.datetime.now().year - 1) + '-01-01'
id = input ('Data iniziale [' + id1 + ']: ' )
if id == '':
    initialDate = id1
else:
    try:
        datetime.datetime.strptime(id, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Inserire la data nel formato YYYY-MM-DD")
    initialDate = id

ed1 = str(datetime.datetime.now().year - 1) + '-12-31'
ed = input ('Data finale [' + ed1 + ']: ' )
if ed == '':
    endDate = ed1
else:
    try:
        datetime.datetime.strptime(ed, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Inserire la data nel formato YYYY-MM-DD")
    endDate = ed

d = input ('Mostra i dettagli dei movimenti [S]: ')
showDetails = (d == 'S' or d == 's' or d == '')


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

    if row[0] > endDate:
        break

    if row[0] < initialDate:
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

print ("-----")

input ('Premi invio per chiudere')