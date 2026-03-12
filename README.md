# Riwistore

## Description

Riwistore is a command-line shopping cart application designed for managing product purchases. The application is built to calculate subtotals and accumulate a grand total for multiple items efficiently. It provides a user-friendly interface for adding products until the user decides to finalize the purchase.

## How it works

1. The program displays a welcome message and imports the `obtener_input_valido` function from the `inventario` module to handle user input validation.

2. It defines the `costo_total` function, which multiplies the price by quantity to calculate each item's subtotal.

3. The main loop runs while the user enters "si" (yes), prompting for product name, price, and quantity with input validation.

4. For each item, the program calculates the subtotal using `costo_total`, adds it to `total_general`, and displays the product details.

5. After each item, it asks if the user wants to add another article; the loop continues based on the response.

6. When the user enters "no", the program exits the loop and displays the final total to pay.

> **Status**: The application is fully functional and currently processes multiple products while accumulating the grand total accurately.
