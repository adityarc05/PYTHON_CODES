import pickle

options = "1. Adding Pass to secure\n, 2. Setting security pass\n, 3. Show passwords\n, 4. Exit"

print(options)

opt_1 = int(input("Enter the options 1, 2, 3, 4 : "))

if opt_1 == 1:
    str_1 = input("Enter the password in foramt 'platform - password' :")
    a = open("pass_data.dat", "wb")
    pickle.dump(str_1,a)
    print("PASS SECURED")
    a.close()

elif opt_1 == 2:
    password_sec = input("Enter the security pass : ")
    b = open("opening_pass_dat.dat", "wb")
    pickle.dump(password_sec, b)
    print("Password is set")
    b.close()

elif opt_1 == 3:
    print("Please ensure that you have entered your password correctly ")
    a = open("pass_data.dat", "rb")
    b = open("opening_pass_dat.dat", "rb")
    passwords = pickle.load(a)
    pass_sec = pickle.load(b)
    input_pass_sec = input("Enter the security pass :")
    if input_pass_sec == pass_sec :
        print(passwords)
    else:
        print("Incorrect password")
    a.close()
    b.close()
else:
    print("")