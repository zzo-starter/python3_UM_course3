import json
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    json.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 00:30:14 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 00:47:45 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def pretty(o):
    #serializes json Object to string and formats
    #can sort by keys
    return json.dumps(o, sort_keys = True, indent = 2)

d = {'key2':{'e':5,'d':90 }, 'key1':{'b':15,'a':190, 'c':"yes"}}

print('d: ', d)
print()
print('pretty: ', pretty(d))

"""
pretty:  {
  "key1": {
    "a": 190,
    "b": 15,
    "c": "yes"
  },
  "key2": {
    "d": 90,
    "e": 5
  }
}
"""

 
 