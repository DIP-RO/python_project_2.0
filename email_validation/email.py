email = input("Enter your email: ")  # g@g.in
k, j, l = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count("@") == 1):
            if (email[-4] == ".") or (email[-3] == ".") or (email[-3] and email[-7] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                        break
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                            break
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "-" or i == "@" or i == ".":
                        continue
                    else:
                        l = 1
                if i == "k" or i == "j" or i == "l":
                    print("Enter valid email")

            else:
                print("Please enter valid Email Address")
        else:
            print("Please enter valid Email Address")
    else:
        print("Please enter valid Email Address")
else:
    print("Wrong Email 1")
