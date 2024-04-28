def remove_duplicates(customer_ids):
    unique_customer_ids = set(customer_ids)
    return unique_customer_ids

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_customer_ids = remove_duplicates(customer_ids)

print("Unique customer IDs:", unique_customer_ids)
