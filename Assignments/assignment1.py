
-:Swiggy Order Information System :-
Food Order Details as Input

1.Order ID (int) - Unique identifier
2.Customer Name (str)
3.Restaurant Name (str)
4.Food Items (list)- Comma-separated food items
5.Order Amount (float)- Total bill
6.Delivery Status (tuple) -Delivered (Yes/No), Delivery Time in mins
7.GST Percentage (float) - Tax percentage
8.Delivery Address (dict) -House Number, Area, City
9.Order Tags (set) - Eg: Spicy, Vegan, Popular

Display Order Details Using Different Formatting Methods
i)   Comma Separation (sep=',') [Print Order ID, Customer Name, and Restaurant Name]
ii)  Percentage Formatting (%)  [Show GST as percentage].
iii) f-strings                  [Display the food items, total amount, and delivery status clearly].
iv)  .format() method           [Show delivery address with formatting].


#Swiggy Order Information System 
# Task 1: Take Food Order Details as Input
# 1. Order ID
order_id = int(input("Enter Order ID: "))
# 2. Customer Name
customer_name = input("Enter Customer Name: ")
# 3. Restaurant Name
restaurant_name = input("Enter Restaurant Name: ")
# 4. Food Items (comma-separated)
food_items_input = input("Enter Food Items (comma-separated): ")
food_items = food_items_input.split(',')
# 5. Order Amount
order_amount = float(input("Enter Total Amount: "))
# 6. Delivery Status (Tuple)
delivered = input("Enter Delivery Status (Delivered? Yes/No): ")
delivery_time = int(input("Enter Delivery Time in minutes: "))
delivery_status = (delivered, delivery_time)
# 7. GST Percentage
gst = float(input("Enter GST Percentage: "))
# 8. Delivery Address (Dictionary)
house_no = input("Enter House Number: ")
area = input("Enter Area: ")
city = input("Enter City: ")
address = { "house": house_no, "area": area,"city": city}
# 9. Order Tags (Set)
tags_input = input("Enter Order Tags (comma-separated): ")
order_tags = set(tags_input.split(','))
# Task 2: Display Order Details Using Different Formatting Methods
print("\n----- Order Details -----\n")
# 1. Comma Separation
print("Order ID, Customer Name, Restaurant:", order_id, customer_name, restaurant_name, sep=',')
# 2. Percentage Formatting
print("GST Applied: %.2f%%" % gst)
# 3. f-strings
print(f"Food Items Ordered: {food_items}")
print(f"Total Amount: ₹{order_amount}")
print(f"Delivery Status: Delivered - {delivery_status[0]}, Time - {delivery_status[1]} mins")
print(f"Order Tags: {order_tags}")
# 4. .format() method
print("Delivery Address: House No - {}, Area - {}, City - {}".format(
    address["house"], address["area"], address["city"]))
'''Output:
Enter Order ID: 5001  
Enter Customer Name: Pravalika  
Enter Restaurant Name: Meghana Foods  
Enter Food Items (comma-separated): Biryani, Raita, Coke  
Enter Total Amount: 599.50  
Enter Delivery Status (Delivered? Yes/No): Yes  
Enter Delivery Time in minutes: 35  
Enter GST Percentage: 5.0  
Enter House Number: 12-5  
Enter Area: Ameerpet  
Enter City: Hyderabad  
Enter Order Tags (comma-separated): Spicy, Popular '''