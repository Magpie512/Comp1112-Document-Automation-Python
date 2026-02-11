import re # Regex library for pattern matching
import pyinputplus as pyip # (nickname)

# Our master list to store each person's data
database = []

while True:
    print("\n--- DATABASE MENU ---")
    menu_choice = pyip.inputMenu(['Add Person', 'Search Database', 'Exit'], numbered=True)

    if menu_choice == 'Add Person':
        # 1 & 2. Names (Ensuring Title Case)
        first_name = pyip.inputStr("First Name: ").strip().title()
        last_name = pyip.inputStr("Last Name: ").strip().title()
        
        # 3. Age (Ensuring Integer)
        age = pyip.inputInt("Age: ")
        
        # 4. DOB (Regex using \d shorthand for numeric digits)
        # Your slides show \d represents any numeric digit from 0 to 9
        dob_pattern = r'^\d\d/\d\d/\d\d\d\d$'
        dob = pyip.inputRegex(dob_pattern, prompt="DOB (MM/DD/YYYY): ")
        
        # 5. City (Title Case)
        city = pyip.inputStr("City: ").strip().title()
        
        # 6. Street Address (## street name)
        # Using \d+ for digits and \s for the space as shown in your character classes
        address_pattern = r'^\d+\s\w+'
        address = pyip.inputRegex(address_pattern, prompt="Street Address (e.g. 123 Main): ")
        
        # 7. Postal Code
        postal = pyip.inputStr("Postal Code: ")
        
        # 8. Preferred Mode of Communication (Menu)
        comm = pyip.inputMenu(['Email', 'Phone', 'Post'], prompt="Preferred Communication:\n")
        
        # 9. Email Address
        email = pyip.inputEmail("Email: ")
        
        # 10. Password (Strength check: must contain at least one digit \d)
        pass_pattern = r'^.*?\d.*$'
        password = pyip.inputRegex(pass_pattern, prompt="Password (must include at least one number): ")

        # Storing the information in a list instead of a dictionary
        # Index order: 0:fname, 1:lname, 2:age, 3:dob, 4:city, 5:address, 6:postal, 7:comm, 8:email
        new_record = [first_name, last_name, age, dob, city, address, postal, comm, email]
        database.append(new_record)
        print("Record successfully added to the master list.")

    elif menu_choice == 'Search Database':
        # Search by first and last name
        search_f = pyip.inputStr("Enter First Name to search: ").title()
        search_l = pyip.inputStr("Enter Last Name to search: ").title()
        
        found_it = False
        for person in database:
            # Checking the first (0) and second (1) items in the nested list
            if person[0] == search_f and person[1] == search_l:
                # Formatting using escape characters \n and \t
                # Using concatenation (+) instead of f-strings
                print("\n--- RECORD DATA ---")
                print("First Name:\t" + person[0])
                print("Last Name:\t" + person[1])
                print("Age:\t\t" + str(person[2]))
                print("DOB:\t\t" + person[3])
                print("City:\t\t" + person[4])
                print("Address:\t" + person[5])
                print("Email:\t\t" + person[8])
                print("Comm Pref:\t" + person[7])
                found_it = True
        
        if not found_it:
            print("No matching records were discovered.")

    elif menu_choice == 'Exit':
        print("Closing the ledger. Goodbye.")
        break