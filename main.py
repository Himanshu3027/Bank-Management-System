import pickle
import random

# FUNCTION FOR CREATING ACCOUNT
def create_acc():
    print("To create new Account enter the following details:")
    name = input("Enter your name: ")
    acc_type = input("\nEnter the type of Account you want to create:\n\t1. Savings Account\n\t2. Fixed Deposit\n\t3. Current Account\n\t")
    open_amt = float(input("\nEnter the Account opening balance:\t"))
    last_trans_amt = 0
    last_depo_amt = 0
    input("\nTo confirm Press ENTER")
    num = "10019"
    ra = str(random.randint(1000, 9999))
    acc_no = int(num + ra)
    total_amt = open_amt
    password = input("\nEnter your password: ")
    print("\nYour PASSWORD is created.\nKindly remember it for future use!")
    all = [acc_no, acc_type, name, password, open_amt, total_amt, last_depo_amt, last_trans_amt]
    fh = open("bank-file.bin", "ab")
    pickle.dump(all, fh)
    fh.close()
    print("\t-----THANK YOU-----")
    print("You have successfully created your Account")
    input("Press any key")
    print("\nYour Account details are:\n\tACCOUNT DETAILS\n")
    print("\n\tACCOUNT NUMBER: ", acc_no)
    print("\tACCOUNT HOLDER NAME: ", name)
    print("\tACCOUNT TYPE: ", acc_type)
    print("\tOPENING AMOUNT: ", open_amt)
    input("\nTo proceed Press ENTER")
    return

# FUNCTION FOR CHECKING PASSWORD
def pass_word(a):
    while True:
        o = 1
        p = input("\nEnter your Password: ")
        if p == a[3]:
            break
        else:
            i = int(input("\nPassword is incorrect!\n=>To re-enter your Password PRESS 1\n=>To go to the Main Menu PRESS 2:\t"))
            print("\n\n")
            if i == 1:
                continue
            else:
                o = 0
                break
    return o

# FUNCTION FOR PRINTING STATEMENT
def statement(a):
    fs = open("bank-file.bin", "rb")
    try:
        while True:
            q = pickle.load(fs)
            if q[0] == a:
                input("To print your Account Statement press ENTER key\n")
                print("\t\t·······ACCOUNT STATEMENT·······")
                print("\n\tACCOUNT NUMBER: ", q[0])
                print("\tACCOUNT HOLDER NAME: ", q[2])
                print("\tACCOUNT TYPE: ", q[1])
                print("\tOPENING AMOUNT: ", q[4])
                print("\tCURRENT BALANCE: ", q[5])
                print("\tLAST TRANSACTION AMOUNT: ", q[7])
                print("\tLAST DEPOSITED AMOUNT: ", q[6])
                input("\nTo go back to Main Menu press ENTER key")
                break
    except EOFError:
        fs.close()
    return

# FUNCTION FOR DEPOSITING AMOUNT
def deposit(a):
    fs = open("bank-file.bin", "rb+")
    try:
        while True:
            r = fs.tell()
            q = pickle.load(fs)
            if q[0] == a:
                dep = float(input("\nEnter the Amount to be deposited: "))
                q[5] += dep
                q[6] = dep
                fs.seek(r)
                pickle.dump(q, fs)
                print("\nYou have successfully deposited the amount")
                input("To go back to Main Menu press ENTER key")
                break
    except EOFError:
        fs.close()
    return

# FUNCTION FOR TRANSACTING AMOUNT
def trans_amt(a):
    fs = open("bank-file.bin", "rb+")
    try:
        while True:
            r = fs.tell()
            q = pickle.load(fs)
            if q[0] == a:
                trans = float(input("\nEnter the amount to be transacted: "))
                if trans <= q[5]:
                    q[5] -= trans
                    q[7] = trans
                    fs.seek(r)
                    pickle.dump(q, fs)
                    print("\nYour transaction is successful")
                    input("To go back to Main Menu press ENTER key")
                    break
                else:
                    print("\nYou don't have enough balance to transact this amount")
                    input("To go back to Main Menu press ENTER key")
    except EOFError:
        fs.close()
    return

# FUNCTION FOR MODIFYING ACCOUNT DETAILS
def edit(a):
    fs = open("bank-file.bin", "rb+")
    try:
        while True:
            r = fs.tell()
            q = pickle.load(fs)
            if q[0] == a:
                z = int(input("\n1.To Change the Account holder name PRESS 1\n2.To Change the Account Type PRESS 2\n3.To Change the Password PRESS 3\n\tEnter the Option:\t"))
                if z == 1:
                    na = input("\nEnter the new Account Holder Name:\t")
                    q[2] = na
                    fs.seek(r)
                    pickle.dump(q, fs)
                    print("The Account Holder Name is changed successfully")
                    input("Press Enter to Proceed")
                    break
                elif z == 2:
                    ty = input("\nEnter the new Account Type:\t")
                    q[1] = ty
                    fs.seek(r)
                    pickle.dump(q, fs)
                    print("The Account Type is changed successfully")
                    input("Press Enter to Proceed")
                    break
                elif z == 3:
                    input("Enter the Old Password\t")
                    pa = input("Enter the new Password\t")
                    input("Enter the new Password again to confirm\t")
                    q[3] = pa
                    fs.seek(r)
                    pickle.dump(q, fs)
                    print("The Password is changed successfully")
                    input("Press Enter to Proceed")
                    break
    except EOFError:
        fs.close()
    return

# FUNCTION FOR DELETING ACCOUNT
def delete(a):
    fs = open("bank-file.bin", "rb")
    lst = []
    try:
        while True:
            global data
            data = pickle.load(fs)
            lst.append(data)
    except EOFError:
        fs.close()
    fs = open("bank-file.bin", "wb")
    for rec in lst:
        if rec[0] == a:
            continue
        pickle.dump(rec, fs)
    fs.close()
    print("Your Account is Deleted\n")
    input("PRESS Enter to go the MAIN MENU")
    return

# MAIN PROGRAM
print("\n\t----------WELCOME----------")
while True:  # Main loop
    ch = int(input("\n\n1.TO CREATE A NEW ACCOUNT :PRESS 1\n2.TO GO TO THE MAIN MENU :PRESS 2   "))
    if ch == 1:
        create_acc()
        wish = int(input("\n1.To Proceed: PRESS 1\n2.To exit PRESS 2\t"))
        if wish == 1:
            print("\n" * 2)
            continue
        else:
            print("\t---------THANK YOU FOR VISITING US----------\n\t--------------HAVE A GOOD DAY---------------")
            input("\nPress ENTER key")
            break
    elif ch == 2:
        while True:  # Menu Loop
            choice = int(input("\n\n\n-------MAIN MENU--------\n\n1.To Print Account Statement-PRESS 1\n2.To Deposit Amount-PRESS 2\n3.To Transact Amount-PRESS 3\n4.To Modify the Account Details PRESS 4\n5.To Delete Account PRESS 5\n6.To Create Account-PRESS 6\n7.To view MASTER BANK DATABASE PRESS 7\n8.To EXIT- PRESS 8\nEnter you choice:\t"))
            if choice == 1:  # TO PRINT STATEMENT
                while True:
                    j = 1
                    acc = int(input("Enter your Account Number: "))
                    fs = open("bank-file.bin", "rb+")
                    try:
                        while True:
                            q = pickle.load(fs)
                            if q[0] == acc:
                                j = pass_word(q)
                                o1 = 0
                                break
                    except EOFError:
                        print("\nInvalid Account Number")
                        inva = int(input("\n1.If you are not registered with us PRESS 1. To create Account\n2.To re-enter your Account Number PRESS 2\t"))
                        if inva == 1:
                            o1 = 1
                        else:
                            o1 = 2
                    if o1 == 0 and j == 1:
                        statement(acc)
                        break
                    elif o1 == 1 or j == 0:
                        break
                    elif o1 == 2:
                        continue
            elif choice == 2:  # TO DEPOSIT AMOUNT
                while True:
                    j = 1
                    acc = int(input("Enter your Account Number: "))
                    fs = open("bank-file.bin", "rb+")
                    try:
                        while True:
                            q = pickle.load(fs)
                            if q[0] == acc:
                                j = pass_word(q)
                                o1 = 0
                                break
                    except EOFError:
                        print("\nInvalid Account Number")
                        inva = int(input("\n1.If you are not registered with us PRESS 1. To create Account\n2.To re-enter your Account Number PRESS 2\t"))
                        if inva == 1:
                            o1 = 1
                        else:
                            o1 = 2
                    if o1 == 0 and j == 1:
                        deposit(acc)
                        break
                    elif o1 == 1 or j == 0:
                        break
                    elif o1 == 2:
                        continue
            elif choice == 3:  # TO TRANSACT AMOUNT
                while True:
                    acc = int(input("Enter your Account Number: "))
                    fs = open("bank-file.bin", "rb+")
                    try:
                        while True:
                            q = pickle.load(fs)
                            if q[0] == acc:
                                j = pass_word(q)
                                o1 = 0
                                break
                    except EOFError:
                        print("\nInvalid Account Number")
                        inva = int(input("\n1.If you are not registered with us PRESS 1. To create Account\n2.To re-enter your Account Number PRESS 2\t"))
                        if inva == 1:
                            o1 = 1
                        else:
                            o1 = 2
                    if o1 == 0 and j == 1:
                        trans_amt(acc)
                        break
                    elif o1 == 1 or j == 0:
                        break
                    elif o1 == 2:
                        continue
            elif choice == 4:  # TO MODIFY ACCOUNT DETAILS
                while True:
                    acc = int(input("Enter your Account Number: "))
                    fs = open("bank-file.bin", "rb+")
                    try:
                        while True:
                            q = pickle.load(fs)
                            if q[0] == acc:
                                j = pass_word(q)
                                o1 = 0
                                break
                    except EOFError:
                        print("\nInvalid Account Number")
                        inva = int(input("\n1.If you are not registered with us PRESS 1. To create Account\n2.To re-enter your Account Number PRESS 2\t"))
                        if inva == 1:
                            o1 = 1
                        else:
                            o1 = 2
                    if o1 == 0 and j == 1:
                        edit(acc)
                        break
                    elif o1 == 1 or j == 0:
                        break
                    elif o1 == 2:
                        continue
            elif choice == 5:  # TO DELETE ACCOUNT
                while True:
                    acc = int(input("Enter your Account Number: "))
                    fs = open("bank-file.bin", "rb+")
                    try:
                        while True:
                            q = pickle.load(fs)
                            if q[0] == acc:
                                j = pass_word(q)
                                o1 = 0
                                break
                    except EOFError:
                        print("\nInvalid Account Number")
                        inva = int(input("\n1.If you are not registered with us PRESS 1. To create Account\n2.To re-enter your Account Number PRESS 2\t"))
                        if inva == 1:
                            o1 = 1
                        else:
                            o1 = 2
                    if o1 == 0 and j == 1:
                        input("To delete your Account PRESS Enter")
                        delete(acc)
                        break
                    elif o1 == 1 or j == 0:
                        break
                    elif o1 == 2:
                        continue
            elif choice == 6:  # TO CREATE ACCOUNT
                o = 0
                break
            elif choice == 7:  # TO SHOW MASTER DATABASE
                ad = input("\nEnter the ADMIN NAME:\t")
                if ad.upper() == "SHIVANSHU YADAV":
                    pin = int(input("Enter the ADMIN PIN:\t"))
                    if pin == 123456789:
                        print("\t\tBANK DATABASE\nS. NO.   A/C NO.\tA/C TYPE\tA/C_HOLDER\tOPEN_AMT   TOTAL_AMT   LAST_DEPO_AMT   LAST_TRANS_AMT\n")
                        fs = open("bank-file.bin", "rb")
                        try:
                            co = 1
                            while True:
                                q = pickle.load(fs)
                                if len(q[2]) <= 12:
                                    g = q[2] + "    "
                                    print(co, "     ", q[0], "     ", q[1], "    ", g, "      ", q[4], "   ", q[5], "    ", q[6], "        ", q[7])
                                else:
                                    print(co, "     ", q[0], "     ", q[1], "    ", q[2], "      ", q[4], "   ", q[5], "    ", q[6], "        ", q[7])
                                co += 1
                        except EOFError:
                            input("Enter any key")
                            fs.close()
                    else:
                        print("The entered PIN is incorrect\nYou are being redirected to MAIN MENU")
                        input("Press Enter key")
                else:
                    print("\nThe entered ADMIN Name is incorrect\nOnly the ADMIN is authorised to view the Bank Database")
                    input("Press Enter to Go to the MAIN MENU")
            elif choice == 8:  # TO EXIT
                print("\t---------THANK YOU FOR VISITING US----------\n\t---------HAVE A GOOD DAY-----------")
                input("Press ENTER key")
                o = 1
                break
            else:
                print("Error occurred\nPlease enter valid content")  # End of Menu Loop
        if o == 0:
            continue
        else:
            break  # End of Main Loop

        

# End of Program