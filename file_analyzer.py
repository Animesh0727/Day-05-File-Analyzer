print("==============================")
print("        FILE ANALYZER")
print("==============================")

print("Welcome to the File Analyzer!")
try:
    with open("sample.txt", "r") as file:
        content = file.read()

    print()
    print("File loaded successfully!")

except FileNotFoundError:
    print("Error: sample.txt was not found.")
    exit()
lines = content.splitlines()

total_lines = len(lines)

print("Total Lines:", total_lines)
words = content.split()

total_words = len(words)

print("Total Words:", total_words)
characters = len(content)

print("Total Characters:", characters)
print()
search_word = input("Enter a word to search: ")

count = content.lower().count(search_word.lower())

print("Word found", count, "time(s).")
average_words = total_words / total_lines

print("Average Words per Line:", round(average_words, 2))

print()
print("====================================")
print("          FILE ANALYSIS REPORT")
print("====================================")

print("Total Lines:", total_lines)
print("Total Words:", total_words)
print("Total Characters:", characters)
print("Average Words per Line:", round(average_words, 2))
print("Search Word:", search_word)
print("Search Count:", count)

print("====================================")
print("        Analysis Completed!")
print("====================================")