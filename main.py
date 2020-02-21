#from yahoo_fin import stock_info as si 
import actionz as a
import csv
#	with open(r'idscores.csv', 'a') as f:
#		writer = csv.writer(f)
#		writer.writerow(keyandscores)
choice = " "
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
	if choice == "info":
		break
if choice == "add":
	a.addtrade()
elif choice == "viewtrades":
	a.viewtrades()
elif choice == "viewportfolio":
	a.viewportfolio()
elif choice == "info":
	a.info()
