def is_product_name_valid(name):
    if not name.strip():
        return False, "The name cannot be empty."
    if name.isdigit():  # if it's only numbers (e.g. "2000", "123")
        return False, "The product name cannot be only numbers."
    if any(char.isdigit() for char in name):  # if it contains any digit
        return False, "The product name cannot contain numbers."
    return True, ""


sales = []  # List that stores each sale (dictionary)
continue_entry = True


print("=== Daily sales registration ===\n")


while continue_entry:
    print("\n--- New sale ---")
    name = input("Product name (or type 'exit' to finish the day): ").strip()


    # Check if the user wants to exit
    if name.lower() == "exit":
        continue_entry = False
        continue


    # Validate name with the function
    is_valid, message = is_product_name_valid(name)
    if not is_valid:
        print(message)
        continue


    # Read and validate price
    try:
        price = float(input("Unit price: "))
        if price < 0:
            print("Price cannot be negative. Please try again.")
            continue
    except ValueError:
        print("Invalid price. You must enter a number. Please try again.")
        continue


    # Read and validate quantity
    try:
        quantity = int(input("Quantity sold: "))
        if quantity <= 0:
            print("Quantity must be greater than 0. Please try again.")
            continue
    except ValueError:
        print("Invalid quantity. You must enter an integer. Please try again.")
        continue


    # Calculate total of the sale
    total_sale = price * quantity


    # Record the sale
    sales.append({
        "product": name,
        "unit_price": price,
        "quantity": quantity,
        "total_sale": total_sale
    })


    print(f"Sale recorded: {name} - {quantity} units - Total: {total_sale:.2f}")



# Summary at the end of the day
print("\n" + "=" * 50)
print("DAILY SALES SUMMARY")
print("=" * 50)


if not sales:
    print("No sales were recorded today.")
else:
    # Dictionary to accumulate quantities per product
    product_totals = {}
    total_day = 0.0


    for sale in sales:
        prod = sale["product"]
        qty = sale["quantity"]
        tot = sale["total_sale"]


        if prod in product_totals:
            product_totals[prod]["quantity"] += qty
            product_totals[prod]["total_accumulated"] += tot
        else:
            product_totals[prod] = {
                "quantity": qty,
                "total_accumulated": tot
            }


        total_day += tot


    # Show list of products
    print("\nProducts sold:")
    print("-" * 40)
    for prod, data in product_totals.items():
        print(f"{prod:20} - Units: {data['quantity']:3} - Total: {data['total_accumulated']:8.2f}")


    # General totals
    print("\n" + "-" * 40)
    print(f"Total units sold: {sum(v['quantity'] for v in sales)} units")
    print(f"Total income of the day: {total_day:.2f}")
    print("-" * 40)


print("\nSales registration finished!")
