# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D-nested-iteration3.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 11:54:19 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 12:07:06 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Use nested iteration to save every string containing 'b' into a new list named b_strings


L= [['apples','bananas','blueberries','lemons'],['carrots','peas','cucumbers','green beans']]


b_strings=[]
for x in L:
    #print('@x', x)
    for y in x:
        #print('@y', y)
        if y.find('b') >=0: #<--------
            b_strings.append(y)
            
print('A b-strings: ', b_strings)

"""
b-strings:  ['bananas', 'blueberries', 'cucumbers', 'green beans']
"""


b_strings=[]
for lst in L:
    #print('@lst', lst)
    for word in lst:
        #print('@word', word)
        if 'b' in word: #<--------
            b_strings.append(word)
            
print('B b-strings: ', b_strings)

"""
b-strings:  ['bananas', 'blueberries', 'cucumbers', 'green beans']
"""
