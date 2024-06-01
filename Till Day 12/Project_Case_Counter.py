def case_counter(sentence):
  
  counter = {"Upper":0, "Lower":0}
  lower_letters = []
  upper_letters = [] 
  for letter in sentence:
    if letter.islower():
      counter["Lower"] += 1
      lower_letters.append(letter)
    elif letter.isupper():
      counter["Upper"] += 1
      upper_letters.append(letter) 
    else: 
      pass 
  print(f"Uppercase Letters = {counter['Upper']} , {upper_letters}")
  print(f"Lowercase Letters = {counter['Lower']} , {lower_letters}") 


user_input = input("Enter your sentence below.\n")
case_counter(user_input) 
