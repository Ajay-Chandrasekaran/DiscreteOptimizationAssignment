#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from solver import solve_it


if __name__ == "__main__":
    cwd = os.getcwd()
    datafiles_path = os.path.join(cwd, "knapsack", "data")
    output_file = os.path.join(
        cwd, "knapsack", "results", input("output file? ").strip()
    )

    try:
        datafiles = os.listdir(datafiles_path)
        with open(output_file, "w+") as op_file:
            for file in datafiles:
                print(f"Running on {file}")

                with open(os.path.join(datafiles_path, file), "r") as input_data_file:
                    result = solve_it(input_data_file.read())

                value_str = result.split("\n")[0].split()[0] + ", " + file + "\n"
                op_file.write(value_str)
    except Exception as e:
        print(e)
