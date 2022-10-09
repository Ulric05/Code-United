#--Enter the Phrase--

user_input = str(input("Enter a Phrase: "))

#--Uses the 1st letter as the Alphabet--

text = user_input.split()

a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
