def quiz4():
    row = int(input('Number of rows: '))
    col = int(input('Number of cols: '))
    grid = int(input('Grid size: '))

    for i in range(row+1):
        print('+' + ('-'*grid + '+')*col)
        if i < row:
            for j in  range(grid):
                  print('|' + (' '*grid + '|')*col)
