"""
Author: Sujana Basnet
Lab: 10
File: ticTacToeGUI.py
This program displays a window with multiple buttons and played tic tac toe.
"""

#Import Modules
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from ticTacToe import TicTacToe

class TicTacToeGUI(EasyFrame):

    def __init__(self):
        """Creates the tic tac toe game, sets up buttons for each play space, a current turn label,  and a restart button."""
        super().__init__(title = "Tic Tac Toe!")
        self.game = TicTacToe()

        self.setSize(64 * len(self.game.board), 64 * len(self.game.board[0]))

        self.tokenImages = {
            " " : PhotoImage(file = "empty.png"),
            "X" : PhotoImage(file = "x.png"),
            "O" : PhotoImage(file = "o.png")}

        self.stateLabel = self.addLabel("Turn:", row = len(self.game.board) + 1, column = 0)
        self.turnLabel = self.addLabel("", row = len(self.game.board) + 1, column = 1)

        self.boardButtons = []
        for row in range(len(self.game.board)):
            self.boardButtons.append([])
            for column in range(len(self.game.board[row])):
                self.boardButtons[row].append(self.addButton(text = "", row = row, column = column,
                                                             command = self.makeButtonFunction(row, column),
                                                             state = "normal",))
                (self.boardButtons[row][column])["image"] = self.tokenImages[" "]

        self.setBoardButton()

        self.newGameButton = self.addButton(text = "New", row = len(self.game.board) + 1, column = 2,
                                            columnspan = 2, command = self.newGame, state = "disabled")

    def makeButtonFunction(self, row, column):
        """Creates a function application using the button to pass as an argument to self.nexttMove. Used by self.boardButtons."""

        return lambda: self.nextMove(row, column)

    def setBoardButton(self):
        """Sets each of the board butttons to the respective image of the token."""
        for row in range(len(self.game.board)):
            for column in range(len(self.game.board[row])):
                if self.game.board[row][column] == "":
                    (self.boardButtons[row][column])["image"] = self.tokenImages[" "]
                elif self.game.board[row][column] == "X":
                    (self.boardButtons[row][column])["image"] = self.tokenImages["X"]
                elif self.game.board[row][column] == "O":
                    (self.boardButtons[row][column])["image"] = self.tokenImages["O"]

        self.turnLabel["image"] = self.tokenImages[self.game.getTurn()]

    def nextMove(self, row, column):
        """Makes a move in the game and updates the view with the results."""

        self.game.step(row, column)
        self.setBoardButton()

        if self.game.gameOver:
            self.messageBox("Game is over!", self.game.getTurn() + " wins!")
            for row in range(len(self.game.board)):
                for column in range(len(self.game.board[row])):
                    (self.boardButtons[row][column])["state"] = "disabled"
            self.newGameButton["state"] = "normal"

    def newGame(self):
        """creates  a new  tic tac toe  and updates the view."""
        self.game = TicTacToe()

        self.setSize(64 * len(self.game.board), 64 * len(self.game.board[0]))

        self.tokenImages = {
            " " : PhotoImage(file = "empty.png"),
            "X" : PhotoImage(file = "x.png"),
            "O" : PhotoImage(file = "o.png")}

        self.stateLabel = self.addLabel("Turn:", row = len(self.game.board) + 1, column = 0)
        self.turnLabel = self.addLabel("", row = len(self.game.board) + 1, column = 1)

        self.boardButtons = []
        for row in range(len(self.game.board)):
            self.boardButtons.append([])
            for column in range(len(self.game.board[row])):
                self.boardButtons[row].append(self.addButton(text = "", row = row, column = column,
                                                             command = self.makeButtonFunction(row, column),
                                                             state = "normal"))
                (self.boardButtons[row][column])["image"] = self.tokenImages[" "]


        self.setBoardButton()

        self.newGameButton["state"] = "disabled"


def main():
    app = TicTacToeGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
                
    
