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

a_string = '\n\n\n{\n "resultCount":25,\n "results":[\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'

d = json.loads(a_string) #deserialize/ unmarshall

print("type is: ", type(d) )
print("keys: ", d.keys())
print("resCount: ", d['resultCount'])