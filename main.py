import json

questions = """
1 - What is your mother's name?
2 - What city were you born in?
3 - What month was your younget sibling born in?
4 - What city did your parents fall in love?
"""

while True:

  option = input("""
  =========================
  Welcome to Soham's Bank!!
  =========================
  Please pick one of the options:
  1 - Make an account
  2 - Add Money
  3 - Withdraw Money
  4 - Transfer Money
  5 - Close your account
  6 - Exit.
  7 - Forgot my ID.
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
        print("\n Your account has been created!")
        with open("number.json", "r") as b:
          number = json.load(b)
        x = list(number.keys())[0]
        print(f"\n Your ID is {x}. Make sure to remember this. If you forget make sure to pick option 7 to get your ID.")
        moreinfo["ID"] = str(x)
        x = int(x)
        x += 1
        x = str(x)
        with open("number.json", "w") as r:
          json.dump(number, r)
        print("\n" + questions)
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
      continue
       
      

    elif option == 6:
      print("\n Thanks for using Soham's bank! We hope you will return!")
      break
    elif option == 7:
      continue
    
    else:
      print("\n Type a proper option.")
      continue

  except ValueError:
    print("\n \n This is not a valid option. Please try again!")
    continue
