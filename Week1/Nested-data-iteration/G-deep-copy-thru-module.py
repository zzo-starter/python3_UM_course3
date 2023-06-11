# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    g-deep-copy-thru-module.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 22:49:51 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 22:53:51 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import copy


original = [ ['a', ['b1','b2']], ['c', ['d1','d2']] ]


print("original list: ", original)

deep_copy = copy.deepcopy(original)
 
print("deep_copy list: ", deep_copy)

print()

deep_copy.append(['e','f','g'])

print("original list: ", original)
print("deep_copy list: ", deep_copy)

"""

original list:  [['a', ['b1', 'b2']], ['c', ['d1', 'd2']]] 
deep_copy list:  [['a', ['b1', 'b2']], ['c', ['d1', 'd2']]]

original list:  [['a', ['b1', 'b2']], ['c', ['d1', 'd2']]]
deep_copy list:  [['a', ['b1', 'b2']], ['c', ['d1', 'd2']], ['e', 'f', 'g']]

"""