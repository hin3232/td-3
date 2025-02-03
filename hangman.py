
import random
Insects = ["ant", "bug", "bee", "fly", "mosquito", "grasshopper", "butterfly", "dragonfly", "beetle", "cockroach"]
fruits = ["apple", 'banana', 'grape', 'mango', 'orange', 'pear', 'peach', 'watermelon', 'kiwi', 'cherry']
Professions = ['engineer', 'pilot', 'teacher', 'doctor', 'nurse', 'scientist', 'lawyer', 'actor', 'chef', 'photographer']
animals = ['lion', 'frog', 'goat', 'wolf', 'elephant', 'tiger', 'giraffe', 'bear', 'kangaroo', 'zebra']
vegetable = ['onion', 'pepper', 'tomato', 'corn', 'carrot', 'broccoli', 'spinach', 'cucumber', 'lettuce', 'potato']

def start():
 print("""\n1:Insects 🐜🐛🐝🪰\n2:fruits🍎🍌🍇🥭 \n3:Professions👷‍♂️👨‍✈️👩‍🏫👨‍⚕️\n4:animals🦁🐸🐐🐺\n5:vegetable🧅🌶️🍅🌽\n don't enter the same letter\n❌❌❌❌❌ Be careful your attempts are 6❌❌❌❌❌\n""")
 fields=input("Choose one of this fields\n")
 try :
    fields=int(fields)
 except ValueError:
    print("Invalid input, please enter a number between 1 and 5\n")
    return start()
 def the_fields (fields):
    match fields :
        case 1:
            return random.choice(Insects)
        case 2:
            return random.choice(fruits)
        case 3:
            return random.choice(Professions)
        case 4:
            return random.choice(animals)
        case 5:
            return random.choice(vegetable)
        case _:
            print("Invalid input\n")
            return start()

 the_word=the_fields(fields)
 the_word_gussed=["__"]*len(the_word)
 attempts=6
 while attempts>0 and "__" in the_word_gussed:
  print(f"{" ".join(the_word_gussed)}\n")
  the_guss=input(" Enter your gusse:\n").lower()
  if len(the_guss)!=1:
    print(" One letter 🧏🏻‍♀️🧏🏻‍♀️🧏🏻‍♀️🧏🏻‍♀️🧏🏻‍♀️\n")
    continue
  if the_guss in the_word and the_guss not in "".join(the_word_gussed):
   for i in range(len(the_word)):
      if the_word[i] == the_guss:
          the_word_gussed[i]=the_guss
          print("✅\n")
      else:
         print ("❌\n")
      
  else:
     attempts-=1
     print(f" You have {attempts} attempts left ⌛️👀⌛️👀⌛️👀 \n")
     if attempts==5:
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========\n''')
     elif attempts==4:
        print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========\n''')
     elif attempts==3:
        print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========\n''')
     elif attempts==2:
        print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========\n''')
     elif attempts==1:
        print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========\n''')
     
 if "__" not in the_word_gussed:
   print ("you won 🫶🏾🫶🏾🫶🏾\n")
   print(the_word )
 else:
   print(" you lost 🤭🤭🤭\n")
   print ('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\n''')
   print(" Oops you died 🪦🪦🪦\n")
   
start()
def aginn():
 again=input("Do you want to play again? (yes or no )").lower()
 if again=="yes":
   start()
 elif again=="no":
   print("Bye bye little boy 👋🏽👋🏽👋🏽\n")
   exit()
 else:
   print(" you can't even right yes or no ?? brah 🤡🤡🤡\n")
   aginn()
aginn()




