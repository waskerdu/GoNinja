# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:20:22 2017
Board Library
@author: Riley
"""

'''
how to use
b=board(4)               creates a 4x4 board
b.printBoard()           prints the board to a console
b.placePiece(1,1,1)      places a piece at location (1,1) with a value of 1
'''

class Board:
    data=[]
    def __init__(self,width):
        for i in range(width):
            toAdd=[]
            for f in range(width):
                toAdd.append(0)
            self.data.append(toAdd)
    def printBoardInt(self):
        for col in self.data:
            out=''
            for row in col:
                out+=str(row)
            print(out)
    def placePiece(self,row,column,val):
        self.data[row][column]=val
    def getCell(self,x,y):
        return self.data[x][y]