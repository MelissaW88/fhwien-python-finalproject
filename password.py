import random
import string

#function that creates the password
def generate_password(min_length, digits=True, special_characters=True):
    #get all upper and lower case letters
    letters = string.ascii_letters
    #get all digits from 0-9
    digits = string.digits
    #get all special characters
    special = string.punctuation

    #start with numbers as the base
    characters = letters
    if digits:
        characters += digits #include digits if true
    if special_characters:
        characters += special #include special characters if true

    #empty string to store the password
    pwd = ""
    meets_criteria = False #track if the password meets all criteria
    has_digits = False     #track if the password has at least one digit
    has_special = False    #track if the password has at least one special character

    #loop that creates passwords until they meet all the criteria
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters) #select random character from the available characters
        pwd += new_char                      #add character to the password

        if new_char in digits:
            has_digits = True         #set the has_digits to True if the new character is a digit
        elif new_char in special:
                has_special = True    #set the has_special to True if the new character is a special character

        #checking if the criteria is met or not with meets_extra_criteria cause only digits and specials are checked
        meets_extra_criteria = True
        if digits:
            meets_criteria = has_digits    #check if the password has at least one digit
        if special_characters:
            meets_criteria = meets_criteria and has_special  #check if the password has at least one special character

    return pwd

#use an extra function run () to only run the code, if the script is executed directly and prevents to execute the code when file is imported from elsewhere
def run ():
    #ask user to give us information about the wanted password
    min_length = int(input("Please enter the minimum length in digit form to get a password: "))
    has_digits = input ("Do you want to have numbers (y/n)? ").lower() == "y"
    has_special = input ("Do you want to have special character (y/n)?").lower() == "y"
    #generate and print the password with the wanted criteria
    pwd = generate_password(min_length, has_digits, has_special)
    print("The generated password is: ", pwd)

    #Save the password to a file, usually not save to save a file in text file, but for this exercise we wanted to try the code try-except
    file_name = input ("Please enter the file name to save the password: ")

    #handle with try-except if any errors may occur while saving
    try:
        with open(file_name, "w") as file: #open file in write mode
            file.write(pwd) #written to the file
        print("Password saved successfully.")
    #with as e the user can know why the error occured    
    except IOError as e:
        print(f"An error occurred while saving the password: {e.args}")
        
if __name__ == '__main__':
    run()
