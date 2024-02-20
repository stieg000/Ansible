#!/bin/bash/python3

import sys
import ast

network_interface_list = []

def network(data):
    for lines in data[6:-3]:
        elements = lines.split()
        if 'LAG' in elements[0] or 'N-' in elements[0]:
            network_interface_list.append(elements[0])

def main():
    input_data = ast.literal_eval(sys.argv[1])
    network(input_data)
    for int in network_interface_list:
        print(int)

if __name__ == "__main__":
    main()
