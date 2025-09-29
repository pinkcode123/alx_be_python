def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
     # Start with an empty shopping list

    shopping_list = []

    while True:  # keep showing the menu until user exits
        display_menu()   # show the menu
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the list.")
        
        
        elif choice == '2':
            # Remove item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the list.")
            else:
                print(f"{item} not found in the list.")
        
        
        elif choice == '3':
            # View list
            if shopping_list:
                print("Your shopping list contains:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
                print("")  # add a blank line for readability
            else:
                print("Your shopping list is empty.\n")
        
        
        elif choice == '4':
            # Exit program
            print("Goodbye!")
            break
        
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()