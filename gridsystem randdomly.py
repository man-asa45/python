import random #grid system
def generate_balanced_grid(rows,cols):
    if rows<3 or cols<3:
        print("Grid must be atleast 3*3 to have an inner layer.")

    while True:
        grid=[[random.randint(1,20) for _ in range(cols)] for _ in range (rows)]
        outer_sum=0 
        inner_sum=0 
        for i in range(rows):
            for j in range(cols):
                if i==0 or i==rows-1 or j==0 or j== cols-1:
                    outer_sum+=grid[i][j]
                else:
                    inner_sum+=grid[i][j]
        if inner_sum==outer_sum:
            print("\nBalanced Grid:")
            for row in grid:
                print(row)
            print(f"\nOuter layer sum={outer_sum}")
            print(f"Inner layer sum={inner_sum}")
            break
rows=int(input("Enter number of rows (min 3):"))
cols=int(input("Enter number of cols (min 3):"))
generate_balanced_grid(rows,cols)