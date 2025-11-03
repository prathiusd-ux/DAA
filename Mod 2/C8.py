import sys

def acquire_matrix_data(name_tag):
    num_rows = int(input("enter number of rows:"))
    num_cols = int(input("enter number of columns:"))
    print("enter the elements row by row:")
    matrix_storage = []
    
    for row_index in range(num_rows):
        current_row = []
        print(f"enter elements for the rows {row_index+1}:")
        for col_index in range(num_cols):
            element_value = int(input(f"element {col_index+1}:"))
            current_row.append(element_value)
        matrix_storage.append(current_row)
    return matrix_storage, num_rows, num_cols

set_one_data = acquire_matrix_data("matrix 1")
InputMatrixA = set_one_data[0]
rows_A = set_one_data[1]
cols_A = set_one_data[2]

set_two_data = acquire_matrix_data("matrix 2")
InputMatrixB = set_two_data[0]
rows_B = set_two_data[1]
cols_B = set_two_data[2]


if cols_A != rows_B:
    print("invalid. pls enter same no. of rows for matrix 2 as columns for 1")
    # Using sys.exit() to stop execution after an error message for clarity
    sys.exit() 
else:
    # 1. Initialize result matrix
    output_matrix = []
    for i_dim in range(rows_A):
        new_row = []
        for j_dim in range(cols_B):
            new_row.append(0)
        output_matrix.append(new_row)

    # 2. Perform multiplication
    for i_out in range(rows_A):
        for j_out in range(cols_B):
            for k_sum in range(rows_B): # k runs up to the common dimension (cols_A or rows_B)
                output_matrix[i_out][j_out] += InputMatrixA[i_out][k_sum] * InputMatrixB[k_sum][j_out]
                
    # 3. Print final matrix
    print("resultant matrix:")
    for row_data in output_matrix:
        print(row_data)