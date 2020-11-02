quote = "A person who never made a mistake never tried anything new"
print("Length of quote is: ", len(quote))
print("UPPERCASE quote: ", quote.upper())
print("Title Case of quote: ", quote.title())

# String formatting.
subject_template = "Thanks for learning {} with us {}."
print(subject_template.format("Python", "Animesh"))

buying_template = "You just bought {} {}."
print(buying_template.format(3, "fidget cubes"))

print("Hello" in "Hello, World")

print("Person is present in Quote:", quote.count("person"), "times.")
print(
    "Person is present in Quote at", quote.find("person"), "index."
)  # -1 if not found.
