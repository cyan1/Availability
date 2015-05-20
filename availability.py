# Author: Chad Yan
# Description: This program calculates system availability of parallel components using N out of H equations
#              where N is the number of components needed to be up and H is the total number of system components.

import math

# menu() prints out program usage
# Inputs: none
# Outputs: none 
def menu():
    print("Calculate availability by using:\n  1. Individual component availability\n  2. MTBF and MTTR\n")

# combin() computes the combination formula
# Inputs: the total number of objects (n) and the number of chosen objects (k)
# Outputs: the number of combinations of k objects out of a total of n objects
def combin(n, k):
    return math.factorial(n) / math.factorial(k) / math.factorial(n - k)
 
# mtbfConfig() computes the mean time between failure for the entire system configuration
# Inputs: MTBF and MTTR for a single component, the total number of components, and the number of components needed to be up
# Outputs: the mean time between failure for the entire configuration
def mtbfConfig(mtbf, mttr, have, need):
    sum = 0.0
    for i in range(need, have + 1):
        sum += combin(have, i) * mtbf**i * mttr**(have - i)
    denominator = have * combin(have - 1, need - 1) * mtbf**(need - 1) * mttr**(have - need)
    return sum / denominator

# mttrConfig() computes the mean time to repair for the entire system configuration
# Inputs: MTBF and MTTR for a single component, the total number of components, and the number of components needed to be up
# Outputs: the mean time to repair for the entire configuration
def mttrConfig(mtbf, mttr, have, need):
    sum = 0.0
    for i in range(need):
        sum += combin(have, i) * mtbf**i * mttr**(have - i)
    denominator = have * combin(have - 1, need - 1) * mtbf**(need - 1) * mttr**(have - need)
    return sum / denominator

# availabilityMean() computes the availability of the entire configuration using the MTBF and MTTR of a single component
# Inputs: the MTBF and MTTR for a single component, the total number of system components, and the number of components needed to be up
# Outputs: the availability for the entire configuration
def availabilityMean(mtbf, mttr, have, need):
    sum1 = 0.0
    sum2 = 0.0
    for i in range(need, have + 1):
        sum1 += combin(have, i) * mtbf**i * mttr**(have - i)
    for i in range(have + 1):
        sum2 += combin(have, i) * mtbf**i * mttr**(have - i)
    return sum1 / sum2

# availability() computes the availability of the entire configuration using the availability of a single component
# Inputs: the availability of a single component as a number in the open interval [0,1), the total number of system components,
# and the number of components needed to be up
# Outputs: the availability for the entire configuration
def availability(avail, have, need):
    sum1 = 0.0
    sum2 = 0.0
    for i in range(need, have + 1):
        sum1 += combin(have, i) * avail**i * (1 - avail)**(have - i)
    for i in range(have + 1):
        sum2 += combin(have, i) * avail**i * (1 - avail)**(have - i)
    return sum1 / sum2

# option1() gathers user input used to calculate and print the availbility of the configuration
# Inputs: none
# Outputs: none
def option1():
    avail = float(input("Enter component availability: "))
    have = int(input("Enter the total number of system components: "))
    need = int(input("Enter the number of components that need to be up: "))
    print("\nOutput Statistics:\nAvailability of configuration: {:02.10f}\n".format(availability(avail, have, need)))

# option2() gathers user input used to calculate the availability, MTBF, and MTTR of the configuration
# Inputs: none
# Outputs: none
def option2():
    mtbf = float(input("Enter the MTBF for a single component: "))
    mttr = float(input("Enter the MTTR for a single component: "))
    have = int(input("Enter the total number of system components: "))
    need = int(input("Enter the number of components that need to be up: "))
    print("\nOutput Statistics:\nAvailability of configuration: {:02.10f}".format(availabilityMean(mtbf, mttr, have, need)))
    print("MTBF of configuration: {:02.10f}".format(mtbfConfig(mtbf, mttr, have, need)))
    print("MTTR of configuration: {:02.10f}\n".format(mttrConfig(mtbf, mttr, have, need)))

# main() is the entry point of the program
# Inputs: none
# Outputs: none
def main():
    print("\nAvailabilityCalculator\n")
    menu()
    userInput = input("Enter your selection, or 'q' to quit: ") 
    while (userInput != "q"):
        if (userInput == "1"):
            option1()
        elif (userInput == "2"):
            option2()
        else:
            print("Invalid menu option.\n")
        menu()
        userInput = input("Enter your selection, or 'q' to quit: ") 
    
# Execute program
main()
