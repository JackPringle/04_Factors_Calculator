# Functions go here

# Puts a series of symbols at start and end of text
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions ():

    statement_generator("Instructions / Information", "=")
    print()
    print("This program finds all the factors of a given integer that is more than, or equal to 1, and less than, or equal to 200. ")
    print()
    print("NOTE: Integer must be a whole number!")
    print()
    print("Enter an integer, and the program will display all of its factors in an ordered list. ")
    print()
    print("This program can tell you if your integer is a perfect square, is a prime number, or is UNITY.")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculaton or any key to quit.")
    print()
    print("Enjoy!")
    print()
    print("-" * 50)
    print()
    return ""

    instructions()



# checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a integer that is more than (or equal to) 1 and less than (or equal to) 200"

        try:

            # ask user to enter a number 
            response = int(input(question))

            # checks number is more than, or equal to, one
            if 1 <= response <= 200 :
                return response
            

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error) 
            print()



# gets factors, returns a sorted list
def get_factors(to_factor):
    # list to hold factors
    factors_list = []

    # Square root to_factor to find 'half way' 
    limit = int(to_factor ** 0.5)

    # find factor pairs and add to list
    for item in range (1, limit + 1):

        #check factor is not 1 (unity)
        if to_factor == 1:
            break

        # check if number is a factor
        result = to_factor % item
        factor_1 = int(to_factor // item)

        # add factor to list if it is not already in there 
        if result == 0: 
            factors_list.append(item)
        
        if factor_1 != item and result == 0:
                factors_list.append (factor_1)

    # output
    factors_list.sort()
    return(factors_list)





# Main Routine goes here

# Heading 
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input ("Press <enter> to see the instructions or any key to continue")
if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor.  Itself ;)"

    # comments for squares / primes 
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
    
    # output factors and comment 

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is speacial..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator!")
print()