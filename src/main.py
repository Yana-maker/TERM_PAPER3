from utils import load_data, executed_operations, five_last_sorted_operations, output_data

def main():
    data = load_data()
    data = executed_operations(data)
    data = five_last_sorted_operations(data)
    data = output_data(data)
    for i in data:
        print()
        print(i)

main()