class User:
    def __init__(self, name, id, address, contactno, password, email):
        self.name = name
        self.id= id
        self.address = address
        self.contactno = contactno
        self.password = password
        self.email = email

class FoodDeliverySystem:
    def __init__(self):
        self.users = {}

    def login_user(self):
        print("Enter the user details entered during registration to proceed with login ")
        s=input("For login via contact number enter 1 \n for login via email enter 2:\n")
        if s=="1":
            contactno= input("Enter contact number: ")
            password = input("Enter password: ")
            user = self.users.get(contactno)
        else:
            email= input("Enter email id: ")
            password = input("Enter password: ")
            user = self.users.get(email)


        if user and user.password == password:
            print("Login successful!\n")
        else:
            print("Invalid id or password!\n")
            c=print("Enter 1 to register first or 2 to enter valid credentials")
            if c=="1":
                self.register_user()
            else:
             self.login_user()

    def register_user(self):
        print("Enter the user details to register")
        
        while True:
            try:
                name = input("Enter name: ")
                if not name.isalpha():
                    print("Name should only contain alphabets. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please try again.")
        
        while True:
            try:
                id = int(input("Enter id: "))
                break
            except ValueError:
                print("ID should be an integer. Please try again.")
        
        while True:
            address = input("Enter address: ")
            if address.strip() == "":
                print("Address cannot be empty. Please try again.")
                continue
            break
        
        while True:
            contactno = input("Enter contactno: ")
            if not contactno.isdigit() or len(contactno) != 10:
                print("Contact number should be a 10 digit number. Please try again.")
                continue
            break
        
        while True:
            password = input("Enter password: ")
            if len(password) < 8:
                print("Password should be at least 8 characters long. Please try again.")
                continue
            break
        
        while True:
            email = input("Enter email: ")
            if "@" not in email or "." not in email:
                print("Invalid email. Please try again.")
                continue
            break
        
        user = User(name, id, address, contactno, password, email)
        self.users[contactno] = user
        self.users[email] = user

        print("Registration successful proceed to login")
        self.login_user()

   
        
    def browse_items(self):
        restaurants = [
        {"name": "BrikOven", "menu": [{"item": "Hawaiian pizza", "price": 10.99}, {"item": "Iced tea", "price": 1.99}, {"item": "Meatball sub", "price": 12.99}, {"item": "Greek salad", "price": 9.99}]},
        {"name": "Ishaara", "menu": [{"item": "Aloo paratha", "price": 8.99}, {"item": "Biryani", "price": 12.99}, {"item": "Butter chicken", "price": 14.99}, {"item": "Naan", "price": 2.99}]},
        {"name": "TastyTacos", "menu": [{"item": "Veg taco", "price": 2.99}, {"item": "Veggie burrito", "price": 7.99}, {"item": "Guacamole", "price": 3.99}, {"item": "Quesadilla", "price": 8.99}]},
        {"name": "SushiHut", "menu": [{"item": "Salmon sushi", "price": 14.99}, {"item": "Miso soup", "price": 2.99}, {"item": "Edamame", "price": 4.99}, {"item": "California roll", "price": 12.99}]},
        {"name": "BurgerBarn", "menu": [{"item": "Classic cheeseburger", "price": 9.99}, {"item": "Fries", "price": 3.99}, {"item": "Milkshake", "price": 5.99}, {"item": "Chicken sandwich", "price": 10.99}]}
    ]

        for restaurant in restaurants:
            print(f"Menu for {restaurant['name']}:")  # Print the restaurant name
            for item in restaurant["menu"]:
                print(f"- {item['item']}: ${item['price']}")  # Print the menu items with prices
        
        d=input("Enter 1 to add to cart and 2 to exit\n")
        if d=="1":
            restaurant_name = input("Enter restaurant name: ")
            item_name = input("Enter item name: ")
            self.add_to_cart(cart, restaurant_name, item_name, restaurants)
            self.browse_items()
        elif d=="2":
            return
        else:
            print("Please enter a valid option")
            self.browse_items()
            
    def add_to_cart(self,cart, restaurant_name, item_name, restaurants):
        for restaurant in restaurants:
            if restaurant["name"] == restaurant_name:
                for item in restaurant["menu"]:
                    if item["item"] == item_name:
                        cart.append({"item": item["item"], "price": item["price"]})
                        print(f"{item['item']} from {restaurant_name} added to cart.")
                        return
                        
        print("Item not found.")

    def view_cart(self,cart):
        if not cart:
            print("Your cart is empty.")
        else:
            print("Your cart:")
            for item in cart:
                print(f"- {item['item']}: ${item['price']}")

    def place_order(self,cart):
        total = sum(item["price"] for item in cart)
        print("Your order:")
        for item in cart:
            print(f"- {item['item']}: ${item['price']}")
        print(f"Total: ${total:.2f}")
        self.coupon(total)

    def coupon(self,total):
        valid_coupon_codes=[1,2,3,4,5,6]
        discounts=[10,20,30,40,50,60]
        c=input("Would you like to use any coupon code? \n1 for Yes 2 for No : ")
        if c=="1":
            coupon_code=int(input("Please enter the coupon code: "))
            if coupon_code in valid_coupon_codes:
                i = valid_coupon_codes.index(coupon_code)
                discount_percentage=discounts[i]
                total=total-((discount_percentage/100)*total)
                print("Hurray! Your total is updated:$ ",total)
                self.payment(total)
            else:
                print("Please enter a valid coupon code")
                self.coupon(total)
        elif c=="2":
            self.payment(total)
        else:
            print("Please enter a valid option")
            self.coupon(total)
        
    def payment(self,total):
        s=input("Please choose your mode of payment: UPI OR COD: ")
        if s=="UPI":
            input("Enter your UPI ID: ")
            print("Order confirmed, now you will be directed to the home page ")
            self.features(total)
        elif s=="COD":
            print("Order confirmed, now you will be directed to the home page")
            self.features(total)
        else:
            print("Please enter a valid payment mode")
            self.payment(total)
            
    def features(self,total): 
        a=input("To avail more features enter \n1)Track order \n2)Cancel order \n3)Review \n4)Return to home page \n")
        if a=="1":
            self.track(total)    
        elif a=="2":
            print("Your order is cancelled, you'll recieve a refund of $",total)
            return
            
        elif a=="3":
            print("Please review your experience with us")
            print("*-poor \n**-average \n***-good \n****-very good \n*****-outstanding \n")
            input("How would you rate us out of 5 stars? ")
            print("Thank you for your valuable feedback")
            print("Would you like to share your experience in words?")
            q=input("Enter yes or no ")
            if q=="yes":
                input("Share a few words")
                print("Thank you for your valuable feedback.We'll direct you to our home page!")
            else:
                print("We'll direct you to our home page!")
            return
        elif a=="4":
            return
        else:
            print("Enter a valid option")
            return self.features(total)
                
                
    def track(self,total):
        print("Your order is being prepared")
        print("Your delivery partner has picked up the package")
        print("Your order is just 1km away from you!")
        t=input("Do you want to return to home page? Enter 1 for yes ")
        if t=="1":
            return
        else:
            self.features(total)

    def edit_details(self):
    
        print("\nOptions:")
        print("1. Edit User name")
        print("2. Edit address")
        print("3. Edit contact.no")
        print("4. Edit password")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_name = input("Enter the name ")
            self.name=new_name
        elif choice == "2":
            new_address = input("enter the address")
            self.address=new_address
        elif choice == "3":
            new_contact_no=input("Enter the contact number")
            self.contactno=new_contact_no
        
        elif choice == "4":
            new_password = input("enter the new password")
            self.password=new_password
        else:
            print("Invalid choice. Please try again.")
            self.edit_details()
    
        
def main():
    system = FoodDeliverySystem()
    
    print("Welcome to the home page of the online food delivery app")
    c=input("Select 1) for new user and \n 2)for existing user: ")
    if c =="1":
        system.register_user()
    elif c == "2":
        system.login_user()
    else:
        print("Enter valid input")
        main()
        

    while True:
        print("\nOptions:")
        print("1. Browse Restaurants and items")
        print("2. View cart")
        print("3. Place order")
        print("4. Edit details")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            system.browse_items()
        elif choice == "2":
            system.view_cart(cart)
        elif choice == "3":
            system.place_order(cart)
        elif choice == "4":
            system.edit_details()
        
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            1

if __name__ == "__main__":
    cart = []
    main()
    
    

