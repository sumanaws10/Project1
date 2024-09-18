
import caffe 

def employee_options(self):
        while True:
            print("\n--- Employee Menu ---")
            print("1. Add food item")
            print("2. Add drink item")
            print("3. Add book item")
            print("4. Add a special item")
            print("5. Remove a food item")
            print("6. Remove a drink item")
            print("7. Remove a book from a list")
            print("8. View all orders")
            print("9. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                new_food = input("Enter the new food item: ")
                self.food_menu.append(new_food)
                print(f"{new_food} added to the food menu!")
            elif choice == "2":
                new_drink = input("Enter the new drink item: ")
                self.drink_menu.append(new_drink)
                print(f"{new_drink} added to the drink menu!")
            elif choice == "3":
                new_book = input("Enter the new book item: ")
                self.book_list.append(new_book)
                print(f"{new_book} added to the book list!")
            elif choice == "4":
                new_special = input("Enter the new special: ")
                self.special_item.append(new_special)
                print(f"{new_special} added to the specials!")
            elif choice =="5":
                Remove_food= input("Enter the food item to be deleted")
                self.food_menu.remove(Remove_food)
                print(f"{Remove_food} is removed from the list")
            elif choice =="6":
                Remove_drink= input("Enter the drink item to be deleted")
                self.drink_menu.remove(Remove_drink)
                print(f"{Remove_drink} is removed from the list")
            elif choice =="7":
                Remove_book= input("Enter the book to be removed from the book list")
                self.book_list.remove(Remove_book)
                print(f"{Remove_book} is removed from the list")
            elif choice == "8":
                self.view_orders()
            elif choice == "9":
                break
            else:
                print("Invalid option. Please try again.")
# shop=cafebook()
