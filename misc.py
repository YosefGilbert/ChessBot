import constraints
from gametree import GameTree
from constraints import Board
import time
from datetime import timedelta


def FENtoArr(fen_string):
    board = []
    for i in range(0, 8):
        row = []
        for j in range(0, 8):
            row.append("0")
        board.append(row)
    curr_row = 0
    curr_col = 0
    for char in fen_string:
        if not char.isdigit() and char != "/":
            board[curr_row][curr_col] = char
            curr_col += 1
        if char.isdigit():
            curr_col += int(char)
        if char == "/":
            curr_col = 0
            curr_row += 1
    return board


def playMinimax(play_as="1", start_fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR", depth=4):
    start_board = FENtoArr(start_fen)
    game_tree = GameTree(start_board, depth)
    game_tree.root_position.printBoard()

    if play_as == "2":
        starttime = time.perf_counter()

        computer_move = game_tree.find_best_move()
        game_tree.root_position = computer_move
        computer_move.printBoard()

        duration = timedelta(seconds=time.perf_counter() - starttime)
        print("Thought for", duration, "seconds")

    while True:
        human_move = input("Move:\n")

        while not move(human_move, game_tree):
            print("please enter a legal move!")
            human_move = input("Move:\n")

        starttime = time.perf_counter()

        game_tree.root_position.printBoard()

        computer_move = game_tree.find_best_move()
        game_tree.root_position = computer_move
        computer_move.printBoard()
        duration = timedelta(seconds=time.perf_counter() - starttime)
        print("Thought for", duration, "seconds")

'''
def playML(play_as="1"):
    start_board = FENtoArr("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
    game_tree = GameTree(start_board, 0)
    game_tree.root_position.printBoard()
    while True:
        human_move = input("Move:\n")

        while not move(human_move, game_tree):
            print("please enter a legal move!")
            human_move = input("Move:\n")

        starttime = time.perf_counter()

        game_tree.root_position.printBoard()

        best_pos = ml.get_best_pos(game_tree.root_position.current_position)
        game_tree.root_position.current_position = best_pos
        game_tree.root_position.printBoard()

        duration = timedelta(seconds=time.perf_counter() - starttime)
        print("Thought for", duration, "seconds")
'''


def move(alg_long, game_tree):
    if 96 < ord(alg_long[0]) < 105 and ord(alg_long[0]) != 98:
        new_board = game_tree.root_position.generatePosition(8 - int(alg_long[1]), ord(alg_long[0]) - 97, 8 - int(alg_long[3]), ord(alg_long[2]) - 97, "")
    else:
        new_board = game_tree.root_position.generatePosition(8 - int(alg_long[2]), ord(alg_long[1]) - 97, 8 - int(alg_long[5]), ord(alg_long[4]) - 97, "")

    if new_board in game_tree.root_position.findLegalPositions():
        game_tree.root_position = Board(new_board, game_tree.root_position.half_move + 1)
        return True
    else:
        return False
