from project import *


def test_new_board():
    gamepanel = Board()
    board = new_board(gamepanel)

    for row in board:
        for piece in row:
            assert piece == 0

    assert type(board) == list
    assert len(board) == 4


def test_get_random():
    gamepanel = Board()
    get_random(gamepanel)
    get_random(gamepanel)
    generated_tile = 0
    is_2 = 0
    is_4 = 0
    is_8 = 0
    for i in range(gamepanel.boardSize):
        for j in range(gamepanel.boardSize):
            if gamepanel.gameTile[i][j] != 0:
                generated_tile += 1
            elif gamepanel.gameTile[i][j] == 2:
                is_2 += 1
            elif gamepanel.gameTile[i][j] == 4:
                is_4 += 1
            elif gamepanel.gameTile[i][j] == 8:
                is_8 += 1
    assert generated_tile == 2
    assert is_2 >= 0 or is_4 >= 0 or is_8 >= 0


def test_is_mergable():
    gamepanel = Board()
    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    assert is_mergeable(gamepanel) == True

    gamepanel.gameTile = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],]
    assert is_mergeable(gamepanel) == False

    gamepanel.gameTile = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 16],]
    assert is_mergeable(gamepanel) == False

    gamepanel.gameTile = [[1, 2, 2, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],]
    assert is_mergeable(gamepanel) == True

    gamepanel.gameTile = [[1, 2, 3, 4], [5, 2, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],]
    assert is_mergeable(gamepanel) == True


def test_reverse():
    gamepanel = Board()
    gamepanel.gameTile = [[2, 2, 4, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    reverse(gamepanel)
    assert  gamepanel.gameTile == [[8, 4, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [2, 2, 4, 8], [0, 0, 0, 0], [0, 0, 0, 0],]
    reverse(gamepanel)
    assert  gamepanel.gameTile == [[0, 0, 0, 0], [8, 4, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 4, 8], [0, 0, 0, 0],]
    reverse(gamepanel)
    assert  gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [8, 4, 2, 2], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 4, 8],]
    reverse(gamepanel)
    assert  gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [8, 4, 2, 2],]


def test_compress():
    gamepanel = Board()
    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    compress(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[2, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    compress(gamepanel)
    assert gamepanel.gameTile == [[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 2, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    compress(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [2, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 8, 0], [0, 0, 0, 0],]
    compress(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [2, 8, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, 2],]
    compress(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 0],]

    gamepanel.gameTile = [[2, 4, 8, 2], [8, 4, 2, 2], [2, 2, 2, 2], [4, 4, 8, 2],]
    assert not_full(gamepanel) == False


def test_transpose():
    gamepanel = Board()
    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    transpose(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[2, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 0], [8, 0, 0, 0],]
    transpose(gamepanel)
    assert gamepanel.gameTile == [[2, 2, 4, 8], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 2, 0, 0], [0, 2, 0, 0], [0, 4, 0, 0], [0, 8, 0, 0],]
    transpose(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [2, 2, 4, 8], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 2, 0], [0, 0, 2, 0], [0, 0, 4, 0], [0, 0, 8, 0],]
    transpose(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 4, 8], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 4], [0, 0, 0, 8],]
    transpose(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 4, 8],]


def test_merge():
    gamepanel = Board()
    gamepanel.gameTile = [[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    merge(gamepanel)
    assert gamepanel.gameTile == [[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    merge(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0],]
    merge(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0],]

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0],]
    merge(gamepanel)
    assert gamepanel.gameTile == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 0, 0],]

def test_not_full():
    gamepanel = Board()

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    assert not_full(gamepanel) == True

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0],]
    assert not_full(gamepanel) == True

    gamepanel.gameTile = [[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    assert not_full(gamepanel) == True

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0],]
    assert not_full(gamepanel) == True

    gamepanel.gameTile = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0],]
    assert not_full(gamepanel) == True


