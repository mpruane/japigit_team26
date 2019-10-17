#Project 5
#Created by Michael Ruane
#Purpose: Showcases Writing Out Files and using the libraries urllib and json to grab information from an API and processing it
#File: japi.py
#Description: Main File - output is in japi.out

import urllib
import json

def getStockData(stockSym):
	mURL = "https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=" + stockSym + "&apikey=LZHMVTZEAJSOYY6V"
	connection = urllib.urlopen(mURL)
	return connection.read().decode()

def main():
	f = open("japi.out", "w")
	print 'Type "quit" to end program'
	uInput = ""
	while (True):
		uInput = raw_input("Enter Stock Symbol: ")
		if uInput == "quit":
			break
		stockInfo = getStockData(uInput)
		stockDict = json.loads(stockInfo)
		#Stock Quotes is translated into a list with a dictionary inside, so i removed the list since it was redundent
		stockDict['Stock Quotes'] = stockDict['Stock Quotes'][0]
		#Printing to screen
		print "------------------------------------------------------------------------"
		print "JSON Formatted Response:                                               |"
		print "------------------------------------------------------------------------"
		print stockInfo
		print "------------------------------------------------------------------------"
		print "The current price of " + stockDict['Stock Quotes']['1. symbol'] + " is: $" + stockDict['Stock Quotes']['2. price']
		print "------------------------------------------------------------------------"
		#Printing to file
		f.write("------------------------------------------------------------------------\n")
		f.write("JSON Formatted Response:                                               |\n")
		f.write("------------------------------------------------------------------------\n")
		f.write(stockInfo + "\n")
		f.write("------------------------------------------------------------------------\n")
		f.write("The current price of " + stockDict['Stock Quotes']['1. symbol'] + " is: $" + stockDict['Stock Quotes']['2. price'] +"\n")
		f.write("------------------------------------------------------------------------\n\n")
	f.close()

if __name__== "__main__":
  main()