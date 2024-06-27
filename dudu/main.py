# dudu/main.py

from collections import Counter
import argparse

def find_common_elements(lst):
    counter = Counter(lst)
    common_elements = counter.most_common()
    return common_elements

def main():
    parser = argparse.ArgumentParser(description="Find common elements in a list")
    parser.add_argument('elements', nargs='+', help='List of elements')
    args = parser.parse_args()
    
    elements = args.elements
    common_elements = find_common_elements(elements)
    
    for element, count in common_elements:
        print(f"{element}: {count}")

if __name__ == "__main__":
    main()
