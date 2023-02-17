#Name: Zac Konrad
#This program converts miles to kilometers
#Miles can be input to one decimal point and
#answer in kilometers will be up to 2 decimal points

def main ():
    #display the intro screen.
    intro()
    try:    
  
  # Get the number of miles driven in the vehicle with up to 
  # one max decimal point.
      miles_drove = float(input('Enter the number of miles drove: '))

  # Convert the miles to kilometers.
      miles_to_kilometers(miles_drove)

    except:
      print("An execption occurred, try entering a number with one decimal point max")
      print()
      main()

  # The intro function displays an introductory screen to 
  # explain and give information.
def intro():
    print('This program converts distances')
    print('in miles to kilometers. For your')
    print('reference the formula is:')
    print('1 miles = 1.6 kilometer')
    print()
  
  # The mile_to_kilometers function accepts a 
  # whole number with one max decimal point
  # of miles and displays the number of kilometers
  # to whole number and one place decimel point.
def miles_to_kilometers(miles):
  kilometers = miles * 1.6
  print('That converts to', kilometers,'kilometers.')

  #Call the main function.
main()