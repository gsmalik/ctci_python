import numpy as np

def place_queen(placements, row_num, N):
    if row_num==N-1:
        return_value = np.sum(placements[row_num,:] != -1)
        if return_value !=0:
            print(placements)
        return return_value
    
    ways = 0
    for column_num,square in enumerate(placements[row_num,:]):
        # print("placing at square:", row_num, column_num, "with placements\n", placements)
        if square==0:
            ways += place_queen(update_constraints(np.ndarray.copy(placements), row_num, column_num), row_num+1, N)
    return ways

def update_constraints(placements, row_num, column_num):
    # Set all squares in that row to -1
    placements[row_num, :] = -1

    # Set all squares in that col to -1
    placements[:,column_num] = -1

    # Set all diagonals from that row, col to -1
    index=0
    while index+row_num < np.shape(placements)[0] and index+column_num < np.shape(placements)[0]:
        placements[index+row_num][index+column_num] = -1
        index+=1

    index=0
    while row_num-index >= 0 and column_num-index >=0:
        placements[row_num-index][column_num-index] = -1
        index+=1

    index=0
    while row_num-index >= 0 and index+column_num < np.shape(placements)[0]:
        placements[row_num-index][index+column_num] = -1
        index+=1
    
    index=0
    while column_num-index >= 0 and index+row_num < np.shape(placements)[0]:
        placements[index+row_num][column_num-index] = -1
        index+=1

    placements[row_num][column_num]=1
    return placements

N=5
test = np.zeros((N,N))
print(place_queen(test, 0, N))