import string
import api as ap   #api code 
import currency_list as cl  #currency code for currency dict
#currency converter  
#Any currency to any currency.
#written by Nandhu
#_version_2.1_

#Function for sending data to Currency class
def call(amount,frm,frmto):
    get = ap.Currency(amount,frm,frmto)
    print("\nplease wait....\n")
    get.check()
    get.prnt()
#function for converting into numbers
def set1(amount1):
    num = [x for x in amount1 if x in string.digits]   
    return ''.join(num).strip()

#function for taking input from the user
def ask():
    #dictionary for currency
    currency = cl.list()
    try:
        while True:
            #amount input from user
            amount = 0
            amount1 = input("\nEnter the amount : ")
            amount = set1(amount1)
            #check if amount is not empty
            if amount not in '':
                while True:
                    count = 0
                    #printing currency examples
                    print(">>I_HOPE_U_KNOW_CURRENCY_SHORTFORMS_<<")
                    print('\t    EXAMPLES')
                    print('|--------------------------------|')
                    for x in currency:
                        if count == 6:
                            break
                        else:
                            print(">>",x,'\t\t\t')
                            print('|--------------------------------|')
                            count += 1
                    #take input from -> to
                    frm1 = input("Convert from : ")
                    frmto1 = input(f"{frm1.upper()} to : ")
                    frm = frm1.upper()
                    frmto = frmto1.upper()
                    #check if currency exist
                    if  frm in currency and frmto in currency:
                        call(amount,frm,frmto)
                        break          
                    else:
                        print('\n>>>out_of_choice<<<<\n')
            #exception for invalid input
            else:
                print("\n>>>>invalid_input<<<\n")
                continue
            break
    #for ctrl + c
    except KeyboardInterrupt:
        print('\n\n>>>use_my_program_later<<<\n\n')
    #execute this at the end of program
    finally:
        print("""\nThank you for using me :)\n\n\nThis program was made by @cuber-dev Admin of web_learnerX,
        \n\n\nWelcome to Web Learner's Community.(Telegram)

        🧠 | HTML • CSS • Javascript  • React  • Node  js  • Angular • Next  • Vue 



        ✅ Join: @Web_LearnerX

        💬 Admin Contact:  @WebSaan | @cuber_dev | @codexpranav | @CodeX_Rix |\n\n""")
#calling ask function
ask()
#end
