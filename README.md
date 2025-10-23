# Credit Card Validation System

A Python application that validates credit card numbers using the Luhn algorithm with enhanced digit manipulation and verification processes.

## 📁 Files

- **Toh Qi Hao_T04_A2P1.py** - Main Python application file containing the complete credit card validation system
- **README.md** - Project documentation (this file)

## 👨‍💻 Author

**Toh Qi Hao**  

## 🛠 Technologies Used

- **Python 3** - Core programming language
- **Standard Python Libraries** - Built-in functions and modules
- **String Manipulation** - For card number processing and formatting
- **List Comprehensions** - Efficient data processing
- **Modular Arithmetic** - Luhn algorithm implementation
- **Input Validation** - Robust user input handling
- **Function-Oriented Programming** - Modular code structure

## 📋 Program Features

### Input Validation
- Credit card number format checking (XXXX-XXXX-XXXX-XXXX)
- Non-digit character detection
- Token count validation (exactly 4 groups of 4 digits)
- Interactive retry mechanism

### Card Processing Pipeline
1. **Reverse Digits** - Each 4-digit group is reversed
2. **Even Position Multiplication** - 2nd and 4th digits in each group are doubled
3. **Digit Sum Calculation** - Sum of all digits in each modified group
4. **Total Sum Computation** - Aggregate sum of all digits
5. **Modulo Validation** - Final check using modulo 10 operation

### User Interface
- Welcome message from "ABC credit card company"
- Clear step-by-step analysis display
- Formatted output with proper alignment
- Interactive session management

## 🔍 Validation Algorithm

The program implements a modified Luhn algorithm:
1. Reverse each 4-digit group
2. Double digits at even positions (2nd and 4th in each group)
3. Calculate sum of all individual digits
4. Check if total sum is divisible by 10

## 🚀 How to Run

1. Ensure Python 3 is installed on your system
2. Download the `Toh Qi Hao_T04_A2P1.py` file
3. Open terminal/command prompt in the file directory
4. Run the program:
   ```bash
   python "Toh Qi Hao_T04_A2P1.py"
