import multiprocessing
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

    scissors = """
                 _______
             ---'   ____)____
                       ______)               Parallel Computing:
                    __________)
                   (____)
             ---.__(___)
     """
    print(scissors)

    total_self_checkout_customers = int(input('\nEnter total self-checkout customers: '))

    total_traditional_checkout_customers = list( range( 1, int(input('Enter total traditional customers: '))))
    traditional_customer1 = total_traditional_checkout_customers [:len(total_traditional_checkout_customers)//2]
    traditional_customer2 = total_traditional_checkout_customers [len(total_traditional_checkout_customers)//2:]

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

    self_lane1 = multiprocessing.Process(target=self_checkout_cashier, args=[1, distributed_self_checkout_customers[0]])
    self_lane2 = multiprocessing.Process(target=self_checkout_cashier, args=[2, distributed_self_checkout_customers[1]])
    self_lane3 = multiprocessing.Process(target=self_checkout_cashier, args=[3, distributed_self_checkout_customers[2]])
    self_lane4 = multiprocessing.Process(target=self_checkout_cashier, args=[4, distributed_self_checkout_customers[3]])

    traditional_lane1 = multiprocessing.Process(target=traditional_cashier, args=[1, traditional_customer1])
    traditional_lane2 = multiprocessing.Process(target=traditional_cashier, args=[2, traditional_customer2])
    less_item_lane = multiprocessing.Process(target=fifteen_item_cashier, args=[1, fifteen_item_checkout_customer ])

    start = time.perf_counter()

    self_lane1.start()
    self_lane2.start()
    self_lane3.start()
    self_lane4.start()

    traditional_lane1.start()
    traditional_lane2.start()

    less_item_lane.start()

    self_lane1.join()
    self_lane2.join()
    self_lane3.join()
    self_lane4.join()

    traditional_lane1.join()
    traditional_lane2.join()

    less_item_lane.join()

    finish = time.perf_counter()

    print(f'\nRuntime in: {round(finish-start)} second(s)')

