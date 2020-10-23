#! /usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/game-of-life/
# According to the Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the
# following four rules (taken from the above Wikipedia article):
# 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by over-population..
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its
# current state. The next state is created by applying the above rules simultaneously to
# every cell in the current state, where births and deaths occur simultaneously.
#
# Example:
# Input: [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
# output will be: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
#
from Utils.timer_decorater import timer


class Solution(object):
    # Time: o(mn)
    # Space: o(mn)

    @timer
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        neighbors = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        copy_board = [[col for col in row] for row in board]

        for x in range(rows):
            for y in range(cols):

                live_nums = 0
                for neighbor in neighbors:
                    dx = x + neighbor[0]
                    dy = y + neighbor[1]

                    if (0 <= dx < rows) and (0 <= dy < cols) and copy_board[dx][dy] == 1:
                        live_nums += 1

                if copy_board[x][y] == 1 and (live_nums < 2 or live_nums > 3):
                    board[x][y] = 0

                if copy_board[x][y] == 0 and live_nums == 3:
                    board[x][y] = 1

        return board


class Solution2(object):
    # Time: o(2mn)
    # Space: o(1)

    @timer
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        neighbors = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

        for x in range(rows):
            for y in range(cols):

                live_nums = 0
                for neighbor in neighbors:
                    dx = (x + neighbor[0])
                    dy = (y + neighbor[1])

                    if (0 <= dx < rows) and (0 <= dy < cols) and abs(board[dx][dy]) == 1:
                        live_nums += 1

                if board[x][y] == 1 and (live_nums < 2 or live_nums > 3):
                    board[x][y] = -1

                if board[x][y] == 0 and live_nums == 3:
                    board[x][y] = 2

        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

        return board


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    # print(Solution().gameOfLife(board))
    print(Solution2().gameOfLife(board))
