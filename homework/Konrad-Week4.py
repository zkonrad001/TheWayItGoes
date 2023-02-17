#Name: Zac Konrad

print ("Welcome to Fiber 4 U")

company_name = input("Please enter your company Name: ")

feet_of_cable = input("Please enter the number of feet of cable: ")


feet_of_cable = float(feet_of_cable)
cost_of_cable = feet_of_cable * .87

if feet_of_cable > 100 and feet_of_cable <= 250:
  print("Cost of cable is $.80 per foot")
elif feet_of_cable >250 and feet_of_cable <= 500:
  print("Cost of cable is $.70 per foot")
elif feet_of_cable >500:
  print("Cost of cable is $.50 per foot")

message = "The cost is: " + str(cost_of_cable)

print(message)

message1 = "Thank you for shopping with us " + str(company_name)

print(message1)