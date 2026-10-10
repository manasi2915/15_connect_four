from board import Board, COLS
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")
        while True:
            self.board.print()
            if self.turn == "X":
                try:
                    raw = input("Column (1-7), or q: ").strip().lower()
                except (EOFError, KeyboardInterrupt):
                    print("\nGame ended.")
                    return
                if raw == "q":
                    print("Game ended.")
                    return
                try:
                    col = int(raw) - 1
                except ValueError:
                    print("Enter a column number from 1 to 7, or q to quit.")
                    continue
                if not 0 <= col < COLS:
                    print("Column must be between 1 and 7.")
                    continue
                if self.board.drop(col, self.turn) is None:
                    print("That column is full. Choose another.")
                    continue
            else:
                col = self.ai.choose_column(self.board)
                if col is None:
                    self.board.print()
                    print("O has no legal move. Draw.")
                    return
                if self.board.drop(col, self.turn) is None:
                    print("O chose an illegal column. Game stopped.")
                    return

            label = "You" if self.turn == "X" else "AI"
            print(f"{label} ({self.turn}) played column {col + 1}.")

            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return
            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            self.turn = "O" if self.turn == "X" else "X"