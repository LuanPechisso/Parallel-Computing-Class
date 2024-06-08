

scissors = """
             _______
         ---'   ____)____
                   ______)               Serial Computing version:
                __________)
               (____)
         ---.__(___)
 """

print(scissors)
import random
import time


# Function to simulate a checkout process for customers in self-checkout lines
def self_checkout_cashier(line_id, customers):
    print(f"line {line_id} of Self-checkout  starts processing.")

    for customer in customers:
        left_processing_customer(line_id, customer)
    print(f"line {line_id} Self-checkout has finished processing.")
    # print('\n')


# Function to simulate a cashier processing customers in a single checkout line
def traditional_cashier(line_id, customers):
    print(f"line {line_id} of Tradition_Cashier starts processing.")

    for customer in customers:
        central_processing_customer(line_id, customer)
    print(f"line {line_id} of Traditional_Cashier has finished processing.")
    # print('\n')


# Function to simulate the fast lane processing of customers
def fifteen_item_cashier(line_id, customers):
    print(f"line {line_id} of fifteen_items starts processing.")

    for customer in customers:
        right_processing_customer(line_id, customer)
    print(f"line {line_id} of fifteen_items has finished processing.")
    # print('\n')


# Function to simulate processing of a customer by self_checkout
def left_processing_customer(line_id, customer):
    # processing_time = random.uniform(2.0, 6.0)
    print(f"Self-Checkout Line {line_id} processing customer {customer}...")
    time.sleep(1)
    print(f"Self-Checkout Line {line_id} finished processing customer {customer}.")


# Function to simulate processing of a customer by trained cashier
def central_processing_customer(line_id, customer):
    # processing_time = random.uniform(2.0, 5.0)
    print(f"Traditional-Cashier Line {line_id} processing customer {customer}...")
    time.sleep(1)
    print(f"Traditional-Cashier Line {line_id} finished processing customer {customer}.")


# Function to simulate processing of a customer by trained cashier for 15 max items
def right_processing_customer(line_id, customer):
    # processing_time = random.uniform(2.0, 3.0)
    print(f"15-or-less-iterm-cashier Line {line_id} processing customer {customer}...")
    time.sleep(1)
    print(f"15-or-less-iterm-cashier Line {line_id} finished processing customer {customer}.")


if __name__ == "__main__":

    total_self_checkout_customers = int(input('\nEnter total self-checkout customers: '))

    total_traditional_checkout_customers = list(range(1, int(input('Enter total traditional customers: '))))
    traditional_customer1 = total_traditional_checkout_customers[:len(total_traditional_checkout_customers) // 2]
    traditional_customer2 = total_traditional_checkout_customers[len(total_traditional_checkout_customers) // 2:]

    fifteen_item_checkout_customer = list(range(1, int(input('Enter total 15_item_checkout customers: '))))

    print('\n')

    customers_per_list = total_self_checkout_customers // 4
    remainder_customers = total_self_checkout_customers % 4

    distributed_self_checkout_customers = []

    for i in range(4):
        # Initialize each sublist
        sublist = list(range(i * customers_per_list + 1, (i + 1) * customers_per_list + 1))
        distributed_self_checkout_customers.append(sublist)

    # Distribute any remaining customers
    for i in range(remainder_customers):
        distributed_self_checkout_customers[i].append(total_self_checkout_customers - remainder_customers + i + 1)

    start = time.perf_counter()

    self_checkout_cashier(1, distributed_self_checkout_customers[0])
    self_checkout_cashier(2, distributed_self_checkout_customers[1])
    self_checkout_cashier(3, distributed_self_checkout_customers[2])
    self_checkout_cashier(4, distributed_self_checkout_customers[3])

    traditional_cashier(1, traditional_customer1)
    traditional_cashier(2, traditional_customer2)

    fifteen_item_cashier(1, fifteen_item_checkout_customer)

    finish = time.perf_counter()

    print(f'\nRuntime in: {round(finish - start)} second(s)')

