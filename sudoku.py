import numpy as np


def validate_board(board: np.ndarray) -> bool:
    """Verifies a 9x9 square of numbers is a valid Sudoku board: 1 to 9 in each row,
      column, and the nine 3x3 sub-grids.

    Parameters
    ----------
        board: np.NDArray
        9*9 array representing the sudoku board
    Returns
    -------
    is_valid: bool
        True if valid

    Raises
    ------
    ValueError
        if the given board is not valid.
    """
    valid_nums = np.arange(9) + 1

    if not np.array_equal(np.sort(np.unique(board)), valid_nums):
        raise ValueError("The Board should only contain numbers from 1 to 9!")

    if board.shape != (9, 9):
        return ValueError("The board should be 9 by 9!")

    for idx in range(board.shape[0]):
        if not np.array_equal(np.sort(board[idx]), valid_nums):
            print(f"{idx+1} row is invalid!")
            return False
        if not np.array_equal(np.sort(board[:, idx]), valid_nums):
            print(f"{idx+1} col is invalid!")
            return False

    for i in (0, 3, 6):
        for j in (0, 3, 6):
            if not np.array_equal(np.sort(np.ravel(board[i : i + 3, j : j + 3])), valid_nums):
                print("Invalid squares!")
                return False

    return True
