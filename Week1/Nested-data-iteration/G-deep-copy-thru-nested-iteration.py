# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    G-deep-copies.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 21:20:20 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 22:20:19 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# deep-copying using nested iteration works for making deep copies 
# if we know how many levels of nesting we have and we have a parallel structure in our nesting

print("deep copying using nested iteration...")

original= [['dogs','puppies'],['cats','kittens']]

print("original list: ", original)

copied_outer_list = [] #init outer
for inner_list in original: 
    copied_inner_list = [] #init inner
    for item in inner_list:
        copied_inner_list.append(item) #add to new inner
    copied_outer_list.append(copied_inner_list) #add to new outer
    
print("new deep-copy1: ", copied_outer_list)    

print()

print("original list: ", original)
copied_outer_list2 = [] #init outer
for inner_list in original: 
    copied_inner_list2 = inner_list[:] #can shallow copy inner-list
    copied_outer_list2.append(copied_inner_list2) #add to new outer

copied_outer_list2[0].append(['redbull']) #shallow-copy test 

print("original list: ", original)    
print("new deep-copy2: ", copied_outer_list2) 

"""

deep copying...
original list:  [['dogs', 'puppies'], ['cats', 'kittens']]
new deep-copy1:  [['dogs', 'puppies'], ['cats', 'kittens']]

original list:  [['dogs', 'puppies'], ['cats', 'kittens']]
original list:  [['dogs', 'puppies'], ['cats', 'kittens']]
new deep-copy2:  [['dogs', 'puppies', ['redbull']], ['cats', 'kittens']]

"""