import csv
import numpy as np
import pandas as pd

with open("./grocery_dataset.csv", "r") as file:
    file_contents = csv.reader(file)
    num_of_rows = len(file.readlines())
    file.seek(0)
    columns = []
    for row in file_contents:
        for elem in row:
            columns.append(elem)
    # python sets are unordered but dict is ordered
    columns = list(dict.fromkeys(columns))
    num_of_columns = len(columns)

    transactional_matrix = np.zeros((num_of_rows, num_of_columns), dtype="b")
    file.seek(0)
    for i, row in enumerate(file_contents):
        for elem in row:
            if elem in columns:
                j = columns.index(elem)
                transactional_matrix[i][j] = 1

    df = pd.DataFrame(transactional_matrix)
    df.index += 1
    df.to_csv("transactional_matrix.csv", header=columns)
    print(df)
