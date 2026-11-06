# Import Python's regular expression module.
import re

# Create an empty list to store all extracted names.
names_all = []

# Create an empty list to store all extracted email addresses.
emails_all = []

# Define a function to extract names and email addresses from email text.
# email_text is the file object containing the email content.
def collect_contact_info(email_text):

    # Define a regular expression to identify lines beginning with "From:" or "To:".
    # ^ means the beginning of the line.
    # (From:)|(To:) means either "From:" or "To:".
    # The parentheses create two alternative groups.
    contact_line_pattern = r"^(From:)|(To:)"

    # Read the email file one line at a time.
    for line in email_text:

        # Search for "From:" or "To:" at the beginning of the line.
        # re.search() returns a match object if a match is found, or None otherwise.
        contact_search_res = re.search(contact_line_pattern, line)

        # Extract contact information only if the line matches the pattern.
        if contact_search_res is not None:
            # The contact info is always presented in the format "Name1 <email1>; Name2 <email2>..."

            # Define a regular expression to extract the contact name.
            # [:;] matches either a colon or a semicolon.
            # \s matches one whitespace character.
            # (.+?) captures one or more characters non-greedily as Group 1.
            # \s< matches a whitespace character followed by a literal "<".
            # The captured name is expected to appear between the colon/semicolon
            # and the opening angle bracket.
            name_pattern = r"[:;]\s(.+?)\s<"

            # Find all substrings matching the name pattern.
            # re.findall() returns a list containing the captured names.
            name_search_res = re.findall(name_pattern, line)

            # Define a regular expression to extract the email address.
            # < and > match literal angle brackets.
            # (.+?) captures the characters between the brackets non-greedily.
            email_pattern = r"<(.+?)>"

            # Find all substrings matching the email pattern.
            # The captured email addresses are returned as a list.
            email_search_res = re.findall(email_pattern, line)

            # Add all extracted names to the names_all list.
            # extend() adds each item from the returned list individually.
            names_all.extend(name_search_res)

            # Add all extracted email addresses to the emails_all list.
            emails_all.extend(email_search_res)

# Use range(1, 6) to generate the numbers 1, 2, 3, 4, and 5.
# Each number corresponds to one of the five email sample files.
for n in range(1, 6):

    # Construct the filename by combining the fixed text with the current number.
    # str(n) converts the integer into a string for concatenation.
    filename = "email-sample-" + str(n) + ".txt"

    # Open the corresponding email file for reading using UTF-8 encoding.
    email_reader = open("sources/" + filename, encoding = "utf-8")

    # Pass the open file object to the function for contact information extraction.
    collect_contact_info(email_reader)

# Print the list containing all extracted names.
print(names_all)

# Print the list containing all extracted email addresses.
print(emails_all)

# Pair the names and email addresses by their corresponding positions.
# zip() produces pairs such as ("Emily Carter", "emily.carter@ue.edu").
contact_info_tup = zip(names_all, emails_all)

# Create an empty dictionary to store names and their email addresses as key-value pairs,
# so we can retrieve an email address (value) by a name (key).
contact_info_dict = {}

# Go through the name-email pairs one at a time.
# Each pair is unpacked into the variables name and email.
for name, email in contact_info_tup:

    # Add the name as a dictionary key and the email address as its value.
    # If a name already exists, its previous email address will be replaced.
    contact_info_dict[name] = email

# Print the complete dictionary of names and email addresses.
print(contact_info_dict)

# Look up and print the email address associated with "Emily Carter".
print(contact_info_dict["Emily Carter"])
# This will lead to an error since the name does not exist as a key in the
# dict object. You can try to Google for error handler in Python to see
# how to take different actions depending on whether there is an error or not.
# print(contact_info_dict["TY Chen"])