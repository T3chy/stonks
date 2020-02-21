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
        tcost = '$'+str(int(price)*int(countshares))
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
#       with open(r'idscores.csv', 'a') as f:
#               writer = csv.writer(f)
#               writer.writerow(keyandscores)
def viewtrades():
	print('viewtrades has been called')
def viewportfolio():
	print('viewportfolio has been called')
def info():
	print('info has been called')

