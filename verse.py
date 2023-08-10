def main():
    # Parse input for Train A
    input_train_a = input().split()
    engine_a, bogies_a = input_train_a[1], input_train_a[2:]

    # Parse input for Train B
    input_train_b = input().split()
    engine_b, bogies_b = input_train_b[1], input_train_b[2:]

    # Find the index of HYB in bogie orders
    hyb_index_a = bogies_a.index("HYB") if "HYB" in bogies_a else len(bogies_a)
    hyb_index_b = bogies_b.index("HYB") if "HYB" in bogies_b else len(bogies_b)

    # Arrival order of bogies at Hyderabad for Train A and Train B
    arrival_order_a = [engine_a] + bogies_a[:hyb_index_a]
    arrival_order_b = [engine_b] + bogies_b[:hyb_index_b]

    # Departure order of bogies for merged Train AB
    departure_order_ab = [engine_a, engine_b] + bogies_a[hyb_index_a:] + bogies_b[hyb_index_b:]

    # Print the results
    print("ARRIVAL TRAIN_A", " ".join(arrival_order_a))
    print("ARRIVAL TRAIN_B", " ".join(arrival_order_b))
    print("DEPARTURE TRAIN_AB", " ".join(departure_order_ab))

if __name__ == "__main__":
    main()
