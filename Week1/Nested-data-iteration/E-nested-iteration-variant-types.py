# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    E-structuring-nested-data.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 12:10:14 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 12:12:10 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

nested1 = [1,2,['a','b','c'],['d','e'],['f','g','h']]

for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("   level2: {}".format(y))
    else:
        print(x)