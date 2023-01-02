import os, time

os.system("cls & mode 140,20 && title [Calculator] ~ github.com/ISROHarsh")
print("""\x1b[34m  
\t\t\t\t\t   ____      _            _       _             
\t\t\t\t\t  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
\t\t\t\t\t | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
\t\t\t\t\t | |__| (_| | | (__| |_| | | (_| | || (_) | |   
\t\t\t\t\t  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|\x1b[0m""")

if int(time.strftime("%H")) <= 12:
    print("\n[\x1b[34m#\x1b[0m] Good moring sir, Let's do some calculations")

elif int(time.strftime("%H")) < 18:
    print("\n[\x1b[34m#\x1b[0m] Good afternoon sir, let's do some calculations")

else:
    print("\n[\x1b[34m#\x1b[0m] Good evening sir, let's do some calculations")

print("""
[\x1b[34m1\x1b[0m]  +  For additon
[\x1b[34m2\x1b[0m]  -  For subtraction
[\x1b[34m3\x1b[0m]  *  For multiplication
[\x1b[34m4\x1b[0m]  /  For division
[\x1b[34m5\x1b[0m]  // For floor division
[\x1b[34m6\x1b[0m]  ** For exponent
[\x1b[34m7\x1b[0m]  Q To quit the program 
""")

while True:
    try:
        choice = int(input("[\x1b[34m?\x1b[0m] Enter your choice: "))
        if choice in [1, 2, 3, 4, 5, 6, 7]:
            if choice == 1:
                num_one = int(input("[\x1b[33m>\x1b[0m] Enter first number: "))
                num_two = int(input("[\x1b[33m>\x1b[0m] Enter second number: "))
                print("[\x1b[32m>\x1b[0m] Result:", num_one + num_two)

            elif choice == 2:
                num_one = int(input("[\x1b[33m>\x1b[0m] Enter first number: "))
                num_two = int(input("[\x1b[33m>\x1b[0m] Enter second number: "))
                print("[\x1b[32m>\x1b[0m] Result:", num_one - num_two)

            elif choice == 3:
                num_one = input("[\x1b[33m>\x1b[0m] Enter first number: ")
                num_two = input("[\x1b[33m>\x1b[0m] Enter second number: ")
                print("[\x1b[32m>\x1b[0m] Result:", num_one * num_two)

            elif choice == 4:
                divident = int(input("[\x1b[33m>\x1b[0m] Enter divident: "))
                divisor = int(input("[\x1b[33m>\x1b[0m] Enter divisor: "))
                print("[\x1b[32m>\x1b[0m] Quotient:", divident / divisor)

            elif choice == 5:
                divident = int(input("[\x1b[33m>\x1b[0m] Enter dividend: "))
                divisor = int(input("[\x1b[33m>\x1b[0m] Enter divisor: "))
                print("[\x1b[32m>\x1b[0m] Result:", divident // divisor)

            elif choice == 6:
                base_value = int(input("[\x1b[33m>\x1b[0m] Enter base value: "))
                exp_power = int(input("[\x1b[33m>\x1b[0m] Enter exponential power: "))
                print("[\x1b[32m>\x1b[0m] Result:", base_value ** exp_power) 

            elif choice == 7:
                print("[\x1b[34m#\x1b[0m] Thanks for using the calculator :)")
                quit() 
        else:
            print("[\x1b[31m!\x1b[0m] Please enter a valid choice")
    except ValueError:
        chararray = [67,104,117,116,105,121,97,32,104,97,105,32,107,121,97,32,44,32,69,110,116,101,114,32,97,32,73,110,116,101,103,101,114,32,118,97,108,117,101,33]
        error = "".join(chr(i) for i in chararray)
        print(f"[\x1b[31m!\x1b[0m] {error}")