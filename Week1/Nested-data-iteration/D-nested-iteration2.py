# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    D-nested-iteration2.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 11:46:42 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 11:52:58 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#Write code to create a new list that contains every persons last name and save that list as last_names

info = [['Tina','Turner',1939,'singer'],['Matt','Deamon',1970,'actor'],['Kristen','Wiig',1973,'comedian']]


last_names=[]
for x in info:
   last_names.append(x[1])

print("last names: ", last_names)


"""
last names:  ['Turner', 'Deamon', 'Wiig']
"""