#ZAC KONRAD
#Assignment 8.1   

#Vehicle is the base class
class vehicle:

    def setVehicle_Class(self, type):
      self.Vehicle_Class = type

    def setVehicle_Make(self, make):
      self.Vehicle_Make = make

    def setVehicle_Model(self, model):
      self.Vehicle_Model = model

    def GetVehicle_Class(self, type):
      print(f"The vehicle class is:{self.Vehicle_Class}")

    def GetVehicleMake(self):
      print(f"The make of the vehicle is: {self.Vehicle_Make}")

    def GetVehicleModel(self):
      print(f"The model of the vehicle is: {self.Vehicle_Model}")

#Car inherits from vehicle
class car(type):

    #set number of car doors
    def CarDoor(self, Number):
        self.CarDoor = Number
    
    #display the number of doors
    def GetVehicleMake(self):
        print(f"The vehicle type is: {self.vehicle_type}")
        print(f"The make to the vehicle is: {self.Vehicle_Make}")
    def GetVehicleModel(self): 
      print(f"The model of the vehicle is:{self.Vehicle_Model}")
    def GetCarDoor(self):
        print(f"The number of car doors is:{self.CarDoor}")
      
      
#Pickup inherits from vehicle
class pickup(type):

    #Set the pickup bed length
    def BedLength(self, Length):
        self.BedLength = Length

    #display the bed lenght
    def GetVehicleMake(self):
        print(f"The vehicle type is: {self.vehicle_type}")
        print(f"The make to the vehicle is: {self.Vehicle_Make}")
    def GetVehicleModel(self): 
      print(f"The model of the vehicle is:{self.Vehicle_Model}")
    def GetBedLength(self):
      print(f"The bed length of the pickup is:{self.BedLength}")

      
input_class = input("Please enter your verhicle class:")
input_make = input("Please enter the vehicle make:")
input_model = input("Please input the vehicle model: ")
input_number = input("Please input the number of car doors:")
input_length = input("Please input the lenght of pickup bed:")
new_vehicle = vehicle()
new_vehicle.set(input_model)
new_vehicle.set(input_make)
new_vehicle.set(input_model)
new_vehicle.set(input_number)
new_vehicle.set(input_length)
new_vehicle.GetVehicle_Class()
new_vehicle.GetVehicleMake()
new_vehicle.GetVehicleModel()
new_vehicle.GetCarDoor()
new_vehicle.GetBedLength()








































  ##strModel = input ("Please enter the pickup model:")

#new_pickup.setModel(strModel)
  ##strDoors = input("Please enter the bed length:")

#new_pickup.setBedLength(strDoors)
 ## print("")
## print(f"The bed lenght is:{new_pickup.getBedlength()}")
 ## print(f"The make is:{new_pickup.getMake()}")
#print(f"The model is")