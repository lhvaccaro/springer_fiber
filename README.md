# springer_fiber
Code written to automate the calculations for Springer fiber research advised by Professor Julianna Tymoczko at Smith College.

All code in this initial version of the repo works for balanced Yamanouchi words only, however I beleive that this code can be adapted 
to work for non-Yamanouchi words as well. 

## Outline of the files in this repo
- springer_n_letters.py
- generate_x.m
- genreate_springer_matrix.m

## springer_n_letters.py
This is the Python script that produces an arc diagram for non-crossing matchings for a bmt balanced Yamanouchi word. 
At the moment, it only works for bmt words, but it can be adapted to fit any number of blocks


### function: build_position_matrix(word, letters_used)
inputs:
- word: a string value of the letters in the word. ex "bbbmmmttt"
- letters_used: type: list. a list of all letters used in the word, IN ORDER. 
ex. [b,m,t], [b,f,s,t] or [b,t]

* note: all of the letters in word must also be present in letters_used. All letters in letters_used should 
be in the same order of appearence as the balanced Yamanouchi word

output: m. m is a list of lists of index values for each letter in the word. 
Example:
word = "bbbmmmttt"

m = [[0,1,2], 
     [3,4,5],
     [6,7,8]]
Hence, in the word provided, there are b's at indicies 0,1,2, 
m's at indicies 3,4,5, and t's at indicies 6,7,8 

note that since m is a list of lists, 
m[0] = [0,1,2] which represents b
m[1] = [3,4,5] which represents m
m[2] = [6,7,8] which represents t
observe that these are lists, not single numbers. 

Also note that for letters_used = [b,m,t], 
letters_used[0] = b
letters_used[1] = m
letters_used[2] = t

These indicies all line up, which means we can use them to add values into m faster

### function: make_arcs_list(m, letters_used, color_list, result)
inputs:
m -- output of build_position_matrix()
letters_used -- ordered list of all letters in the word
color_list -- ordered list of colors being used in the graph. 
the colors should match the conventions of a bmt balanced yamanouchi word
result -- a list of lists, 
the smaller list contains the starting point of the arc, the endpoint of the arc, and the color,
the outer list is a list of the smaller lists

variables:
count_lines -- represents the number of times make_lines() is called
