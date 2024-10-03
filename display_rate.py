user_choice = float(input("1 for hdfc 2 for aditya birla 3 for motilal oswal:- "))

if user_choice==1:
   principle = float(input("how much amount:- "))
   years = float(input("how many years:- "))
   
   return_rate1= principle * (1 + 0.086 / 1) ** years
   
   print("return rate is:- ", return_rate1 )

elif user_choice==2:
   principle2 = float(input("how much amount:- "))
   years2 = float(input("how many years:- "))
   
   return_rate2= principle2 * (1 + 0.0725 / 1) ** years2
   
   print("return rate is:- ", return_rate2 )

elif user_choice==3:
   principle3 = float(input("how much amount:- "))
   years3 = float(input("how many years:- "))
   
   return_rate3= principle3 * (1 + 0.18 / 1) ** years3
   
   print("return rate is:- ", return_rate3 )
      