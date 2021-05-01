import json

questions = ["1 - What is your mother's name?", "2 - What city were you born in?", "3 - What month was your younget sibling born in?", "4 - What city did your parents fall in love?"]

while True:

    option = input("""
  =========================
  Welcome to My Bank!!
  =========================
  Please pick one of the options:
  1 - Make an Account
  2 - Add Money
  3 - Withdraw Money
  4 - Transfer Money
  5 - Close your account
  6 - Exit.
  7 - Forgot my Password.
  =========================
  Pick your option: """)

    try:
        option = int(option)
        if option == 1:
            with open("info.json", "r") as f:
                data = json.load(f)

            email = input("\n Whats your email? ")

            if email in data.keys():
                print("Sorry there is already an account in the database with this email. Try again with a new email!")
            
                while True:
                    c = input("Do you still want to use the bank? Answer with True or False? ")
                    if c == "True":
                        break
                    elif c == "False":
                        print("Thanks for using our bank! We hope you will return!")
                        break
                    else:
                        print("Try again, and answer properly!")
                        continue
            
                if c == "False":
                    break

            else:
                data[str(email)] = {}
                moreinfo = data[str(email)]
                fname = input(" \n What's your first name? ")
                moreinfo["first_name"] = str(fname)
                lname = input("\n What's your last name? ")
                moreinfo["last_name"] = str(lname)
                with open("username_password.json", 'r') as g:
                    dat = json.load(g)
                while True:
                    username = input("\n What's your username? ")
                    if username in dat.keys():
                        print("This username is already in use. Please choose another one.")
                        continue
                    else:
                        break
                password = input("\n What's your password? ")
                dat[str(username)] = str(password)
                with open("username_password.json", 'w') as h:
                    json.dump(dat, h)
                print("\n Your account has been created!")
                questionstring = ""
                for i in questions:
                    questionstring += i
                    questionstring+= "\n"
                print(questionstring)
                option2 = input("\n Pick one option for a security question (You will have to restart the process if you don't pick a correct number): ")
                try:
                    option2 = int(option2)
                    if option2 == 1:
                        moreinfo["security_question"] = "What is your mother's name?"

                        answer = input("\n What is your mother's name? ")
                        moreinfo["security_question_answer"] = str(answer)

                        print(f"\n Your answer was: {answer}")
                        print("\n Make sure to remember this answer or you may not be able to log into your account and do any of the actions.")


                        with open("info.json", "w") as l:
                            json.dump(data, l)
                except ValueError:
                    print("\n \n This is not a valid option. Please try again!")
                    break
        
        


        elif option == 2:
            with open("username_password.json", 'r') as z:
                data = json.load(z)
            
            uname = input("\n You will have to login for you to add money! What is your username: ")
            if uname in data.keys():
                while True:
                    passw = input("\n Now whats your password: ")
                    actualp = data[str(uname)]
                    if str(passw) == str(actualp):
                        print("Perfect! You are now logged in!")
                        c = 1
                        break
                    else:
                        print("You mistyped your password. Please try again.")
                        continue
                
            else:
                print("You don't have an account, or you mistyped your username. Either way you are going back to the home page.")
                c = 0
            
            if c == 1:
                money = input("How much money do you want to add to your account: ")
                try:
                    money = float(money)
                except:
                    print("The money you inputted is not integer.")
                    

            
            

                

       
      

        elif option == 6:
            print("\n Thanks for using My bank! We hope you will return!")
            break
        elif option == 7:
            continue
    
        else:
            print("\n Type a proper option.")
            continue

    except ValueError:
        print("\n \n This is not a valid option. Please try again!")
        continue
