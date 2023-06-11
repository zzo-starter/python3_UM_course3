# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D-nested-iteration.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 11:41:08 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 11:45:48 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

nested1= [['a','b','c'],['1','2','3'],['d','e','f']]

for x in nested1:
    print('level1: ')
    for y in x:
        print('    level2: ' + y )
        
"""
level1: 
    level2: a
    level2: b
    level2: c
level1: 
    level2: 1
    level2: 2
    level2: 3
level1: 
    level2: d
    level2: e
    level2: f
"""