from yahoo_fin import stock_info as si 
import csv
def add(ticker):
	while ticker == "":
		ticker = input("ticker?")
	currentprice = si.get_live_price(ticker)
	print("the current price for " + ticker + " is " +str(currentprice))
	while conf == "":
		conf = input("does this look right? y/n")
	if conf == "n":
		price = input("please input the price you bought at")
	else:
		price = currentprice
	countshares = input("how many shares did you purchase?")
	print(""
Ticker | Price | Shares
----------------------"" 
+ ticker + " | " + price + " | " countshares)
#	with open(r'idscores.csv', 'a') as f:
#		writer = csv.writer(f)
#		writer.writerow(keyandscores)
choice = ""
while 'TRUE' == 'TRUE':
	choice = input("""
Welcome to Elam's Portfolio! Please select a function :)
--------------------------------------------------------
Add a trade	View Trades	View Portfolio    View Information on a Stock
[add]		[viewtrades]	[viewportfolio]		    [info]
Your Selection:""")
	if choice == "add":
		break
	if choice == "viewtrades":
		break
	if choice == "viewportfolio":
		break
if choice == "add"

