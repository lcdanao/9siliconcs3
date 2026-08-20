# Computational Thinking Exercise
## [Smart School Canteen Queue OR Smart Vending Machine]
**Name:** Leanne C. Danao
**Section:** Silicon
**Last Name:** Danao
**Date:** August 17, 2026
---
## Step 1: Identify the Big Problem
### Main Problem

The school canteen has long queues during lunch because ordering, payment, and monitoring food supplies are slow and inefficient. This affects the school by causing delays, reducing students’ lunch time, and making the canteen less efficient and organized.

---
## Step 2: Identify the Sub-Problems

1. Students take too long to decide what food to order.
2. Cashiers manually calculate the total price and give change.
3. Canteen staff have difficulty tracking which food items are running out.
4. The ordering and payment process causes long queues and delays.

---
## Step 3: Apply Computational Thinking Skills

| Students take too long to decide what to order | Decomposition | Divide the menu into categories and display food, prices, and availability clearly. |
| Cashiers manually calculate totals price and give change. | Algorithm Design | Create a program that calculates the total cost and automatically determines the customer's change. |
| Staff have difficulty tracking food supplies. | Pattern Recognition | Record sales and identify which food items are frequently sold or running low. |
| Long queues occur during lunch. | Abstraction | Focus on the important information: food selected, quantity, price, payment, and available stock. |

---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
Write the sub-problem you selected.
### Pseudocode

START

Display available food items, prices, and stock

Student selects food item
Student enters quantity

IF stock is sufficient THEN
    Update food stock
    Display total amount
    Receive payment

    IF payment >= total THEN
        Calculate change = payment - total
        Display change
        Confirm order
    ELSE 
        Display "Insufficient payment"
    END IF

ELSE
    Display "Item is out of stock"
END IF

Dislay updated food availability

END
---