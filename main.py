import threading
import random
import time


# Function to simulate a checkout process for customers in self-checkout lines
def self_checkout_cashier(line_id, customers):
    print(f"Self-checkout line  {line_id} starts processing.")

    for customer in customers:
        right_process_customer(line_id, customer)
    print(f"Self-checkout line {line_id} has finished processing.")
    # print('')

# Function to simulate a cashier processing customers in a single checkout line
def traditional_cashier(line_id, customers):
    print(f"Cashier at line {line_id} starts processing.")

    for customer in customers:
        process_customer(line_id, customer)
    print(f"Cashier at line {line_id} has finished processing.")
    # print('')


# Function to simulate processing of a customer by self_checkout
def left_process_custmer(line_id, customer):
    print(f"Line {line_id} processing customer {customer}...")
    print(f"Line {line_id} finished processing customer {customer}.")


# Function to simulate processing of a customer by trained cashier
def process_customer(line_id, customer):
   
    print(f"Line {line_id} processing customer {customer}...")
   
    print(f"Line {line_id} finished processing customer {customer}.")


# Function to simulate processing of a customer by trained cashier for 15 max items
def right_process_customer(line_id, customer):
   
    print(f"Line {line_id} processing customer {customer}...")
    print(f"Line {line_id} finished processing customer {customer}.")



# Main function to simulate the supermarket checkout process
def main():
    start_time = time.time()
    num_customers = int(input('Enter total number of customers in supermarket: '))  # Total number of customers
    print('')

    num_self_checkout_lines = 4  # Number of self-checkout lines
    num_traditional_lines = 3  # Number of traditional checkout lines

    customers = list(range(1, num_customers + 1))

    mid_point = len(customers) // 2
    self_checkout_customers = customers[:mid_point]
    traditional_checkout_customers = customers[mid_point:]


    # Divide customers among self-checkout lanes
    self_checkout_group = [self_checkout_customers[i::num_self_checkout_lines] for i in range(num_self_checkout_lines)]

    # Divide customers among traditional checkout lanes
    traditional_checkout_group = [traditional_checkout_customers[i::num_traditional_lines] for i in range(num_traditional_lines)]

    threads = []

    # Start threads for self-checkout cashier
    for i in range(num_self_checkout_lines):
        thread = threading.Thread(target=self_checkout_cashier, args=(i + 1, self_checkout_group[i]))
        threads.append(thread)
        thread.start()

    # Start threads for traditional cashiers
    for i in range(num_traditional_lines):
        thread = threading.Thread(target=traditional_cashier, args=(i + 1, traditional_checkout_group[i]))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print('')
    print("All customers have been processed.")
    print('')

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()