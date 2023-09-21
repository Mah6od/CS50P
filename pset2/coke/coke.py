def main():
    # Define the price of a Coke in cents
    coke_price = 50

    # Initialize a variable to keep track of the total amount inserted
    total_inserted = 0

    # Continuously prompt the user to insert coins until enough is inserted
    while total_inserted < coke_price:
        # Prompt the user for a coin (25, 10, or 5 cents)
        coin = int(input("Insert Coin: "))

        # Check if the inserted coin is valid
        if coin in [25, 10, 5]:
            total_inserted += coin
            remaining_amount = coke_price - total_inserted
            if remaining_amount > 0:
                print(f"Amount Due: {remaining_amount}")

    # Calculate and print the change owed to the user
    change = total_inserted - coke_price
    if change == 0:
        print("Change Owed: 0 cents")
    else:
        print(f"Change Owed: {abs(change)}")

if __name__ == "__main__":
    main()
