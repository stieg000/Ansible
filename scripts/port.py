#!/bin/bash/python3
import sys
import ast
import re

data = ast.literal_eval(sys.argv[1])
port_pattern = r'\d+/\d+/[a-zA-Z]\d+/\d+'
port_list = []

if __name__ == "__main__":
    for lines in data[6:]:
        if 'conn' not in lines:
            a = lines.split()
            filtered_list = [item for item in a if item]
            if filtered_list:
                match_result = re.match(port_pattern, filtered_list[0])  
                if match_result:
                    port_data =  match_result.group()
                    port_list.append(port_data)


    for port in port_list:
        print(port)

