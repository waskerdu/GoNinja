# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:19:53 2017
Go Ninja
@author: Riley
"""

import ryBoard

def turn(playerNum,myBoard):
    invalidMove=True
    while invalidMove:
        xVal=int(input("Player "+str(playerNum)+" which column will you put your pice?: "))
        yVal=int(input("Player "+str(playerNum)+" which row will you put your pice?: "))
        if myBoard.getCell(xVal,yVal)==0:
            invalidMove=False
            myBoard.placePiece(xVal,yVal,playerNum)
            myBoard.printBoardInt()
        else:
            print("that is not a valid cell")
    concede=str(input("Player "+str(playerNum)+" Do you concede? (y/n): "))
    return (concede.lower()=='y')

gameRunning=True
while gameRunning:
    size=int(input("How big do you want the board? "))
    myBoard=ryBoard.Board(size)
    myBoard.printBoardInt()
    
    matchRunning=True
    while matchRunning:
        if turn(1,myBoard):
            matchRunning=False
        elif turn(2,myBoard):
            matchRunning=False
    