# Exercise 3: Mobile Contact Update
# Use one update() call to change the phone number and add an email.
# Remove landline using pop(), safely try to remove fax with a default,
# and print the final dictionary.

contact = {
    "name": "Neha Desai",
    "phone": "98250 11111",
    "city": "Surat",
    "landline": "0261-2233445"
}

contact.update({
    "phone": "98250 22222",
    "email": "neha.d@mail.com"
})

print("Updated :", contact)
print("Removed landline:", contact.pop("landline"))
print("Fax       :", contact.pop("fax", "No fax saved"))
print("Final     :", contact)