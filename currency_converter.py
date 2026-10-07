# Currency Converter Agent for Beginners

rates = {
    "USD": 83.50,
    "EUR": 90.20,
    "GBP": 105.30,
    "AED": 22.75,
    "JPY": 0.57
}

print("Welcome to Currency Converter Agent")
print("Convert foreign currency into INR")
print("Type exit to stop")

while True:
    currency = input("\nEnter currency code USD/EUR/GBP/AED/JPY: ").upper()

    if currency == "EXIT":
        print("Thank you for using Currency Converter Agent")
        break

    if currency in rates:
        amount = float(input("Enter amount: "))
        result = amount * rates[currency]

        print("Converted Amount:")
        print(amount, currency, "=", round(result, 2), "INR")
    else:
        print("Currency not available")