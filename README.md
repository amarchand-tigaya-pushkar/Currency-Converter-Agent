# 💱 Currency Converter Agent using Python

A beginner-friendly Python project that converts foreign currency into Indian Rupees (INR) using predefined exchange rates.

## 📌 Project Name

**Simple Currency Converter Agent using Python**

## 🎯 Goal

Create an agent that converts one currency into another currency.

## 🔄 Workflow

```text
User enters amount
        ↓
User enters currency
        ↓
Agent checks exchange rate
        ↓
Agent calculates result
        ↓
Agent shows converted amount
```

## 🛠️ Tools Required

- Python
- VS Code
- Basic `input()`
- Variables
- Dictionary
- If-Else
- Loop
- Formula

## 📁 Project Structure

```text
Currency-Converter-Agent/
│
├── currency_converter.py
├── README.md
└── requirements.txt
```

## ▶️ How to Run

Open the terminal inside the project folder:

```bash
python currency_converter.py
```

## 💱 Supported Currencies

The project currently supports:

| Currency | Rate to INR |
|---|---:|
| USD | 83.50 |
| EUR | 90.20 |
| GBP | 105.30 |
| AED | 22.75 |
| JPY | 0.57 |

## 🧮 Formula

```text
result = amount × exchange rate
```

Example:

```text
10 × 83.50 = 835 INR
```

## 🖥️ Sample Output

```text
Welcome to Currency Converter Agent
Convert foreign currency into INR
Type exit to stop

Enter currency code USD/EUR/GBP/AED/JPY: USD
Enter amount: 10

Converted Amount:
10.0 USD = 835.0 INR
```

## 🚪 Exit

Type:

```text
exit
```

to stop the program.

## 🤖 Agentic AI Thinking

### User Goal

```text
Convert 100 USD into INR
```

### Agent Steps

1. Understand source currency = USD
2. Understand target currency = INR
3. Get exchange rate
4. Apply formula
5. Show final answer

## 🧠 Concepts Learned

This project helps beginners understand:

- Python input
- Variables
- Dictionary
- Conditions
- Loops
- String `upper()`
- Mathematical formula
- Currency conversion
- Basic agent workflow

## 🌐 Real API Version

The project can also be upgraded to use live exchange rates.

Install:

```bash
pip install requests
```

Example API workflow:

```python
import requests

amount = float(input("Enter amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

response = requests.get(url)
data = response.json()

rate = data["rates"][to_currency]

result = amount * rate

print(amount, from_currency, "=", round(result, 2), to_currency)
```

## 🚀 Future Extensions

1. Add more currencies
2. Add live API rates
3. Add Streamlit web app
4. Add voice input
5. Add chatbot interface
6. Add travel expense calculator
7. Add WhatsApp currency bot

## 📚 Project Description

A Currency Converter Agent is a beginner-friendly Python project that takes amount and currency from the user, checks exchange rates, calculates converted value, and displays the result.

It helps beginners understand input, dictionary, conditions, loops, APIs, JSON, and real-world agent workflow.