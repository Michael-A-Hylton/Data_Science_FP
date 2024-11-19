import numpy as np
from GameLoop import gameloop

player_num=1
sub_array = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

array_of_arrays = np.array([sub_array] * 9).reshape(3, 3, 3, 3)
print(array_of_arrays[0])
square=input("Which square do you want your first play to be"+
             "\n1, 2, 3\n4, 5, 6\n7, 8, 9\n")

big_square=input("Which square would you like to play your first move in\n1, 2, 3\n4, 5, 6\n7, 8, 9\n")
gameloop(int(big_square),array_of_arrays,player_num)

