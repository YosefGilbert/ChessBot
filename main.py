
# TODO LIST
# 1. Castling (add in rules that you cant castle after moving king/rooks; cant castle through check
# 2. En passant
# 3. Change game tree structure so not the entire tree is regenerated after each move, only the bottom layer
# 4. Add kingsafety to the eval
# 5. add other attributes to eval that the bot wont pick up on (passed pawns, having a defended/connected position)

import misc


if __name__ == '__main__':
    print("Choose mode: ")
    print("1. Play from start")
    print("2. Play from given position")

    option = input()
    print("Choose depth:")
    depth = int(input())
    print("Play as: ")
    print("1. White")
    print("2. Black")
    play_as = input()
    if option == "1":
        misc.playMinimax(play_as=play_as, depth=depth)
    if option == "2":
        print("Enter start FEN: ")
        fen = input()
        misc.playMinimax(play_as, fen, depth)

