def chatbot(username):  
 while True:
  print("#*30")
  print(f"1.hello?")
  print(f"2.how are you?")
  print(f"3.bye?")
request = int(input("Enter your choice:"))
match request:
    case 1:
        print("hello sumanth")
    case 2:
        print(f"hi,i'm fine,thanks!")
    case 3:
        print(f"Good bye!")
    case _:
        print("Invalid option")
cont = input("Do you want to continue the chat?[y/n]: ")
if(cont == 'n'):
    print("Thankyou!!")  

def main():
 username="harish"
 print(f"welcome {username} how can i help you?")

 chatbot(username)
 
 main()
