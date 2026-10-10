from board import COLS


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        # 1. Only legal columns are candidates (a column is legal if its top cell is empty).
        legal = [c for c in range(COLS) if board.grid[0][c] == "."]
        if not legal:
            return None

        # 2. Take an immediate win if one exists.
        for c in legal:
            if self._wins_if_dropped(board, c, me):
                return c

        # 3. Otherwise block the column where the opponent would win next move.
        for c in legal:
            if self._wins_if_dropped(board, c, opponent):
                return c

        # 4. Fallback: prefer the centre column, then the nearest ones.
        return min(legal, key=lambda c: abs(c - COLS // 2))

    def _wins_if_dropped(self, board, col, token):
        """Test a move by placing it temporarily and always undoing it."""
        row = board.drop(col, token)
        if row is None:
            return False
        try:
            return board.winner(token)
        finally:
            board.grid[row][col] = "."