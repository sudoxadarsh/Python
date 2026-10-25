"""

Exception Hanlding is used to manage runtime errors and prevent a
program from terminating unexpedtedly.

Python use try, except, else, and finally.
"""

"""

try: Contains code that may cause an exception.

except: Handles an exception.

else: Executes if no exception occurs.

finally: Executes whether an exception occurs or not.

"""



try:
    a = int(input("Enter a number: "))
    print(10 / a)
except Exception as e:
    print(f"{e}")
finally:
    print("Khatam tata bye bye,....goodbye gya hogya jao na yrr")