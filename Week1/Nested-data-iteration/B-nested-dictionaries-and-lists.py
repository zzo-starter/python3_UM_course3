# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    B-nested-dictionaries-and-lists.py                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zoozdev777 <zoozdev777@gmail.com>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/10 00:19:04 by zoozdev777        #+#    #+#              #
#    Updated: 2023/06/10 00:24:34 by zoozdev777       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#access colors

info = {
        'personal_data':
            {
                'name':'Lauren',
                'age':20,
                'major':'Information Science',
                'physical_features':
                    {
                        'color': {'eye': 'blue','hair': 'brown'},
                        'height': "5'8"              
                    },
                'other':
                    {
                        'favorite_colors': ['purple','green','blue'],
                        'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
                    }
            }
    }

print("---PHYS FEAT COLORS: ", info['personal_data']['physical_features']['color'])
print("---FAVORITE COLORS: ", info['personal_data']['other']['favorite_colors'])