# Application that can check the age of a person
# Input name and age in the application
# 18 years below access will be denied

current_year = 2023 #int



def age_cal():
    name_of_student = (input("Enter Name:   "))
    age_calculation = int(input("Enter year of birth:   "))
    if  age_calculation <= 2005 :
        final_year  = current_year - age_calculation
        
        print("hello", name_of_student , "your age is", final_year ,"years and qualified")
    else:
        final_year  = current_year - age_calculation
        print('hello', name_of_student, 'your age is', final_year, "years, you are not qualified yet" )
  

age_cal()
