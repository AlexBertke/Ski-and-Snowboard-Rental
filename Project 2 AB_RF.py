#------------------------------------------------------------------
# Alex Bertke, Robert Firor
# Project 2
# Ski/Snowboard shop
#------------------------------------------------------------------
import datetime
from datetime import datetime, timedelta
import math

class Customer: 
    def __init__(self, Name, ID):
        self.Name = Name
        self.ID = ID
        self.NumberOfSkis = 0
        self.NumberOfSnowBoards = 0 
        self.CuponCode = ''
        self.RentalBasis = 0
        self.RentalTime = 0 
        self.Bill = 0 

    def RequestSkis(self, NumberOfSkis):

         # implement logic for invalid input
        try:
            self.NumberOfSkis = int(NumberOfSkis)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if self.NumberOfSkis < 1:
            print("Invalid input. Number of skis should be greater than zero!")
            return -1
        else:
            self.NumberOfSkis = NumberOfSkis
            global blnInputValidated
            blnInputValidated = True
        return self.NumberOfSkis

    def RequestSnowBoards(self, NumberOfSnowboards):

         # implement logic for invalid input
        try:
            self.NumberOfSnowBoards = int(NumberOfSnowboards)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if self.NumberOfSnowBoards < 1:
            print("Invalid input. Number of Snowboards should be greater than zero!")
            return -1
        else:
            self.NumberOfSnowBoards = NumberOfSnowboards
            global blnInputValidated
            blnInputValidated = True
        return self.NumberOfSnowBoards

    def returnEquipment(self, strTypeOfRental):
        self.strTypeOfRental = strTypeOfRental
        if self.strTypeOfRental == 'skis' or self.strTypeOfRental == 'Skis':
            if self.RentalBasis and self.rentalTime and self.NumberOfSkis and self.CuponCode:
                return self.rentalTime, self.RentalBasis, self.NumberOfSkis, 0, self.CuponCode
            else:
                return 0,0,0,0,''
        elif self.strTypeOfRental == 'snowboards' or self.strTypeOfRental == 'Snowboards':
            if self.RentalBasis and self.rentalTime and self.NumberOfSnowBoards and self.CuponCode:
                return self.rentalTime, self.RentalBasis, 0, self.NumberOfSnowBoards, self.CuponCode  
            else:
                return 0,0,0,0,''
        elif self.strTypeOfRental == "Both" or self.strTypeOfRental == "both":
            if self.RentalBasis and self.rentalTime and self.NumberOfSkis and self.NumberOfSnowBoards and self.CuponCode:
                return self.rentalTime, self.RentalBasis, self.NumberOfSkis, self.NumberOfSnowBoards, self.CuponCode  
            else:
                return 0,0,0,0,''

class Shop: 
    TotalSkisRentedForDay = int(0)
    TotalSnowBoardsRentedForDay = int(0)
    TotalRevenueForDay = int(0)
    def __init__(self, SkiStock=0, SnowBoardStock=0):
        self.SkiStock = SkiStock
        self.SnowBoardStock = SnowBoardStock

    def DisplayStock(self):
        print('We have {} skis and {} snowboards in stock.'.format(self.SkiStock, self.SnowBoardStock))

    def RentSkisOnHourlyBasis(self, n):
        Shop.TotalSkisRentedForDay += int(n)
       
        # reject invalid input 
        if int(n) <= 0:
            print("Number of skis should be positive!")
            return None
        
        elif int(n) > self.SkiStock:
            print("Sorry! We have currently {} skis available to rent.".format(self.SkiStock))
            return None

        # rent the skis        
        else:
            now = datetime.now()                      
            print("You have rented a {} ski(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $15 for each hour per Ski.")
            print("Happy Skiing!")
            self.SkiStock -= int(n)
            return now    

    def RentSkisOnDailyBasis(self, n):
        
        Shop.TotalSkisRentedForDay += int(n)
        # reject invalid input 
        if int(n) <= 0:
            print("Number of skis should be positive!")
            return None
        
        elif int(n) > self.SkiStock:
            print("Sorry! We have currently {} skis available to rent.".format(self.SkiStock))
            return None

        # rent the skis        
        else:
            now = datetime.now()                      
            print("You have rented a {} ski(s) on daily basis today at {} hours.".format(n,now.hour))
            print("You will be charged $50 for each day per Ski.")
            print("Happy Skiing!")
            self.SkiStock -= int(n)
            return now  

    def RentSkisOnDweeklyBasis(self, n):
        Shop.TotalSkisRentedForDay += int(n)
        # reject invalid input 
        if int(n) <= 0:
            print("Number of skis should be positive!")
            return None
        
        elif int(n) > self.SkiStock:
            print("Sorry! We have currently {} skis available to rent.".format(self.SkiStock))
            return None

        # rent the skis        
        else:
            now = datetime.now()                      
            print("You have rented a {} ski(s) on Weekly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $200 for each week per Ski.")
            print("Happy Skiing!")
            self.SkiStock -= int(n)
            return now  

    def RentSnowBoardStockOnHourlyBasis(self, n):
        Shop.TotalSnowBoardsRentedForDay += int(n)
        # reject invalid input 
        if int(n) <= 0:
            print("Number of SnowBoards should be positive!")
            return None
        
        elif int(n) > self.SnowBoardStock:
            print("Sorry! We have currently {} SnowBoards available to rent.".format(self.SnowBoardStock))
            return None
        # rent the SnowBoards        
        else:
            now = datetime.now()                      
            print("You have rented a {} SnowBoard(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $10 for each hour per SnowBoard.")
            print("Happy SnowBoarding!")
            self.SnowBoardStock -= int(n)
            return now   
       
    def RentSnowBoardStockOnDailyBasis(self, n):
        Shop.TotalSnowBoardsRentedForDay += int(n)
        # reject invalid input 
        if int(n) <= 0:
            print("Number of SnowBoards should be positive!")
            return None
        
        elif int(n) > self.SnowBoardStock:
            print("Sorry! We have currently {} SnowBoards available to rent.".format(self.SnowBoardStock))
            return None
        # rent the SnowBoards        
        else:
            now = datetime.now()                      
            print("You have rented a {} SnowBoard(s) on daily basis today at {} hours.".format(n,now.hour))
            print("You will be charged $40 for each day per SnowBoard.")
            print("Happy SnowBoarding!")
            self.SnowBoardStock -= int(n)
            return now   

    def RentSnowBoardStockOnWeeklyBasis(self, n):
        Shop.TotalSnowBoardsRentedForDay += int(n)
        # reject invalid input 
        if int(n) <= 0:
            print("Number of SnowBoards should be positive!")
            return None
        
        elif int(n) > self.SnowBoardStock:
            print("Sorry! We have currently {} SnowBoards available to rent.".format(self.SnowBoardStock))
            return None
        # rent the SnowBoards        
        else:
            now = datetime.now()                      
            print("You have rented a {} SnowBoard(s) on weekly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $160 for each week per SnowBoard.")
            print("Happy SnowBoarding!")
            self.SnowBoardStock -= int(n)
            return now   

    def ReturnEquipment(self, request):
        
        rentalTime, RentalBasis, NumberOfSkis, NumberOfSnowBoards, CuponCode = request
        bill = 0
        
        if rentalTime and RentalBasis and NumberOfSkis or NumberOfSnowBoards and CuponCode:
            print("Thanks for returning your equipment. Hope you enjoyed our service!")
            print("Please Find A Breakdown of Your Bill Below")
            print("Number Of Skis Rented: ", NumberOfSkis)
            print("Number Of SnowBoards Rented: ", NumberOfSnowBoards)
            self.SkiStock += int(NumberOfSkis)
            self.SnowBoardStock += int(NumberOfSnowBoards) 
            Now = datetime.now()
            RentalPeriod = Now - rentalTime
            print("Total Time of Rental: ", RentalPeriod)


            # Ski bill calculation
            # hourly bill calculation
            if RentalBasis == 'Hourly':
                #Check if Greate Than 4 Hours
                if math.ceil(RentalPeriod.seconds) >= 14400:
                    #days
                    bill += math.ceil(RentalPeriod.seconds/86400) * 50 * int(NumberOfSkis)
                else:
                    #Hours
                    bill += math.ceil(RentalPeriod.seconds / 3600) * 15 * int(NumberOfSkis)
                
            # daily bill calculation
            elif RentalBasis == 'Daily':
                #Check if greater than 4 Days
                if math.ceil(RentalPeriod.seconds/86400) >= 4:
                    #Weeks
                    bill += math.ceil(RentalPeriod.seconds/604800) * 200 * int(NumberOfSkis)
                else:
                    #Days
                    bill += math.ceil(RentalPeriod.seconds/86400) * 50 * int(NumberOfSkis)
                
            # weekly bill calculation
            elif RentalBasis == 'Weekly':
                #weeks
                bill += math.ceil(RentalPeriod.seconds/604800) * 200 * int(NumberOfSkis)

            # Snowboard bill calculation
            # hourly bill calculation
            if RentalBasis == 'Hourly':
                #Check to See if more than 4 Hours
                if math.ceil(RentalPeriod.seconds) >= 14400:
                    #days
                    bill += math.ceil(RentalPeriod.seconds/86400) * 40 * int(NumberOfSnowBoards)
                else:
                    #Hours
                    bill += math.ceil(RentalPeriod.seconds / 3600) * 10 * int(NumberOfSnowBoards)
                
            # daily bill calculation
            elif RentalBasis == 'Daily':
                #Check to see if more than 4 days
                if math.ceil(RentalPeriod.days) >= 4:
                    #Weeks
                    bill += math.ceil(RentalPeriod.seconds/604800) * 160 * int(NumberOfSnowBoards)
                else:
                    #days
                    bill += math.ceil(RentalPeriod.seconds/86400) * 40 * int(NumberOfSnowBoards)
                
            # weekly bill calculation
            elif RentalBasis == 'Weekly':
                #weeks
                bill += math.ceil(RentalPeriod.seconds/604800) * 160 * int(NumberOfSnowBoards)
       
            print("Total Bill For Rental Before Discount ${}".format(bill))


            # Family Discount Calculation Way 2
            #if (NumberOfSkis + NumberOfSnowBoards >= 3):
            #    if NumberOfSkis < 6 and NumberOfSkis > 2 Then 
            #    else
                    
            #    NumberOfSnowboards - NumberOfSkis 



            dblDiscountTotal = float(0)
            # Cupon Discount
            if 'BBP' in CuponCode:
                dblDiscountTotal += bill * 0.10
                
                print('Cupon code accepted! You just got 10% OFF!')
            else:
                print('Invalid cupon code. No discount will be applied. Start Over to Re-Enter')
            

            
            # family discount calculation Way 1
            #if (3 <= NumberOfSkis + NumberOfSnowBoards <= 5):

            #    print("You are eligible for Family rental promotion of 25% discount")
            #    dblDiscountTotal += bill * 0.25
                
            if (3 <= int(NumberOfSkis) + int(NumberOfSnowBoards)):
                print("You are eligible for Family rental promotion of 25% discount")
                FDiscountbill = int(0)
                if int(NumberOfSkis) >= 5:
                    intFamilyDNumberOfSkis = int(5)
                    if RentalBasis == 'Hourly':
                        if math.ceil(RentalPeriod.seconds) >= 14400:
                            #DAys
                            FDiscountbill += math.ceil(RentalPeriod.seconds/86400) * 50 * int(intFamilyDNumberOfSkis)
                        else:
                            #Hours
                            FDiscountbill += math.ceil(RentalPeriod.seconds / 3600) * 15 * int(intFamilyDNumberOfSkis)
                    elif RentalBasis == 'Daily':
                        if math.ceil(RentalPeriod.days) >= 4:
                            #Weeks
                            FDiscountbill += math.ceil(RentalPeriod.seconds/604800) * 200 * int(intFamilyDNumberOfSkis)
                        else:
                            #days
                            FDiscountbill += math.ceil(RentalPeriod.seconds/86400) * 50 * int(intFamilyDNumberOfSkis)
                    elif RentalBasis == 'Weekly':
                        #weeks
                        bill += math.ceil(RentalPeriod.seconds/604800) * 200 * int(intFamilyDNumberOfSkis)
                        
                else: 
                    if (int(NumberOfSkis) + int(NumberOfSnowBoards)) >= 5:
                        intFamilyDNumberOfSnowboards = 5 - int(NumberOfSkis)
                        intFamilyDNumberOfSkis = int(NumberOfSkis)
                    else:
                        intFamilyDNumberOfSnowboards = int(NumberOfSnowBoards)
                        intFamilyDNumberOfSkis = int(NumberOfSkis)
                    if RentalBasis == 'Hourly':
                        if math.ceil(RentalPeriod.seconds) >= 14400:
                            FDiscountbill += math.ceil(RentalPeriod.seconds/86400) * 50 * int(intFamilyDNumberOfSkis)
                        else:
                            FDiscountbill += math.ceil(RentalPeriod.seconds / 3600) * 15 * int(intFamilyDNumberOfSkis)
                    elif RentalBasis == 'Daily':
                        if math.ceil(RentalPeriod.days) >= 4:
                            FDiscountbill += math.ceil(RentalPeriod.seconds/604800) * 200 * int(intFamilyDNumberOfSkis)
                        else:
                            FDiscountbill += math.ceil(RentalPeriod.seconds/86400) * 50 * int(intFamilyDNumberOfSkis)
                    elif RentalBasis == 'Weekly':
                        #weeks
                        FDiscountbill += math.ceil(RentalPeriod.seconds/604800) * 200 * int(intFamilyDNumberOfSkis)


                    if RentalBasis == 'Hourly':
                        if math.ceil(RentalPeriod.seconds) >= 14400:
                            FDiscountbill += math.ceil(RentalPeriod.seconds/86400) * 40 * int(intFamilyDNumberOfSnowboards)
                        else:
                            FDiscountbill += math.ceil(RentalPeriod.seconds / 3600) * 10 * int(intFamilyDNumberOfSnowboards)
                    elif RentalBasis == 'Daily':
                        if math.ceil(RentalPeriod.days) >= 4:
                            FDiscountbill += math.ceil(RentalPeriod.seconds/604800) * 160 * int(intFamilyDNumberOfSnowboards)
                        else:
                            FDiscountbill += math.ceil(RentalPeriod.seconds/86400) * 40 * int(intFamilyDNumberOfSnowboards)
                    elif RentalBasis == 'Weekly':
                        FDiscountbill += math.ceil(RentalPeriod.seconds/604800) * 160 * int(intFamilyDNumberOfSnowboards)

                    dblDiscountTotal += FDiscountbill * 0.25
            if dblDiscountTotal >= bill:
                bill = 0
            bill = bill - dblDiscountTotal
            Shop.TotalRevenueForDay += bill
            #print("Thanks for returning your equipment. Hope you enjoyed our service!")
            print("Discount Total: ", dblDiscountTotal)
            print("That would be ${}".format(bill))



            return bill
        
        else:
            print("Are you sure you rented equipment with us?")
            return None

    def Print_Daily_Totals(self):
        print("Total Skis Rented Today: ", Shop.TotalSkisRentedForDay)
        print("Total Snowboards Rented Today: ", Shop.TotalSnowBoardsRentedForDay)
        print("Total Revenue For Today (Based On Returns): ", Shop.TotalRevenueForDay)
       
        

#--------------------------------------------------------------------------
# Final Project - Main Processing Area   - Ski/Snowboard shop
# Validation
#--------------------------------------------------------------------------

def Validate_Number_Of_Skis_Stock_Input(intInventoryInputSkis):
   try:
        intInventoryInputSkis = int(intInventoryInputSkis)
        if intInventoryInputSkis >= 0:
            global blnInputValidated
            blnInputValidated = True
        else:
            print("Must Be Positive Number, Greater Than 0")
   except ValueError:
        intInventoryInputSkis = int(0)
        print("Must be an Integer Number")
   return intInventoryInputSkis



def Validate_Number_Of_Snowboards_Stock_Input(intInventoryInputSnowboards):
   try:
        intInventoryInputSnowboards = int(intInventoryInputSnowboards)
        if intInventoryInputSnowboards >= 0:
            global blnInputValidated
            blnInputValidated = True
        else:
            print("Must Be Positive Number, Greater Than 0")
   except ValueError:
        intInventoryInputSnowboards = int(0)
        print("Must be an Integer Number")
   return intInventoryInputSnowboards

def Validate_Selection_Menue_Input ( intSelectionMenue ):
    try:
        intSelectionMenue = str(intSelectionMenue)
        if intSelectionMenue == "1" or intSelectionMenue == "2" or intSelectionMenue == "3" or intSelectionMenue == "4":
            global blnInputValidated
            blnInputValidated = True
            return intSelectionMenue
        else:
            print("You Must Choose an Option by Entering a Number, 1-4")
    except ValueError:
            intSelectionMenue = str("")
            print("You Must Choose an Option")

def Validate_Customer_Name_Input(strCustomerName):
    if strCustomerName == "":
        print("Please Make Sure to Enter Your Name")
    else: 
        global blnInputValidated
        blnInputValidated = True
        return strCustomerName

def Validate_Type_Of_Rental_Input(strSelectionMenue):
    if strSelectionMenue == "skis" or strSelectionMenue == "Skis" or strSelectionMenue == "snowboards" or strSelectionMenue == "Snowboards" or strSelectionMenue == "Both" or strSelectionMenue == "both":
            global blnInputValidated
            blnInputValidated = True
            return strSelectionMenue
    else:
        print("You Must Select a Type of Rental. Either Skis, Snowboards or Both")
#Rental Basis
def Validate_Rental_Bases_Time_Period_Input( intRentalBasis ):
    try:
        intRentalBasis = int(intRentalBasis)
        if intRentalBasis == 1 or intRentalBasis == 2 or intRentalBasis == 3:
            global blnInputValidated
            blnInputValidated = True
            return intRentalBasis
        else:
            print("You Must Choose an Option by Entering a Number, 1, 2 or 3")
    except ValueError:
            print("Your Choise Must Be an integer. 1, 2 or 3")
# VAlidate Return Customer ID

def Validate_Return_Customer_ID( intReturnCustomerID ):
    global lstCustomerlist
    try:
        intReturnCustomerID = int(intReturnCustomerID)
        for obj in lstCustomerlist:
            if intReturnCustomerID == obj.ID:
                global blnInputValidated
                blnInputValidated = True
                return intReturnCustomerID
    except ValueError:
            print("You Must Enter One of The Numbers Listed Next to the names. This Is The CustomerID for the Customer With That Name")

# Validate Coupon Code
def Validate_Coupon_Code_Input(strCouponCode):
    if strCouponCode == "":
        print("Please Make Sure to Enter A Coupon Code")
    else: 
        global blnInputValidated
        blnInputValidated = True
        return strCouponCode

def Validate_Next_Customer_Input( intInput ):
    if intInput == "Y" or intInput == "y":
        global blnInputValidated
        blnInputValidated = True
        return intInput
   



#--------------------------------------------------------------------------
# Project # 1 - Main Processing Area   
# Calculations
#--------------------------------------------------------------------------

lstCustomerlist = []
intCustomerID = int(0)
intValue1 = int(0)
intValue2 = int(0)
blnInputValidated = bool(False)
strNewCustomer = str('Y')

    #Establish Stock 
while blnInputValidated == False:
    intInventoryInputSkis = input("Enter Total Number Of Skis In Shops Inventory: ")
    intInventoryInputSkis = Validate_Number_Of_Skis_Stock_Input(intInventoryInputSkis)

blnInputValidated = bool(False)

while blnInputValidated == False:
    intInventoryInputSnowboards = input("Enter Total Number Of Snowboards In Shops Inventory: ")
    intInventoryInputSnowboards = Validate_Number_Of_Snowboards_Stock_Input(intInventoryInputSnowboards)
blnInputValidated = bool(False)

    #Instantiate Shop
    
shop1 = Shop(intInventoryInputSkis, intInventoryInputSnowboards)

shop1.DisplayStock() 



while strNewCustomer == 'Y' or strNewCustomer == 'y':
    blnInputValidated = False 
    #navigational selection
    while blnInputValidated == False:
        intSelectionMenue = input("What would you like to do. Enter '1' for New Customer Rental, '2' for Rental Return, '3' 'for Show Inventory', '4' for 'End of Day': ")
        intSelectionMenue = Validate_Selection_Menue_Input (intSelectionMenue)
    blnInputValidated = bool(False)

#New Customer
    if intSelectionMenue == "1":
        
        blnInputValidated = bool(False)
        while blnInputValidated == False:
            strCustomerName = input("Enter Customer Full Name: ")
            strCustomerName = Validate_Customer_Name_Input(strCustomerName)

        #instantiate Customer
        lstCustomerlist.append(Customer(strCustomerName, intCustomerID))


        # Number of snowboards and skis
        blnInputValidated = bool(False)
        while blnInputValidated == False:
            strTypeOfRental = input("What Type Of Rental Would you like? To Rent Skis please enter 'Skis', To Rent SnowBoards Please Enter 'Snowboards' or To Rent Both Skis and Snowboards Please Enter 'Both': ")
            strTypeOfRental = Validate_Type_Of_Rental_Input(strTypeOfRental)


        intNumberOfSkis = int(0)
        intNumberOfSnowboards = int(0)


        if strTypeOfRental == "Skis" or strTypeOfRental == "skis":
            blnInputValidated = bool(False)
            while blnInputValidated == False:
                intNumberOfSkis = input("Enter Total Number Of Skis You Want to Rent: ")
                intNumberOfSkis = lstCustomerlist[intCustomerID].RequestSkis(intNumberOfSkis)
        else:
            if strTypeOfRental == "Snowboards" or strTypeOfRental == "snowboards":
                blnInputValidated = bool(False)
                while blnInputValidated == False:
                    intNumberOfSnowboards = input("Enter Total Number Of Snowboards You Want to Rent: ")
                    intNumberOfSnowboards = lstCustomerlist[intCustomerID].RequestSnowBoards(intNumberOfSnowboards)
            elif strTypeOfRental == "Both" or strTypeOfRental == "both":
                blnInputValidated = bool(False)
                while blnInputValidated == False:
                    intNumberOfSkis = input("Enter Total Number Of Skis You Want to Rent: ")
                    intNumberOfSkis = lstCustomerlist[intCustomerID].RequestSkis(intNumberOfSkis)
                blnInputValidated = bool(False)
                while blnInputValidated == False:
                    intNumberOfSnowboards = input("Enter Total Number Of Snowboards You Want to Rent: ")
                    intNumberOfSnowboards = lstCustomerlist[intCustomerID].RequestSnowBoards(intNumberOfSnowboards)


        


        #Rental basis
        blnInputValidated = bool(False)
        while blnInputValidated == False:
            intRentalBasis = input("How Long Would You Like The Rental to be? Enter '1' for Hourly Rental, '2' For Daily Rental, '3' For Weekly Rental: ")
            intRentalBasis = Validate_Rental_Bases_Time_Period_Input(intRentalBasis)

        if intRentalBasis == 1:
            strRentalBasis = str("Hourly")
        elif intRentalBasis == 2:
            strRentalBasis = str("Daily")
        elif intRentalBasis == 3:
            strRentalBasis = str("Weekly")

        #for obj in lstCustomerlist:
        #    if obj.ID == intCustomerID:
        #        obj.RentalBasis = strRentalBasis

        lstCustomerlist[intCustomerID].RentalBasis = strRentalBasis


        ## Rental time
        #blnInputValidated = bool(False)
        #while blnInputValidated == False:
        #    intRentalAmountOfTime = input("How Many " + strRentalBasis + " Would You Like To Rent For? : ")
        #    intRentalAmountOfTime = Validate_Rental_Bases_Time_Amount_Input(intRentalAmountOfTime)

        # Set Time At Rental Request (to use upon return)
        lstCustomerlist[intCustomerID].rentalTime = datetime.now()

        ####


        # Cupon code
        blnInputValidated = bool(False)
        while blnInputValidated == False: 
            strCouponCode = input("If Valide Coupon Code Is Not Entered At This Time Rental Will Have to Be Restarted To Enter. Enter Any Characters other than 'BBP' If Customer Does Not Have Coupon Code. Please Enter Coupon Code Now: ")
            strCouponCode = Validate_Coupon_Code_Input(strCouponCode)


        lstCustomerlist[intCustomerID].CuponCode = strCouponCode


        #Initiate Rental

        if strTypeOfRental == "Both" or strTypeOfRental =="both":
            if intRentalBasis == 1:
                shop1.RentSkisOnHourlyBasis(intNumberOfSkis)
                shop1.RentSnowBoardStockOnHourlyBasis(intNumberOfSnowboards)
            elif intRentalBasis == 2:
                shop1.RentSkisOnDailyBasis(intNumberOfSkis)
                shop1.RentSnowBoardStockOnDailyBasis(intNumberOfSnowboards)
            elif intRentalBasis == 3:
                shop1.RentSkisOnDweeklyBasis(intNumberOfSkis)
                shop1.RentSnowBoardStockOnWeeklyBasis(intNumberOfSnowboards)
        elif strTypeOfRental == "Skis" or strTypeOfRental == "skis":
            if intRentalBasis == 1:
                shop1.RentSkisOnHourlyBasis(intNumberOfSkis)
            elif intRentalBasis == 2:
                shop1.RentSkisOnDailyBasis(intNumberOfSkis)
            elif intRentalBasis == 3:
                shop1.RentSkisOnDweeklyBasis(intNumberOfSkis)
        elif strTypeOfRental == "Snowboard" or strTypeOfRental == "snowboard":
            if intRentalBasis == 1:
                shop1.RentSnowBoardStockOnHourlyBasis(intNumberOfSnowboards)
            elif intRentalBasis == 2:
                shop1.RentSnowBoardStockOnDailyBasis(intNumberOfSnowboards)
            elif intRentalBasis == 3: 
                shop1.RentSnowBoardStockOnWeeklyBasis(intNumberOfSnowboards)

        shop1.DisplayStock()
        intCustomerID += 1 

        print("Rental Is Complete For This Customer")

    elif intSelectionMenue == "2":
        #Determine Returing Customer's CustomerID and Name
        if intCustomerID == 0:
            print("You Must Choose 1 for New Customer Before Choosing 2 For Return")
        else:
            blnInputValidated = bool(False)
            while blnInputValidated == False:
                for obj in lstCustomerlist:
                    print( obj.Name, obj.ID, sep =' ' )
                intReturnCustomerID = input("Enter Number Next To Customer's Name (Customer ID): ")
                intReturnCustomerID = Validate_Return_Customer_ID(intReturnCustomerID)
            #print Name
            print(lstCustomerlist[intReturnCustomerID].Name)

            request = lstCustomerlist[intReturnCustomerID].returnEquipment(strTypeOfRental)
            shop1.ReturnEquipment(request) 
    elif intSelectionMenue == "3":
        shop1.DisplayStock()
    elif intSelectionMenue == "4":
        shop1.Print_Daily_Totals()
        break
        
        
    blnInputValidated = False 
    while blnInputValidated == False:
        strNewCustomer = input("Next Customer? Or if you would like to do something else, enter Y: ")
        strNewCustomer = Validate_Next_Customer_Input(strNewCustomer)
    




    #intRequestRentalFromCustSkis = input("Enter How Many Skis Would You LIke To Rent: ")
    #intRentalTimeBasisCust = input("Would You Like To Rent For A Certain Number Hours, Days or Weeks. Enter 'Hourly' for Hours, 'Daily' for Days Or 'Weekly' for Weeks. ")
    #intRequestRentalFromCustSnowboards = input("Enter How Many Snowboards Would You LIke To Rent: ")







    ##Check
    #shop1.RentSkisOnHourlyBasis(intRequestRentalFromCustSkis)
    #shop1.RentSkisOnDailyBasis(-1)

    ##Initiate Rental - Check
    #shop1.RentSnowBoardStockOnHourlyBasis()
    #shop1.RentSnowBoardStockOnDailyBasis(-1)
    #shop2.RentSnowBoardStockOnWeeklyBasis(14)


    ##Check
    ## Create customer
    #customer1 = Customer()
    #customer2 = Customer()
    #customer3 = Customer()
    #customer4 = Customer()

    ##Customerlist.append (Customer())
    ##for obj in Customerlist:
    ##    if 

    ## Rental basis. Check
    #customer1.RentalBasis = 1 #'Hourly'
    #customer2.RentalBasis = 2 #'Daily'
    #customer3.RentalBasis = 2 #'Daily'
    #customer4.RentalBasis = 3 #'Weekly'

    ## Number of snowboards and skis. Check
    #customer1.NumberOfSkis = 2
    #customer2.NumberOfSkis = 1
    #customer3.NumberOfSkis = 1
    #customer4.NumberOfSkis = 2

    #customer1.NumberOfSnowBoards = 3
    #customer2.NumberOfSnowBoards = 1
    #customer3.NumberOfSnowBoards = 2
    #customer4.NumberOfSnowBoards = 2

    ## Rental time. Check
    #customer1.rentalTime = datetime.now() + timedelta(hours=-3)
    #customer2.rentalTime = datetime.now() + timedelta(days=-2)
    #customer3.rentalTime = datetime.now() + timedelta(days=-5)
    #customer4.rentalTime = datetime.now() + timedelta(days=-14)

    ## Cupon code. Check
    #customer1.CuponCode = '123BBP'
    #customer2.CuponCode = '456TTT'
    #customer3.CuponCode = '789BBP'
    #customer4.CuponCode = '101TTT'

    ## create request to return the bike
    #request1 = customer1.returnEquipment()
    #request2 = customer2.returnEquipment()
    #request3 = customer3.returnEquipment()
    #request4 = customer4.returnEquipment()

    ## return the bike to shop and get a bill
    #shop1.ReturnEquipment(request1) 
    #shop1.ReturnEquipment(request2) 
    #shop1.ReturnEquipment(request3) 
    #shop1.ReturnEquipment(request4) 


    #Qs for Bob
    #How prevent someone from choosing 2 before choosing 1? 
    #Accumulation not working right 

    
