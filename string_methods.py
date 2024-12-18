# Define a sample string
my_string = "  Hello, Python! This is a String example.  "

# 1. strip() - Removes leading and trailing whitespace
print(my_string.strip())

# 2. lstrip() - Removes leading (left-side) whitespace
print(my_string.lstrip())

# 3. rstrip() - Removes trailing (right-side) whitespace
print(my_string.rstrip())

# 4. lower() - Converts the string to lowercase
print(my_string.lower())

# 5. upper() - Converts the string to uppercase
print(my_string.upper())

# 6. capitalize() - Capitalizes the first character of the string
print(my_string.capitalize())

# 7. title() - Converts the string to title case
print(my_string.title())

# 8. swapcase() - Swaps the case of each character
print(my_string.swapcase())

# 9. replace() - Replaces a substring with another substring
print(my_string.replace("Python", "World"))

# 10. split() - Splits the string into a list based on a delimiter
print(my_string.split())  # Default delimiter is whitespace

# 11. join() - Joins elements of a list into a string with a specified separator
words = ["Hello", "World"]
print(", ".join(words))

# 12. find() - Returns the first occurrence of a substring, or -1 if not found
print(my_string.find("Python"))

# 13. rfind() - Returns the last occurrence of a substring, or -1 if not found
print(my_string.rfind("a"))

# 14. index() - Like find(), but raises ValueError if not found
print(my_string.index("Python"))

# 15. count() - Counts the number of occurrences of a substring
print(my_string.count("is"))

# 16. startswith() - Checks if the string starts with a specific substring
print(my_string.startswith("Hello"))

# 17. endswith() - Checks if the string ends with a specific substring
print(my_string.endswith("example."))

# 18. isalpha() - Checks if all characters are alphabetic
print("Python".isalpha())

# 19. isdigit() - Checks if all characters are digits
print("12345".isdigit())

# 20. isalnum() - Checks if all characters are alphanumeric
print("Python123".isalnum())

# 21. isspace() - Checks if the string contains only whitespace
print("   ".isspace())

# 22. isnumeric() - Checks if the string contains only numeric characters
print("12345".isnumeric())

# 23. islower() - Checks if all characters are lowercase
print("python".islower())

# 24. isupper() - Checks if all characters are uppercase
print("PYTHON".isupper())

# 25. zfill() - Pads the string with zeros to the left to reach the specified width
print("123".zfill(5))

# 26. center() - Centers the string within the specified width
print(my_string.center(50, "-"))

# 27. ljust() - Left-justifies the string within the specified width
print(my_string.ljust(50, "-"))

# 28. rjust() - Right-justifies the string within the specified width
print(my_string.rjust(50, "-"))

# 29. encode() - Encodes the string using the specified encoding
print(my_string.encode("utf-8"))

# 30. format() - Formats the string using placeholders
name = "Nikan"
age = 20
print("My name is {} and I am {} years old.".format(name, age))

# 31. f-string - String interpolation (introduced in Python 3.6)
print(f"My name is {name} and I am {age} years old.")

# 32. partition() - Splits the string at the first occurrence of a substring
print(my_string.partition("Python"))

# 33. rpartition() - Splits the string at the last occurrence of a substring
print(my_string.rpartition("is"))

# 34. splitlines() - Splits the string into a list at line breaks
multi_line_string = "Hello\nPython\nWorld"
print(multi_line_string.splitlines())

# 35. casefold() - Converts the string to lowercase, more aggressive than lower()
print("ß".casefold())  # German character example