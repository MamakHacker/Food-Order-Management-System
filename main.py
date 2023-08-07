

# import os and datetime module

import os
import datetime


# function to clear screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



# function to get user input
def get_input(message):
    return input(message)



# function to get user input with data type conversion
def get_input_int(message):
    return int(input(message))




# function to get user input with data type conversion
def get_input_float(message):
    return float(input(message))



# function to pause
def pause():
    input("Press Enter to continue...")










# function to display menu
def display_menu():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    1. Login as Admin
    2. Login as Customer
    3. Login as Delivery Staff
    4. Register
    5. View as Guest
    6. Exit
    """)

    choice = get_input_int("Enter choice : ")

    # check user choice
    if choice == 1:
        login()
    elif choice == 2:
        login_as_customer()
    elif choice == 3:
        login_as_delivery_staff()
    elif choice == 4:
        register()
    elif choice == 5:
        display_menu_for_guest_user()
    elif choice == 6:
        exit()
    else: 
        return display_menu()
    
def display_menu_for_guest_user():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    1. View Food Category
    2. View Food Items
    3. Register
    4. Exit
    
    """)

    choice = get_input_int("Enter choice : ")

    # check user choice
    if choice == 1:
        display_food_category_as_guest()
    elif choice == 2:
        display_food_items_as_guest()
    elif choice == 3:
        register()
    elif choice == 4:
        exit()
    else:  
        return display_menu_for_guest_user()



# function to display menu for registered user
def display_menu_for_registered_user():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    1. View Food Category
    2. View Food Items
    3. Select Menu Items
    4. Confirm Order
    5. Give Feedback
    6. Back
    """)
    

    choice = get_input_int("Enter choice : ")

    # check user choice
    if choice == 1:
        display_food_category_as_customer()
    elif choice == 2:
        display_food_items_as_customer()
    elif choice == 3:
        select_menu_items()
    elif choice == 4:
        confirm_order()
    elif choice == 5:
        give_feedback()
    elif choice == 6:
        display_menu()
    else:
        
        return display_menu_for_registered_user()



# function to display menu for admin
def display_menu_for_admin():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== ADMIN PANEL ==========================
    1. Add Food Category
    2. Add Food Item
    3. Modify Food Item
    4. View All Food Category
    5. View All Food Item
    6. View All Customer Orders
    7. View All Customer Payment
    8. Search Customer Order
    9. Search Customer Payment
    10. Add Delivery Staff
    11. Modify Delivery Staff
    12. Delete Delivery Staff
    13. Assign Orders to Delivery Staff
    14. View Customer Feedback
    15. Back
    """)

    choice = get_input_int("Enter choice : ")

    # check user choice
    if choice == 1:
        add_food_category()
    elif choice == 2:
        add_food_item()
    elif choice == 3:
        modify_food_item()
    elif choice == 4:
        display_food_category_as_admin()
    elif choice == 5:
        display_food_items_as_admin()
    elif choice == 6:
        display_customer_order()
    elif choice == 7:
        display_customer_payment()
    elif choice == 8:
        search_customer_order()
    elif choice == 9:
        search_customer_payment()
    elif choice == 10:
        add_delivery_staff()
    elif choice == 11:
        modify_delivery_staff()
    elif choice == 12:
        delete_delivery_staff()
    elif choice == 13:
        assign_orders_to_delivery_staff()
    elif choice == 14:
        view_feedback()
    elif choice == 15:
        display_menu()
    else:
        return display_menu_for_admin()


# function to login
def login():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== LOGIN AS ADMIN ================================
    """)
    username = get_input("Enter username : ")
    password = get_input("Enter password : ")

    # check if username and password is correct
    if username == "admin" and password == "admin":
        display_menu_for_admin()
    else:
        return login() 
        

# function to view food items
def display_food_items_as_guest():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW FOOD ITEMS =======================
    """)

    # open file
    file = open("food_item.txt", "r")

    # read file
    food_items = file.read()

    # close file
    file.close()

    # display food items
    print(food_items)

    pause()
    return display_menu_for_guest_user()

# function to view food items
def display_food_items_as_admin():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW FOOD ITEMS =======================
    """)

    # open file
    file = open("food_item.txt", "r")

    # read file
    food_items = file.read()

    # close file
    file.close()

    # display food items
    print(food_items)

    pause()
    return display_menu_for_admin()

# function to view food items
def display_food_items_as_customer():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW FOOD ITEMS =======================
    """)

    # open file
    file = open("food_item.txt", "r")

    # read file
    food_items = file.read()

    # close file
    file.close()

    # display food items
    print(food_items)

    pause()
    return display_menu_for_registered_user()    

# function to display food category
def display_food_category_as_guest():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW ALL FOOD CATEGORY ===============
    """)

    # open file
    file = open("food_category.txt", "r")

    # read file
    food_category = file.read()

    # close file
    file.close()

    # display food category
    
    print(food_category)
    pause()
    return display_menu_for_guest_user()

def display_food_category_as_admin():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW ALL FOOD CATEGORY ===============
    """)

    # open file
    file = open("food_category.txt", "r")

    # read file
    food_category = file.read()

    # close file
    file.close()

    # display food category
    print(food_category)
    pause()
    return display_menu_for_admin()

def display_food_category_as_customer():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW ALL FOOD CATEGORY ===============
    """)

    # open file
    file = open("food_category.txt", "r")

    # read file
    food_category = file.read()

    # close file
    file.close()

    # display food category
    print(food_category)
    pause()
    return display_menu_for_registered_user()
    
    







# function to display customer order
def display_customer_order():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW ALL CUSTOMER ORDERS =============
    """)

    # open file
    file = open("selected_menu_items.txt", "r")

    # read file
    customer_order = file.read()

    # close file
    file.close()

    # display customer order
    print(customer_order)

    pause()
    return display_menu_for_admin()



# function to display customer payment
def display_customer_payment():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW ALL CUSTOMER PAYMENT ============
    """)

    # open file
    file = open("order.txt", "r")

    # read file
    customer_payment = file.read()

    # close file
    file.close()

    # display customer payment
    print(customer_payment)

    pause()
    return display_menu_for_admin()


# function to search customer order
def search_customer_order():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== SEARCH CUSTOMER ORDER ================
    """)

    # open file
    file = open("selected_menu_items.txt", "r")

    # read file
    customer_order = file.read()

    # close file
    file.close()

    # display customer order
    print(customer_order)

    # get customer order id
    customer_order_id = get_input_int("\nEnter Customer Order ID: ")

    # open file
    file = open("selected_menu_items.txt", "r")

    # read file
    customer_order = file.readlines()

    # close file
    file.close()

    # search customer order
    for line in customer_order:
        if str(customer_order_id) in line:
            print(line)

    pause()
    return display_menu_for_admin()



# function to search customer payment
def search_customer_payment():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== SEARCH CUSTOMER PAYMENT ==============
    """)

    # open file
    file = open("order.txt", "r")

    # read file
    customer_payment = file.read()

    # close file
    file.close()

    # display customer payment
    print(customer_payment)

    # get customer payment id
    customer_payment_id = get_input_int("\nEnter Customer Payment ID: ")

    # open file
    file = open("order.txt", "r")

    # read file
    customer_payment = file.readlines()

    # close file
    file.close()

    # search customer payment
    for line in customer_payment:
        if str(customer_payment_id) in line:
            print(line)

    pause()
    return display_menu_for_admin()



# function to add food category
def add_food_category():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== ADD FOOD CATEGORY ====================
    """)

    # get food category id
    food_category_id = get_input_int("Enter Food Category ID: ")

    # get food category name
    food_category_name = get_input("Enter Food Category Name: ")

    # open file
    file = open("food_category.txt", "a")

    # write to file
    file.write("\n" + str(food_category_id) + "," + food_category_name)

    # close file
    file.close()

    print("\nFood Category Added Successfully!")

    pause()
    return display_menu_for_admin()



# function to add food item
def add_food_item():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== ADD FOOD ITEM ========================
    """)
    # open file
    file = open("food_item.txt", "r")

    # read file
    food_item = file.read()

    # close file
    file.close()

    # display food item
    print("Food Available Now")
    print(food_item)
    
    # get food item id
    food_item_id = get_input("Enter New Food Item ID (Ex: 1,2,3...): \n")
    
    # get food item name
    food_item_name = get_input("Enter Food Item Name: ")

    # get food item price
    food_item_price = get_input_float("Enter Food Item Price: ")

    # open file
    file = open("food_item.txt", "a")

    # write to file
    file.write("\n" + food_item_id + "," + str(food_item_name) + "," + str(food_item_price))

    # close file
    file.close()

    print("\nFood Item Added Successfully!")

    pause()
    return display_menu_for_admin()



# function to modify food item
def modify_food_item():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== MODIFY FOOD ITEM =====================
    """)

    # open file
    file = open("food_item.txt", "r")

    # read file
    food_item = file.read()

    # close file
    file.close()

    # display food item
    print(food_item)

    # get food item 
    food_item_id = get_input("\nEnter Food Item ID To Modify: ")

    # open file
    file = open("food_item.txt", "r")

    # read file
    food_item = file.readlines()

    # close file
    file.close()

    # search food item
    for line in food_item:
        if str(food_item_id) in line:
            
            print(line)

    

    # get food item name
    food_item_name = get_input("Enter Food Item Name: ")

    # get food item price
    food_item_price = get_input_float("Enter Food Item Price: ")

    # open file
    file = open("food_item.txt", "w")

    # write to file
    for line in food_item:
        if str(food_item_id) in line:
            file.write(food_item_id + ", " + str(food_item_name) + "," + str(food_item_price) + "\n")
        else:
            file.write(line)

    # close file
    file.close()

    print("\nFood Item Modified Successfully!")

    pause()
    return display_menu_for_admin()



# function to add delivery staff
def add_delivery_staff():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== ADD DELIVERY STAFF ===================
    """)

    # get delivery staff id
    delivery_staff_id = get_input_int("Enter Delivery Staff ID: ")

    # get delivery staff name
    delivery_staff_name = get_input("Enter Delivery Staff Name: ")

    # open file
    file = open("delivery_staff.txt", "a")

    # write to file
    file.write("\n" + str(delivery_staff_id) + "," + delivery_staff_name)

    # close file
    file.close()

    print("\nDelivery Staff Added Successfully!")

    pause()
    return display_menu_for_admin()


# function to modify delivery staff
def modify_delivery_staff():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== MODIFY DELIVERY STAFF =================
    """)

    # open file
    file = open("delivery_staff.txt", "r")

    # read file
    delivery_staff = file.read()

    # close file
    file.close()

    # display delivery staff
    print(delivery_staff)

    # get delivery staff id
    delivery_staff_id = get_input_int("\nEnter Delivery Staff ID: ")

    # open file
    file = open("delivery_staff.txt", "r")

    # read file
    delivery_staff = file.readlines()

    # close file
    file.close()

    # search delivery staff
    for line in delivery_staff:
        if str(delivery_staff_id) in line:
            print(line)

    # get delivery staff name
    delivery_staff_name = get_input("Enter Delivery Staff Name: ")

    # open file
    file = open("delivery_staff.txt", "w")

    # write to file
    for line in delivery_staff:
        if str(delivery_staff_id) in line:
            file.write(str(delivery_staff_id) + "," + delivery_staff_name + "\n")
        else:
            file.write(line)

    # close file
    file.close()

    print("\nDelivery Staff Modified Successfully!")

    pause()
    return display_menu_for_admin()


# function to delete delivery staff
def delete_delivery_staff():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== DELETE DELIVERY STAFF =================
    """)

    # open file
    file = open("delivery_staff.txt", "r")

    # read file
    delivery_staff = file.read()

    # close file
    file.close()

    # display delivery staff
    print(delivery_staff)

    # get delivery staff id
    delivery_staff_id = get_input_int("\nEnter Delivery Staff ID: ")

    # open file
    file = open("delivery_staff.txt", "r")

    # read file
    delivery_staff = file.readlines()

    # close file
    file.close()

    # search delivery staff
    for line in delivery_staff:
        if str(delivery_staff_id) in line:
            print(line)

    # open file
    file = open("delivery_staff.txt", "w")

    # write to file
    for line in delivery_staff:
        if str(delivery_staff_id) not in line:
            file.write(line)

    # close file
    file.close()

    print("\nDelivery Staff Deleted Successfully!")

    pause()
    return display_menu_for_admin()


# function to assign orders to delivery staff
def assign_orders_to_delivery_staff():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== ASSIGN ORDERS TO DELIVERY STAFF =======
    """)

    # open file
    file = open("selected_menu_items.txt", "r")

    # read file
    customer_order = file.read()

    # close file
    file.close()

    # display customer order
    print(customer_order)

    # get customer order id
    customer_order_id = get_input_int("\nEnter Customer Order ID: ")

    # open file
    file = open("selected_menu_items.txt", "r")

    # read file
    customer_order = file.readlines()

    # close file
    file.close()

    # search customer order
    for line in customer_order:
        if str(customer_order_id) in line:
            print(line)

    # get delivery staff id
    delivery_staff_id = get_input_int("\nEnter Delivery Staff ID: ")

    # open file
    file = open("customer_order.txt", "w")

    # write to file
    for line in customer_order:
        if str(customer_order_id) in line:
            file.write(line.replace("\n", "," + str(delivery_staff_id) + "\n"))
        else:
            file.write(line)

    # close file
    file.close()

    print("\nOrders Assigned to Delivery Staff Successfully!")

    pause()
    return display_menu_for_admin()

# function to display feedback
def view_feedback():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== VIEW FEEDBACK ========================
    """)

    # open file
    file = open("feedback.txt", "r")

    # read file
    feedback = file.read()

    # close file
    file.close()

    # display feedback
    print(feedback)

    pause()
    return display_menu_for_admin()


# function to add food category
def add_food_category():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== ADD FOOD CATEGORY ====================
    """)

    # get input from user
    category_name = get_input("Enter food category name : ")

    # open file
    file = open("food_category.txt", "a")

    # write to file
    file.write(category_name + "\n")

    # close file
    file.close()

    print("Food category added successfully")

    pause()
    return display_menu_for_admin()





# function to add food items
def add_food_items():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== ADD FOOD ITEMS ========================
    """)

    # get input from user
    
    food_name = get_input("Enter food name : ")
    food_price = get_input_float("Enter food price : ")

    # open file
    file = open("food_item.txt", "a")

    # write to file
    file.write(food_name + "," + " RM " + str(food_price) + "\n")

    # close file
    file.close()

    print("Food items added successfully")

    pause()
    return display_menu_for_admin()



    

# function to select menu items
def select_menu_items():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== SELECT MENU ITEMS =====================
    """)

    # open file
    file = open("food_item.txt", "r")

    # read file
    food_items = file.read()

    # close file
    file.close()

    # display food items
    print(food_items)

    # get input from user
    food_name = get_input("Enter food name : ")
    food_quantity = get_input_int("Enter food quantity : ")

    # open file
    file = open("selected_menu_items.txt", "a")

    # write to file
    file.write(food_name + "," + str(food_quantity) + "\n")

    # close file
    file.close()

    print("Food items added successfully")

    pause()
    return display_menu_for_registered_user()


# function to confirm order
def confirm_order():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== CONFIRM ORDER ========================
    """)

    # open file
    file = open("selected_menu_items.txt", "r")

    # read file
    selected_menu_items = file.read()

    # close file
    file.close()

    # display selected menu items
    print("Your orders: ")
    print(selected_menu_items)

    # get input from user
    payment_method = get_input("Enter payment method : ")

    # open file
    file = open("order.txt", "a")

    # write to file
    file.write(selected_menu_items + "," + payment_method + "\n")

    # close file
    file.close()

    print("Order placed successfully")

    pause()
    return display_menu_for_registered_user()



# function to give feedback
def give_feedback():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== GIVE FEEDBACK ========================
    """)

    # get input from user
    name = get_input("Enter your name : ")
    feedback = get_input("Enter your feedback : ")

    # open file
    file = open("feedback.txt", "a")

    # write to file
    file.write(name + ": " + feedback + "\n")

    # close file
    file.close()

    print("Thank you for your feedback !")

    pause()
    return display_menu_for_registered_user()


# function to register
def register():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== REGISTER =============================
    """)

    # get input from user
    first_name = get_input("Enter first name : ")
    last_name = get_input("Enter last name : ")
    username = get_input("Enter username : ")
    password = get_input("Enter password : ")

    # open file
    file = open("user.txt", "a")

    # write to file
    file.write(first_name + "," + last_name + "," + username + "," + password + "\n")

    # close file
    file.close()

    print("User registered successfully")

    pause()
    return display_menu()

# function to login as delivery staff
def login_as_delivery_staff():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== LOGIN AS DELIVERY STAFF ===============
    """)

    # get user input
    username = get_input("Enter Your Staff ID: ")
    password = get_input("Enter Password: ")

    # open file
    file = open("delivery_staff.txt", "r")

    # read file
    delivery_staff = file.read()

    # close file
    file.close()

    # check if username and password is correct
    if username in delivery_staff and password in delivery_staff:
        print("Login Successful!")
        pause()
        delivery_staff_menu()
    
    else:
        print("Login Failed!")
        pause()
        return login_as_delivery_staff()

def login_as_customer():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== LOGIN AS CUSTOMER ===============
    """)

    # get user input
    username = get_input("Enter Username: ")
    password = get_input("Enter Password: ")

    # open file
    file = open("user.txt", "r")

    # read file
    registered_user = file.read()

    # close file
    file.close()

    # check if username and password is correct
    if username in registered_user and password in registered_user:
        print("Login Successful!")
        pause()
        display_menu_for_registered_user()
    else:
        print("Login Failed!")
        pause()
        return login_as_customer()

# function to display delivery staff menu
def delivery_staff_menu():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== DELIVERY STAFF MENU ===================
    """)

    
    print("""
    1. View and select Orders for Delivery.
    2. Update Delivery Status.
    3. Exit
    """)
    
    # get user input        
    choice = get_input_int("Enter choice : ")

    # check user choice
    if choice == 1:
        view_and_select_orders_for_delivery()
    elif choice == 2:
        update_delivery_status()
    elif choice == 3:
        exit()
    else:
        print("Invalid Choice!")
        pause()
        delivery_staff_menu()



# function to view and select orders for delivery
def view_and_select_orders_for_delivery():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =============== VIEW AND SELECT ORDERS FOR DELIVERY =======
    """)

    # open file
    file = open("order.txt", "r")

    # read file
    orders = file.read()

    # close file
    file.close()

    # display orders
    print(orders)

    pause()
    return delivery_staff_menu()


# function to update delivery status
def update_delivery_status():
    cls()
    print("""
    ==========================================================
    =================== AOFS ONLINE FOOD SERVICES ============
    ==========================================================

    =================== UPDATE DELIVERY STATUS ================
    """)

    # get user input
    order_id = get_input("Enter Order ID: ")
    order_status = get_input("Enter Order Status: ")

    # open file
    file = open("order.txt", "r")

    # read file
    orders = file.read()

    # close file
    file.close()

    # check if order id exist
    if order_id in orders:
        # open file
        file = open("order.txt", "w")

        # replace order status
        orders = orders.replace(order_id, order_id + " -- > " + order_status)

        # write to file
        file.write(orders)

        # close file
        file.close()

        print("Order Status Updated!")
        pause()
        return delivery_staff_menu()
    else:
        print("Order ID does not exist!")
        pause()
        return delivery_staff_menu()


# main function
def main():
    display_menu()

    # get user input
    choice = get_input_int("Enter choice : ")

    # check user choice
    if choice == 1:
        login()
    elif choice == 2:
        login_as_customer()
    elif choice == 3:
        login_as_delivery_staff()
    elif choice == 4:
        register()
    elif choice == 5:
        exit()
    else:
        return main()



# call main function
main()