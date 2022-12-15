# Task 5 Реализуйте алгоритм перемешивания списка.

import random

test_list = [1, 4, 5, 6, 3]                                 #  инициализирующий список

print("Первоначальный список таков : " + str(test_list))    #Printing original list Печать оригинального списка

res = random.sample(test_list, len(test_list))              #using random.sample() использование random.sample()
                                                            # to shuffle a list  чтобы перетасовать список


print("Перемешеный список : " + str(res))                   #Printing shuffled list Печать перетасованного списк
