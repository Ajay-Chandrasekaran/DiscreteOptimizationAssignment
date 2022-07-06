#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from solver import solve_it


if __name__ == '__main__':
    cwd = os.getcwd()
    output_file = os.path.join(
        cwd, 'results', input('output file? ').strip())

    try:
        datafiles = os.listdir(os.path.join(cwd, 'knapsack', 'data'))
        for file in datafiles:
            with open(file, 'r') as input_data_file:
                result = solve_it(input_data_file.read())

            value_str = result.split('\n')[0].split()[0] + ', ' + file

            with open(output_file, 'a') as op_file:
                op_file.write(value_str)
    except Exception as e:
        print(e)
