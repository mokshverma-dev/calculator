global run
# ---------------------------------------------------------------
# These all 4 functions are of Mathematical Calculations


def addition():
    number1, number2 = int(input(" -> Enter the value of 1st number : ")
                           ), int(input(" -> Enter the value of 2st number : "))
    print(" => The Sum is ", number1+number2)


def subtraction():
    number1, number2 = int(input(" -> Enter the value of 1st number : ")
                           ), int(input(" -> Enter the value of 2st number : "))
    print(" => The Subtraction is ", number1-number2)


def multiplication():
    number1, number2 = int(input(" -> Enter the value of 1st number : ")
                           ), int(input(" -> Enter the value of 2st number : "))
    print(" => The Multiplication is ", number1*number2)


def division():
    number1, number2 = int(input(" -> Enter the value of 1st number : ")
                           ), int(input(" -> Enter the value of 2st number : "))
    print(" => The Division is ", number1/number2)

# ---------------------------------------------------------------
# Function where all the Mathematical Operations will take place


def mathematical_calculator():
    print('''
    
'Here is your MATHEMATICAL CALCULATOR'
=====================
Enter the Operation : 
1. Addition - 'Add'
2. Subtraction - 'Sub
3. Multiplication - 'Mul'
4. Division - 'Div'
5. Back to Main Menu - 'Menu'
---------------------
''')

    m_option = str(input("Which operation you want to perform : "))

    if m_option == "Add" or m_option == "add" or m_option == "Addition" or m_option == "addition" or m_option == "+":
        addition()
    elif m_option == "Sub" or m_option == "sub" or m_option == "Subtraction" or m_option == "subtraction" or m_option == "-":
        subtraction()
    elif m_option == "Mul" or m_option == "mul" or m_option == "Multiplication" or m_option == "multiplication" or m_option == "*":
        multiplication()
    elif m_option == "Div" or m_option == "div" or m_option == "Division" or m_option == "division" or m_option == "/":
        division()
    elif m_option == "Menu" or m_option == "menu" or m_option == "Main Menu" or m_option == "main menu" or m_option == "back":
        main_menu()
    else:
        print(" 'Please Enter the right Input' ")
        mathematical_calculator()

# ---------------------------------------------------------------
# Function where Simple Interest will be Calculated


def simple_interest_calculator():
    print(''''Here is your SIMPLE INTEREST CALCULATOR'
=====================
''')

    principle_amount, interest_rate, time_period = int(
        input(" -> Enter the Principle Amount (Begining Balance) : ")), int(input(" -> Enter the Interest Rate : ")), int(input(" -> Enter the Time Period (in years) : "))

    print(" => The Final Interest Amount is ",
          (principle_amount*interest_rate*time_period)/100)

# ---------------------------------------------------------------
# Function where BMI Calculator will be Calculated


def bmi_calculator():
    print(''''Here is your BMI CALCULATOR'
=====================
''')

    height, weight = int(
        float(input(" -> Enter the Height (in meters) : "))), float(input(" -> Enter the Weight (in kgs) : "))

    print(" => The Final BMI Calculated is ", weight/height**2)

# ---------------------------------------------------------------


def main_menu():
    print('''
    
'HERE IS YOUR CALCULATOR'
=========================
''')
    print('''Enter the Operation : 
    1. Calculation - 'C' or 1
    2. Simple Interest Calculation - 'SI' or 2
    3. BMI Calculation - 'BMI' or 3
    4. Press 4 to exit
-------------------------
''')
    option = str(input("Which calculator you want to use : "))

    if option == "Calculation" or option == "calculation" or option == "C" or option == "c" or option == "+" or option == "-" or option == "*" or option == "/" or option == str(1):
        mathematical_calculator()
    elif option == "Simple Interest" or option == "simple interest" or option == "SI" or option == "si" or option == "interest" or option == str(2):
        simple_interest_calculator()
    elif option == "BMI Calculator" or option == "BMI calculator" or option == "bmi calculator" or option == "BMI" or option == "bmi" or option == str(3):
        bmi_calculator()
    elif option == str(4) or option == "Exit" or option == "exit":
        run = False
    else:
        print(" 'Please Enter the right Input' ")
        main_menu()

# ==================================================================


run = True
while (run):
    main_menu()
