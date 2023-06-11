# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    nested-lists.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/28 02:19:00 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/09 02:29:13 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def header(s):
    print('\n=========', s.upper(), '============')
def debug(s):
    print('--- ',s)
    

header('NESTED-DATA')
nested1 = [['a','b','c'],['d','e','f'],['g','h','i']]
print('first inner-list item: ', nested1[0])
print('size of outer list', len(nested1))

nested1.append(['j'])

print('print each nested list:')
for L in nested1:
    print(L)