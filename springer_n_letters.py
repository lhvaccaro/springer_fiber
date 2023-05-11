from numpy import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def main():

    word = "bbbbmtmtmtmtbmtbmtbmtbmtbmt"
    letters_used = ['b','m','t']
    result = list()
    m = build_position_matrix(word, letters_used)
    result = list()
    color_list = ["red","blue","green"]

    arcs_list = make_arcs_list(m, letters_used, color_list, result)
    print(arcs_list)
    draw_diagram(word, arcs_list)
    return 0
    #Plot the Noncrossing matchings


#draws the arc diagram 
def draw_diagram(word, arcs_list):
    fig, ax = plt.subplots()
    
    #[0,1,...,n] where n is the length of the word
    x = range(0, len(word))
    
    #A set of 0s which are meant to pair with each x value
    y = [0] * len(word)
    scale = 1
    
    #Plot black points for each letter in the word ('k'=black 'o'=point)
    plt.plot(x, y, 'ko')
    
    #Plot letter under its respective location 
    for i in range(len(word)):
        ax.annotate(word[i], (x[i], 0), xytext=(x[i]-0.1, -0.15))
    
    for arc in arcs_list:
        #Start point of the arc 
        start = arc[0]
        
        #End point of the arc
        end = arc[1]
        
        #Distance between start point and end point
        distance = end-start
        
        #Height of the arc
        height = distance/len(word)
        
        #(x,y) points to interpolate over for each arc
        
        #5 points equal distance apart between the start and end point inclusive
        X = np.array([start, (3*start+end)/4, (start+end)/2, (start+3*end)/4, end])
        
        #The height of the arc is a function of the distance between the start and end point
        Y = np.array([0, 3*height/4, height, 3*height/4, 0])
        
        #Interpolate over (x,y) points previously defined
        X_Y_Spline = make_interp_spline(X, Y)
        
        #Returns evenly spaced numbers over a specified interval
        #500 is the number of numbers in the interval. We want it high so that the arcs are smooth
        X_ = np.linspace(X.min(), X.max(), 500)
        Y_ = X_Y_Spline(X_)
        
        #Plot the arc between the start and end points with the specified color
        plt.plot(X_, Y_, arc[2])
     
    #Creating the Graph
        
    #Specify the x and y axis intervals
    plt.axis([x[0]-1, x[len(x)-1]+1, -scale, scale])
    
    #Hide the axis
    plt.axis('off')
    
    #Add a title for the plot
    plt.title("Non-Crossing Matchings for "+word)
    
    #Show the graph
    plt.show()
    return 0


def make_lines(b,t,color, result):

    # the base case
    if (len(b) == 0):
        return result
    

    # recursive case
    else: 
        # initializing beginning and ending of the line
        beginning = 0
        ending = t[0]

        #assigning the pairings 
        for i in range(0, len(b)):
            if (ending > b[i] and beginning < b[i]):
                beginning = b[i]

        #making the line array + adding to result
        line = [beginning, ending, color]
        result.append(line)

        #removing endpoints from the lists
        b.remove(beginning)
        t.remove(ending)

        return make_lines(b, t, color, result)
'''
function: build_position_matrix(word, letters_used)
inputs:
- word: a string value of the letters in the word. ex "bbbmmmttt"
- letters_used: type: list. a list of all letters used in the word, IN ORDER. 
ex. [b,m,t] or [b,t]

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
'''
def build_position_matrix(word, letters_used):
    m = list()

    #initializing m by making a list for every unique letter and adding it to m
    for i in range(0, len(letters_used)):
        new_list = list() 
        m.append(new_list) 
    
    #looping through the word, adding an index value for each letter in the appropriate spot in m
    for i, char in enumerate(word):
        m[letters_used.index(word[i])].append(i)
    
    return m
'''
function: make_arcs_list(m, letters_used, color_list, result)
inputs:
m -- output of build_position_matrix()
letters_used -- ordered list of all letters in the word
color_list -- ordered list of colors being used in the graph. 
as of right now, the colors probably don't match the conventions
result --

variables:
count_lines -- represents the number of times make_lines() is called
'''
def make_arcs_list(m, letters_used, color_list, result):
    count_lines =0
    for i in range(0,len(letters_used)):
        for j in range(0,len(letters_used)):
            if i<j:
                make_lines(m[i].copy(), m[j].copy(), color_list[count_lines],result)
                count_lines = count_lines+1
    
    return result

if __name__ == "__main__":
    main()