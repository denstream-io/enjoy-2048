import random
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

class Board(Frame):
    def __init__(self):
        self.FOREGROUND_COLOR = {
            2: "#776e65",
            4: "#776e65",
            8: "#f9f6f2",
            16: "#f9f6f2",
            32: "#f9f6f2",
            64: "#f9f6f2",
            128: "#f9f6f2",
            256: "#f9f6f2",
            512: "#f9f6f2",
            1024: "#f9f6f2",
            2048: "#f9f6f2",
            4096: "#776e65",
            8192: "#f9f6f2",
            16384: "#776e65",
            32768: "#776e65",
            65536: "#f9f6f2",
        }

        self.BACKGROUND_COLOR = {
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e",
            4096: "#eee4da",
            8192: "#edc22e",
            16384: "#f2b179",
            32768: "#f59563",
            65536: "#f67c5f",
        }
        self.boardSize = 4

        self.moved = False
        self.merged = False
        self.compressed = False
        self.gameMatrix = []
        self.gameTile = [self.boardSize * [0] for _ in range(self.boardSize)]
        self.score = 0
        self.new_window = False

        self.root = Tk()
        self.root.title("2048 by denstream-io")

        self.windowStyle = ttk.Style()
        self.windowStyle.configure(
            "Grid.TFrame",
            background="#92877D",  # BBADAO
            boderwidth=5,
            relief="raised",
            width="500p",
            height="500p",
        )

        self.cellStyle = ttk.Style()
        self.cellStyle.configure(
            "Cell.TFrame",
            boderwidth=5,
        )

        self.labelStyle = ttk.Style()
        self.labelStyle.configure(
            "Label.TLabel",
            anchor="center",
        )

        self.scoreStyle = ttk.Style()
        self.scoreStyle.configure(
            "Score.TLabel",
            foreground="green"
        )
        self.var = StringVar()
        self.var.set(f"Your Score: {self.score}")
        self.gameScore = ttk.Label(self.root, textvariable= self.var, style="Score.TLabel")
        self.gameScore.grid()

        self.gameScore = ttk.Button(self.root, text="Quit", command=self.root.destroy)
        self.gameScore.grid()

        self.gameScore = ttk.Button(self.root, text="Restart", command=self.reset_game)
        self.gameScore.grid()

        self.gameWindow = ttk.Frame(self.root, style="Grid.TFrame")
        self.gameWindow.grid(sticky=(N, W, E, S))




        for i in range(int(self.boardSize)):
            labeled_row = []
            for j in range(int(self.boardSize)):
                self.gameCell = ttk.Frame(
                    self.gameWindow, relief="raised", style="Cell.TFrame"
                )
                self.gameCell.grid(column=i, row=j, sticky=(N, W, E, S))
                self.eachLabel = ttk.Label(
                    self.gameWindow, text="", style="Label.TLabel"
                )
                self.eachLabel.grid(column=i, row=j, sticky=(N, W, E, S))
                labeled_row.append(self.eachLabel)
            self.gameMatrix.append(labeled_row)


        for child in self.gameWindow.winfo_children():
            child.grid_configure(padx=5, pady=5, ipadx="25p", ipady="25p")

    def update_board(self):
        self.var.set(f"Your Score: {self.score}")
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.gameTile[i][j] == 0:
                    self.gameMatrix[i][j].configure(
                        text="", background="#9E948A"
                    )
                else:
                    self.gameMatrix[i][j].configure(
                        text=str(self.gameTile[i][j]),
                        background=self.BACKGROUND_COLOR[self.gameTile[i][j]],
                        foreground=self.FOREGROUND_COLOR[self.gameTile[i][j]],
                    )


    def reset_game(self) -> None:

        self.score = 0
        self.gameTile = [[0]*4 for _ in range(self.boardSize)]
        self.update_board()


def main(gamepanel):
    get_random(gamepanel)
    get_random(gamepanel)
    gamepanel.update_board()


    gamepanel.root.bind_all("<Key>", lambda event, gamepanel=gamepanel: control_game(event, gamepanel))
    gamepanel.root.focus_set()
    gamepanel.root.mainloop()



def control_game(event, gamepanel=None):


    key_pressed = event.keysym

    if key_pressed == "Up": # Up
        compress(gamepanel)
        merge(gamepanel)
        gamepanel.moved = gamepanel.merged or gamepanel.compressed
        compress(gamepanel)
        # transpose(gamepanel)
        # compress(gamepanel)
        # merge(gamepanel)
        # gamepanel.moved = gamepanel.merged or gamepanel.compressed
        # compress(gamepanel)
        # transpose(gamepanel)
    elif key_pressed == "Down": #Down
        reverse(gamepanel)
        compress(gamepanel)
        merge(gamepanel)
        gamepanel.moved = gamepanel.merged or gamepanel.compressed
        compress(gamepanel)
        reverse(gamepanel)

        # transpose(gamepanel)
        # reverse(gamepanel)
        # compress(gamepanel)
        # merge(gamepanel)
        # gamepanel.moved = gamepanel.merged or gamepanel.compressed
        # compress(gamepanel)
        # reverse(gamepanel)
        # transpose(gamepanel)
    elif key_pressed == "Left": #Left
        # compress(gamepanel)
        # merge(gamepanel)
        # gamepanel.moved = gamepanel.merged or gamepanel.compressed
        # compress(gamepanel)
        transpose(gamepanel)
        compress(gamepanel)
        merge(gamepanel)
        gamepanel.moved = gamepanel.merged or gamepanel.compressed
        compress(gamepanel)
        transpose(gamepanel)
    elif key_pressed == "Right": # Right
        # reverse(gamepanel)
        # compress(gamepanel)
        # merge(gamepanel)
        # gamepanel.moved = gamepanel.merged or gamepanel.compressed
        # compress(gamepanel)
        # reverse(gamepanel)

        transpose(gamepanel)
        reverse(gamepanel)
        compress(gamepanel)
        merge(gamepanel)
        gamepanel.moved = gamepanel.merged or gamepanel.compressed
        compress(gamepanel)
        reverse(gamepanel)
        transpose(gamepanel)

    if any(max(row) == 2048 for row in gamepanel.gameTile):
            messagebox.showinfo("You won!")
    elif not (not_full(gamepanel) or is_mergeable(gamepanel)):
            messagebox.showwarning("You Lost!")

    if gamepanel.moved:
            get_random(gamepanel)
    gamepanel.update_board()


def get_random(gamepanel):

    if not not_full(gamepanel):
        return

    tiles = []
    for i in range(gamepanel.boardSize):
        for j in range(gamepanel.boardSize):
            if gamepanel.gameTile[i][j] == 0:
                tiles.append((i, j))

    random_tile = random.choice(tiles)
    x = random_tile[0]
    y = random_tile[1]

    gamepanel.gameTile[x][y] = random.choices([2, 4, 8], weights=[60, 37, 3])[0]

def is_mergeable(gamepanel) -> bool:
    """
    Checks if tiles are mergeble

    :return: True if tile is mergeable
    :rtype: bool
    """
    for i in range(gamepanel.boardSize - 1):
        for j in range(gamepanel.boardSize - 1):
            if (
                gamepanel.gameTile[i][j] == gamepanel.gameTile[i + 1][j]
                or gamepanel.gameTile[i][j] == gamepanel.gameTile[i][j + 1]
            ):
                return True
    return False

def new_board(gamepanel) -> list:
    """
    Bulids a new_board game board

    :return: A list of lists
    :raise: AssertionError if size N is float or < 1
    :rtype: list
    """

    assert  gamepanel.boardSize >= 1, "Invalid Board Dimension"
    assert type(gamepanel.boardSize) == int, "N must be an integer"
    return list([0] * gamepanel.boardSize for _ in range(gamepanel.boardSize))


def reverse(gamepanel) -> None:
    """
    Reverses each row in BOARD
    :return: None
    :rtype: NoneType
    """
    reversedTile = new_board(gamepanel)
    for i in range(gamepanel.boardSize):
        for j in range(gamepanel.boardSize):
            reversedTile[i][j] = gamepanel.gameTile[i][gamepanel.boardSize - (1 + j)] # Same row flip column
    gamepanel.gameTile = reversedTile

def transpose(gamepanel) -> None:
    """
    Transposes each row in BOARD

    :return: None
    :rtype: NoneType
    """

    transposedTile = [[0]*4 for _ in range(4)]
    for i in range(gamepanel.boardSize):
        for j in range(gamepanel.boardSize):
            transposedTile[j][i] = gamepanel.gameTile[i][j]
    gamepanel.gameTile = transposedTile

def merge(gamepanel) -> None:
    """
    Merges tiles in row if equal

    :return: None
    :rtype: NoneType
    """
    gamepanel.merged = True

    for i in range(gamepanel.boardSize):
        for j in range(gamepanel.boardSize - 1):
            if gamepanel.gameTile[i][j] != 0 and gamepanel.gameTile[i][j] == gamepanel.gameTile[i][j + 1]:
                gamepanel.gameTile[i][j] *= 2
                gamepanel.gameTile[i][j + 1] = 0
                gamepanel.score += gamepanel.gameTile[i][j]
                gamepanel.merged = True

def not_full(gamepanel):
    """
        Returns True if full else False
    """

    for i in range(gamepanel.boardSize):
        for j in range(gamepanel.boardSize):
            if (gamepanel.gameTile[i][j] == 0):
                return True
    return False

def compress(gamepanel) -> None:
    """
    Compresses all tiles in BOARD row to left

    :return: None
    :rtype: NoneType
    """
    gamepanel.compressed = False

    compressedTile = [[0]*4 for _ in range(4)]
    for i in range(gamepanel.boardSize):
        compressed_loc = 0
        for j in range(gamepanel.boardSize):
            if gamepanel.gameTile[i][j] != 0:
                # Move non-zero element in original matrix to new_board matrix
                # from left to right, top to bottom
                compressedTile[i][compressed_loc] = gamepanel.gameTile[i][j]
                if compressed_loc != j:
                    gamepanel.compressed = True
                compressed_loc += 1

    gamepanel.gameTile = compressedTile

if __name__ == '__main__':
    gamepanel = Board()
    main(gamepanel)