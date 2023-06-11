# WEEK-1 Nested Data and Nested Iteration
## A Nested Lists
     X: `nested1 = [['a','b']['c','d']['e','f']]`

## B Nested Dictionaries
    We can have multi-level nesting of both dictionaries and lists...
    info = {
        'personal_data':
        {'name':'Lauren',
        'age':20,
        'major':'Information Science',
        'physical features':
            {'color': {'eye': 'blue',
                        'hair': 'brown'},
            'height': "5'8"              
            },
        'other':
        {
            'favorite_colors': ['purple','green','blue'],
            'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
        }
        }
    } 
    #access favorite colors.

## C JSON Format and the JSON Module
    - import json for serializing/deserializing json
    - another useful function from JSON module is DUMPS

# WEEK-1 Nested Iteration
- iterating thru complex nested data structures 
- nested iteration to access nested data within dictionary, lists using nested for-loops
- deep vs shallow copying in nested structures
- inner list/dict shared amongst multiple outer objects; make deep copies vs shallow copies to avoid

## D Nested Iteration
- nested iterations via for-loops 

## E Nested Structures
- structuring nested data
- iterating thru variant types/structures

## F Shallow Copies
- making shallow copies is by reference; creating a new variable as an alias, not a real copy
- `copy()`
- `[:]` 
- `=`

## G Deep Copies
- making deep copies using `NESTED ITERATION`
    ### STATIC LIST STRUCTURE (consitent struct)
    deep-copying using nested iteration works for making deep copies 
    if we know how many levels of nesting we have and we have a parallel structure in our nesting
    
    ### DYNAMIC LIST STRUCTURE (variant struct)
    ~ x = [ ['a', ['b1','b2']], ['c', ['d1','d2']] ]
    - one way is to use recursion to handle complex structs
    - an easier way is to use `COPY.DEEPCOPY`

## H Extracting from Nested Data
- navigating thru and understanding a complex json struct
    like a response from Twitter API
- navigate thru one layer at a time
- use `json.dumps(s, indent=2)[:100]` # show the first 100 lines
- `type(res)`
- `res.keys()`
- use JSON online tool