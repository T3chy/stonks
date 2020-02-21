import csv
from datetime import date
def addtrade():
        ticker = ""
        conf = ""
        print('add has been called')
        while ticker == "":
                ticker = input('''ticker?
''').strip('$')
        currentprice = 1 #si.get_live_price(ticker)
        print("the current price for " + ticker + " is $" +str(currentprice))
        while conf == "":
                conf = input('''does this look right? y/n
''')
        if conf == "n":
                price = input('''please input the price you bought at
''').strip('$')
        else:
                price = currentprice
        countshares = input('''how many shares did you purchase?
''')
        pdate = input("""what date was the trade completed?(mm/dd/yy) press enter to use today's date 
""")
        if pdate == '':
                pdate = date.today().strftime('%m/%d/%y')
        tcost = '$'+str(float(price)*float(countshares))
        if len(ticker) == 1:
                tspaces = "      "
        elif len(ticker) == 2:
                tspaces = "     "
        elif len(ticker) == 3:
                tspaces = "    "
        elif len(ticker) == 4:
                tspaces = "   "
        elif len(ticker) == 5:
                tspaces = "  "
        print(""" 
Ticker | Price | Shares | Total Cost
------------------------------------
""" 
+ ticker + tspaces + "|  " + str(price) + "   |   " + countshares + "   |    " + str(tcost))
        fconf = input('''does this look right? y/n
''')
        if fconf == 'y':
                tradeinfo = [pdate,'$'+ticker,countshares,'$'+price,tcost]
                with open(r'transactions.csv', 'a') as f:
                     writer = csv.writer(f)
                     writer.writerow(tradeinfo)
                print('Trade Recorded! Exiting...')
        else:
	        print('Ok! Exiting without recording trade...')
def viewtrades():
	print('viewtrades has been called')
def viewportfolio():
	print('viewportfolio has been called')
def info():
	print('info has been called')

