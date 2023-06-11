# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    F-shallow-copies.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 15:18:03 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 16:03:42 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# SHALLOW-COPIES

original = [['dogs','puppies',[]],['cats','kittens',[[]]],['rabbits','rabbs'],['horses','horsies']]

copied_version1 = original #SHALLOW COPY; not really copying; just storing reference in another variable; CREATED AN ALIAS
copied_version2 = original[:] #SHALLOW COPY; not really copying; just storing reference in another variable; CREATED AN ALIAS [from:to]
copied_version3 = original[1:3] #SHALLOW COPY; not really copying; just storing reference in another variable; CREATED AN ALIAS [from:to]
copied_version4 = original.copy() #SHALLOW COPY; not really copying; just storing reference in another variable; CREATED AN ALIAS [from:to]


print('original: ', original)
print('copy1: ', copied_version1)
print('copy2: ', copied_version2)
print('copy3: ', copied_version3)
print('copy4: ', copied_version4)
print()
print('copy2 is original? ',copied_version2 is original)
print('copy3 is original? ',copied_version3 is original)
print('copy2 same as original? ', copied_version2 == original)
print('copy3 same as original? ', copied_version3 == original)
print('copy4 same as original? ', copied_version4 == original)

original[0].append(['canines']) #append to 1st tier
original[0][2].append(['pup1']) #append to 2nd tier
copied_version2[0][2].append(['pup2']) #append to 2nd tier 
copied_version3[0][2].append(['pup3']) #append to 2nd tier 
copied_version4[0][2].append(['pup4']) #append to 2nd tier 


print()
print('original: ', original)
print('copy1: ', copied_version1)
print('copy2: ', copied_version2)
print('copy3: ', copied_version3)
print('copy4: ', copied_version4)

"""

original:  [['dogs', 'puppies', []], ['cats', 'kittens', [[]]], ['rabbits', 'rabbs'], ['horses', 'horsies']]
copy1:  [['dogs', 'puppies', []], ['cats', 'kittens', [[]]], ['rabbits', 'rabbs'], ['horses', 'horsies']]
copy2:  [['dogs', 'puppies', []], ['cats', 'kittens', [[]]], ['rabbits', 'rabbs'], ['horses', 'horsies']]
copy3:  [['cats', 'kittens', [[]]], ['rabbits', 'rabbs']]
copy4:  [['dogs', 'puppies', []], ['cats', 'kittens', [[]]], ['rabbits', 'rabbs'], ['horses', 'horsies']]

copy2 is original?  False
copy3 is original?  False
copy2 same as original?  True
copy3 same as original?  False
copy4 same as original?  True

original:  [['dogs', 'puppies', [['pup1'], ['pup2'], ['pup4']], ['canines']], ['cats', 'kittens', [[], ['pup3']]], ['rabbits', 'rabbs'], ['horses', 'horsies']]
copy1:  [['dogs', 'puppies', [['pup1'], ['pup2'], ['pup4']], ['canines']], ['cats', 'kittens', [[], ['pup3']]], ['rabbits', 'rabbs'], ['horses', 'horsies']]
copy2:  [['dogs', 'puppies', [['pup1'], ['pup2'], ['pup4']], ['canines']], ['cats', 'kittens', [[], ['pup3']]], ['rabbits', 'rabbs'], ['horses', 'horsies']]
copy3:  [['cats', 'kittens', [[], ['pup3']]], ['rabbits', 'rabbs']]
copy4:  [['dogs', 'puppies', [['pup1'], ['pup2'], ['pup4']], ['canines']], ['cats', 'kittens', [[], ['pup3']]], ['rabbits', 'rabbs'], ['horses', 'horsies']]

"""