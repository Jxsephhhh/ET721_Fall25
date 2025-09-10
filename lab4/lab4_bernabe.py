"""
Joseph Bernabe
Lab 4, Dictionary Functions
Sep 10, 2025
"""
print("\n---------- Example 1: Dictionary ----------")
# Contact dictionary with three different users
contacts = {
    "Bill" : "718-111-2222",
    "Martha" : "646-000-3333",
    "Peter" : "212-000-1111"
}
print(contacts)

# Save a specific value of a key
user1 = contacts["Martha"]
print(f"User's phone number = {user1}")

# Add content to the dictionary
contacts["Anna"] = "646-222-3333"
print(contacts)

# Update value of a specific key
contacts["Peter"] = "800-000-0000"
print(contacts)

print("\n---------- Example 2: Loop through a dictionary ----------")
# Print each key in the dictionary
for i in contacts:
    print(i)

# Print each value in the dictionary
for i in contacts:
    print(contacts[i])

# Print each key:value set in the dictionary
for i in contacts:
    print(f"{i} = {contacts[i]}")

print("\n---------- Example 3: Length of the dictionary ----------")
print(f"Dictionary has {len(contacts)} users")

print("\n---------- Example 4: Copy a dictionary ----------")
contacts_copy1 = contacts.copy()
contacts_copy2 = dict(contacts)
print(contacts_copy1)
print(contacts_copy2)

print("\n---------- Example 5: Remove a key:value pair in a dictionary ----------")
print(contacts)
contacts.pop("Peter")
print(contacts)

print("\n---------- Example 6: Add a new key:value pair in a dictionary ----------")
print(contacts)
contacts.update({"Lucas":"212-111-1111"})
print(contacts)

print("\n---------- Example 7: Return items, keys, and values in a dictionary ----------")
print(f"Return items = {contacts.items()}")
print(f"Return keys = {contacts.keys()}")
print(f"Return values = {contacts.values()}")

print("\n---------- Example 8: Dictionary application ----------")
# store in a dictionary the count of occurency of the words in a phrase
phrase = "To be or not to be"
list_phrase = phrase.split()
# create an empty dictionary 
word_count_dictionary = {}
for word in list_phrase:
    if word in word_count_dictionary:
        word_count_dictionary[word] += 1
    else:
        word_count_dictionary[word] = 1

# Print result
for word in word_count_dictionary:
    print(f"{word} appears {word_count_dictionary[word]}")

print("\n---------- EXERCISE ----------")
users = ["peterpan@yahoo.com", "annie@hotmail.com", "Carl@hotmail.com", "martha@gmail.com", "cassie@yahoo.com", "Josue@hotmail.com", "John@hotmail.com"]

email_count = {}

for email in users:
    if "gmail" in email:
        if "gmail" in email_count:
            email_count["gmail"] += 1
        else:
            email_count["gmail"] = 1
    elif "hotmail" in email:
        if "hotmail" in email_count:
            email_count["hotmail"] += 1
        else:
            email_count["hotmail"] = 1
    elif "yahoo" in email:
        if "yahoo" in email_count:
            email_count["yahoo"] += 1
        else:
            email_count["yahoo"] = 1

for provider in email_count:
    print(f"{provider} users = {email_count[provider]}")