# Idea: board_class, piece_class, inherit from board_class to move pieces  based on indexposition of board.

import numpy as np
import string

letters = [x.upper() for x in string.ascii_letters[:8]]
numbers = [str(x) for x in np.arange(1,9)]
notation = [x + y for x in letters for y in numbers]

''' dictionairy of piecevalues.

# p = pawn, n = knight, b = bishop, r = rook, q = queen, k = king.
# lowercase letter is white, capital letter is black. 
# negative values for black and positive for white, as used by modern engines in evaluating a position.
# evaluation of king is 0'''

pieces = [x for x in 'pnbrqk' + 'pnbrqk'.upper()]
values = 1,3,3,5,9,0,-1,-3,-3,-5,-9,0
values = {k:v for k,v in zip(pieces,values)} # check values by dict. eg. values['r'] = 5.

# create dict for checking current position of pieces with square on the board:
board = {i : {} for i in notation }

'''# create visual representation of chessboard, where 0 is white square and 1 is dark square.
# Numbers are stringtypes, so that strings of pieces can be placed with their respectful letter.
# board_visual = np.empty(64).reshape(8,8).astype(str)'''

# # 1 is black square, 0 is white square:
# for ax0_idx,row in enumerate(board_visual):
#     for ax1_idx,num in enumerate(row):
#         if (ax0_idx%2==0 and ax1_idx%2!=0) or (ax0_idx%2!=0 and ax1_idx%2==0):
#             board_visual[ax0_idx,ax1_idx] = '1'
#         else:
#             board_visual[ax0_idx,ax1_idx] = '0'


def starting_position(board,pieces):
    

    for k,v in board.items():
        if '2' in k:
            board[k] = pieces[0]
        elif '7' in k:
            board[k] = pieces[6]
        elif k=='B1' or k=='G1':
            board[k] = pieces[1]
        elif k=='B8' or k=='G8':
            board[k] = pieces[7]
        elif k=='C1' or k=='F1':
            board[k] = pieces[2]
        elif k=='C8' or k=='F8':
            board[k] = pieces[8]
        elif k=='A1' or k=='H1':
            board[k] = pieces[3]
        elif k=='A8' or k=='H8':
            board[k] = pieces[9]
        elif k=='D1':
            board[k] = pieces[4]
        elif k=='D8':
            board[k] = pieces[10]
        elif k=='E1':
            board[k] = pieces[5]
        elif k=='E8':
            board[k] = pieces[11]
        else:
            pass
        
    board_visual = np.array(list(board))
    for index,square in enumerate(board_visual):
        if square in board.keys() and board[square]!={}: # if piece on board, insert piece on board_notated.
            board_visual[index] = board[square]
    
    # board_visual checks the visual representation, while board checks the current position
    return board_visual.reshape(8,8), board

    
def current_position(board_pieces):
    pass

board_visual, board = starting_position(board,pieces)
print(board_visual)
print(board)

