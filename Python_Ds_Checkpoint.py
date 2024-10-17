#Create a list named 'shopping_list' to store the items.
shopping_list = []
unique_items = set()
our_store_items = {"Orange", 
                   "Banana", 
                   "Apple", 
                   "Pineapple", 
                   "Grape",
                   "Mango",
                   "Guava",
                   "Pear",
                   "Watermelon"}

#Use a while loop to create a menu of options for the user to add, remove, or view items from the list.
while True:
    print("""Shopping List Menu
          1. Add Item
          2. Remove Item
          3. View Items
          4. Exit
          """)
    
#Use the input() function to prompt the user to make a selection from the menu.
    user_choice = int(input("Pick from the options(1/2/3/4): \n"))

#If the user selects 'add', use the input() function to prompt the user to enter an item to add to the list. 
# Use the range() function to limit the number of items that can be added to the list.
    if user_choice == 1:
        print("Add Item Selected.")
        print("These are the items we have in our store currently")
        for item in our_store_items:
            print(item)
        for i in range(5):
            item = input("Enter item: ").capitalize()
            if item == "Stop":
                break
            if item in our_store_items:
                if item in unique_items:
                    print(f"{item} is already in shopping list")
                elif item not in unique_items:
                    shopping_list.append(item)
                unique_items.add(item)
                
                print(f"{item} has been added to your shopping cart")
            
            else:
                print("Sorry! We do not have this currently.")
                
#If the user selects 'view', use a for loop to iterate through the list of items and display them to the user....
    elif user_choice == 3:
        print("Here is your selected items : ")
        if len(shopping_list) > 0:
            for item in shopping_list:
                print(f"{item}")
        else:
            print("Your cart is empty")
    
    elif user_choice == 4:
        print("Thank you for shopping with us")
        break


    #If the user selects 'remove', use the input() function to prompt the user to enter an item to remove from the list.
    elif user_choice ==2:
        print("Enter the item you want to remove")
        print("These are the items you have in your cart currently")
        for item in shopping_list:
            print(item)
        for i in range(5):
            item = input("Enter item: ").capitalize()
            if item == "Stop":
                break
            
            if item in unique_items:
                unique_items.remove(item)
            if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} has been removed from your shopping list")
            
            
            else:
                if item not in unique_items:
                    if item not in shopping_list:
                        print(f"{item} is not in your shoppping list")
                
                

            
    