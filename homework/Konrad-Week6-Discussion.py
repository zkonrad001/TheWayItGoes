 #Call the main function.
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

  # The intro function displays an introductory screen.
def intro():
    print('This program converts measurements')
    print('in gallons to fluid liters. For your')
    print('reference the formula is:')
    print(' 1 gallon = 3.78541178 fluid liters')
    print()
  
  # The gallons_to_liters function accepts a whole number of
  # gallons and displays the number of liters to the 8th decimel point.
def gallons_to_liters(gallons):
  liters = gallons * 3.78541178
  print('That converts to', liters, 'liters.')

  #Call the main function.
main()