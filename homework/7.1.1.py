#ZAC KONRAD
#Assignment 7.1     

main()
def main ():
    #display the intro screen.
    intro()
    try:    
  
  # Get the stock ticker symbol.
      stock_symbol = int(input('Enter the stock ticker symbol: '))

    except:
      print("An execption occurred, try again by entering a stock ticker symbol in the dictionary")
      print()
      main()

stocks_dict = {
    "AML":"21.12",
    "TEX":"50.05",
    "DET":"12.58",
    "ARI":"66.66",
    "BRT":"65.21",
    "LMN":"48.35",
    "SUV":"78.55",
    "EMT":"12.02",
    "TIM":"58.22",
    "PIP":"99.99",
}


stock = stocks_dict.get(stock_symbol,'Symbol not found try again')
try:
  print("The price is: ",(stock))
except:
  print("Symbol not found.")
  print("Please try a different symbol")
