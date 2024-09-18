import minu
import caffe

menu={'drinks':{'mojito':10,
        'milkshake':11,
        'juice':9,
        'beer':13,
        'water':3},

'books':{'private peaceful':10,
        'tfios':11,
        'hp':19,
        'got':13,
        'vampire diaries':13},

'foods':{'rice':10,
        'curry':11,
        'veggies':19,
        'cake':13,
        'bread':13}
}


print("\n--- Welcome to the Cafe Bookshop ---")
print("1. View Menu and Place Order")
print("2. Employee Options")
print("3. Exit")

user_input = input("Choose an option: ")

if user_input == "1":
    caffe.take_order(menu)
elif user_input == "2":
    password = input("Enter employee password: ")
    if password == "admin123":  
        minu.employee_options()
    else:
        print("Incorrect password.")

