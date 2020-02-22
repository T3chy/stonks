import csv
from datetime import date
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import get_analysts_info
def addtrade():
        ticker = ""
        conf = ""
        print('add has been called')
        while ticker == "":
                ticker = input('''ticker?
''').strip('$')
        currentprice = round(si.get_live_price(ticker),2)
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
                pdate = str(pdate)
                ticker = '$'+str(ticker)
                countshares = str(countshares)
                price = '$'+str(price)
                tcost = str(tcost)
                tradeinfo = [pdate,ticker,countshares,price,tcost]
                with open(r'transactions.csv', 'a') as f:
                     writer = csv.writer(f)
                     writer.writerow(tradeinfo)
                print('Trade Recorded! Exiting...')
        else:
	        print('Ok! Exiting without recording trade...')
        again = input('add another trade? y/n')
        while again == 'y':
                addtrade()
                again = input('add another trade? y/n')
                if again == 'n':
                      break
        print('updating portfolio...')
        r = csv.reader(open(r'portfolio.csv'))
        lines = list(r)
        if ticker in lines:
                for i in sum(1 for row in lines):
                      if i == ticker:
                           lines[i][1] = p[i][1] + tcost
                           lines[i][2] = p[i][2] + countshares
                           writer = csv.writer(open('portfolio.csv', 'w'))
                           writer.writerows(lines)
        else:
               tradeinfo = [ticker,tcost,countshares]
               writer = csv.writer(open('portfolio.csv', 'w'))
               writer.writerow(tradeinfo)
def viewtrades():
        print('viewtrades has been called')
        with open("transactions.csv") as trans:
                reader = csv.reader(trans)
                for row in reader:
                        print(" ".join(row))

def viewportfolio():
        print('viewportfolio has been called')
	#lmao actually write this
def info():
        print('info has been called')
        ticker = input('ticker?')
        print(get_analysts_info(ticker)) 
