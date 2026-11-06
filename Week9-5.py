import re

names_all = []
emails_all = []

def collect_contact_info(email_text):
    contact_line_pattern = r"^(From:)|(To:)"
    for line in email_text:
        contact_search_res = re.search(contact_line_pattern, line)
        if contact_search_res is not None:
            name_pattern = r"[:;]\s(.+?)\s<"
            name_search_res = re.findall(name_pattern, line)
            email_pattern = r"<(.+?)>"
            email_search_res = re.findall(email_pattern, line)
            names_all.extend(name_search_res)
            emails_all.extend(email_search_res)

for n in range(1, 6):
    filename = "email-sample-" + str(n) + ".txt"
    email_reader = open("sources/" + filename, encoding = "utf-8")
    collect_contact_info(email_reader)

print(names_all)
print(emails_all)

contact_info_tup = zip(names_all, emails_all)

contact_info_dict = {}

for name, email in contact_info_tup:
    contact_info_dict[name] = email

print(contact_info_dict)
print(contact_info_dict["Emily Carter"])
# print(contact_info_dict["TY Chen"])