from random import randint

my_list = [randint(1, 15) for _ in range(10)]
#print(my_list)
final_list = [el for el in my_list if my_list.count(el) == 1]
#final_list = sorted(final_list)
print(f"исходный список \n {my_list}\n получившийся список\n {final_list}")
