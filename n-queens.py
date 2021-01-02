# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:38:17 2020

@author: iNaz

"""

import random

def get_h(board):
  h = 0

  for i in range(len(board)):
    for j in range(i + 1,len(board)):
        #same row
        if board[i] == board[j]:
            h += 1
      
        #distetnce between columns
        distence = j - i  
        
        #same diagonal
        #(if  adding or subtracting 1 unit puts them in 
        #the same row then they are in the same diagonal)      
        if( board[i] == board[j] - distence or board[i] == board[j] + distence):
            h += 1
     
  return h

def hill_climbing (board):
  #calculate h- value for current position  
  best_h = get_h(board)    
             
  best_col = 0                         
  best_row = 0 
  count = 0
  
  #loop through board
  for col in range(len(board)):        
    for row in range(len(board)):
      
      if board[col] == row:
        #cause we already know the h-value
        #of the current positioon we skip  
        continue
       
      board_copy = list(board)
      
      #move the queen to the new row
      board_copy[col] = row
      
      #calculate h for the new board 
      new_h_cost = get_h(board_copy) 
      
      #print("new_h_cost",new_h_cost)
      
      #check if there exist some place higher (hill cmibing)
      if (new_h_cost < best_h):
        
        count+=1
        best_h = new_h_cost
        best_col = col
        best_row = row
        
  #this means we never entered the if codition 
  if (count == 0):
      
      print("Local Optimal: ",board_copy)       
      #the answer we found is in fact the optimal answer
      if (get_h (board) == 0):
          print("Optimal Solution: ",board)
          
          
      #the answer we found is not the optimal answer
      #so we just restart the algorithm
      else:
          print("Random Restart\n")
          randomlist = random.sample(range(0, n), n)
          print("Start again: ",randomlist)
          hill_climbing (randomlist)
  #this means we found a better h_value so we change the board
  #so we change the board and continue climbing     
  elif (count !=0):
      board[best_col] = best_row
      print("new board: ",board)
      hill_climbing (board)
      
  return board


n = int(input("How many queens?"))
#Generate n random numbers between 0 and n-1
initial_state = random.sample(range(0, n), n)
print("Initial State: ",initial_state)
hill_climbing (initial_state)



