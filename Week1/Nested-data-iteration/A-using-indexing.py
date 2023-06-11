# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    using-indexing.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 00:06:35 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 00:11:10 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Using indexing, retrieve the string 'willow' from the list and asign thatt to the variable plant.
# complicated data structure 

data = ['a','b','c',[1,2,3,[]], [['willow','birch'],['elm','apple']]]


print("this is how we access willow: ",data[4][0][0])