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
        try:
                currentprice = round(si.get_live_price(ticker),2)
        except Exception as e:
                print('getting live price failed')
                price = input('''please input the price you bought at
''').strip('$')
        else: 
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
#make this not enter if does this look right says no 
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
               writer = csv.writer(open('portfolio.csv', 'a'))
               writer.writerow(tradeinfo)
def viewtrades():
        print('viewtrades has been called')
        with open("transactions.csv") as trans:
                reader = csv.reader(trans)
                for row in reader:
                        print(" ".join(row))

def viewportfolio():
        print('viewportfolio has been called')
        with open("portfolio.csv") as pp:
                reader = csv.reader(pp)
                for row in reader:
                        print(" ".join(row))
        conf = input("view unrealized gains/losses on a position? y/n")
        if conf == 'y':
                ticker = input("ticker? input 'total' for all unrealized gains/losses").strip('$')
                with open('portfolio.csv') as tt:
                        reader = csv.reader(tt)
                        for row in reader:
                              if row == " ":
                                    continue
                              print(row[0])
                              if row[0] == '$'+ticker:
                                    ugl = float((float(float(si.get_live_price(row[0].strip('$')))*float(row[2].strip('$'))))-float(row[1].strip('$')))
                                    if ugl < 0:
                                           gl = 'losses'
                                    elif ugl > 0:
                                           gl = 'gains'
                                    print('Unrealized '+gl+' for '+row[0]+' are '+'$'+str(round(abs(ugl),2)))
def info():
        print('info has been called')
        ticker = input('ticker?')
        print(get_analysts_info(ticker)) 
