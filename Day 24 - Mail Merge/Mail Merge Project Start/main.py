#TODO: Create a letter using starting_letter.txt
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as l:
    email = l.read()

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.

with open("../Mail Merge Project Start/Input/names/invited_names.txt") as n:
    names = n.readlines()
    print(names)

for name in names:
    strip_name = name.strip()
    finish_email = email.replace("[name]", strip_name)
    print(finish_email)
    with open(f"../Mail Merge Project Start/output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as completed_letter:
        completed_letter.write(finish_email)



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp