from typing import List

# Solution 3 - 100% runtime and 94.33% runtime
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                box_index = (row//3) * 3 + col//3
                if value in rows[row] or value in cols[col] or value in boxes[box_index]:
                    return False
                rows[row].add(value)
                cols[col].add(value)
                boxes[box_index].add(value)
        return True
# Time complexity for all solutions O(1) in this specific case. O(n^2) for a generic sudoku board
# Space complexity for all solution O(1) in this specific case. O(n^2) for a generic sudoku board

# # Solution 2 - 100% runtime 100% memory
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = {i:set() for i in range(9)}
#         cols = {i:set() for i in range(9)}
#         boxes = {i:set() for i in range(9)}
#         for row in range(9):
#             for col in range(9):
#                 value = board[row][col]
#                 if value == ".":
#                     continue
#                 box_index = (row//3) * 3 + col//3
#                 if value in rows[row] or value in cols[col] or value in boxes[box_index]:
#                     return False
#                 rows[row].add(value)
#                 cols[col].add(value)
#                 boxes[box_index].add(value)
#         return True

# # Solution 1 - 100% runtime and 94.33% memory
# class Solution:
#     def isValidSudoku(board: List[List[str]]) -> bool:
#         unique_elements_rows = {}
#         unique_elements_cols = {}
#         unique_elements_boxes = {}
#         for i, row in enumerate(board):
#             unique_elements_rows.setdefault(i, [])
#             for j in range(len(row)):
#                 unique_elements_cols.setdefault(j, [])
#                 box_index = (i // 3) * 3 + j // 3
#                 unique_elements_boxes.setdefault(box_index, [])
#                 if row[j] != ".":
#                     if row[j] not in unique_elements_rows[i]:
#                         unique_elements_rows[i].append(row[j])
#                     else:
#                         return False
#                     if row[j] not in unique_elements_cols[j]:
#                         unique_elements_cols[j].append(row[j])
#                     else:
#                         return False
#                     if row[j] not in unique_elements_boxes[box_index]:
#                         unique_elements_boxes[box_index].append(row[j])
#                     else:
#                         return False
#         print(f"Rows:\n{unique_elements_rows}\nCols:\n{unique_elements_cols}\nBoxes:\n{unique_elements_boxes}")
#         return True

# board =[["1","2",".",".","3",".",".",".","."],
#         ["4",".",".","5",".",".",".",".","."],
#          [".","9","8",".",".",".",".",".","3"],
#          ["5",".",".",".","6",".",".",".","4"],
#          [".",".",".","8",".","3",".",".","5"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".",".",".",".",".",".","2",".","."],
#          [".",".",".","4","1","9",".",".","8"],
#          [".",".",".",".","8",".",".","7","9"]]
#
# board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
#              ["4", ".", ".", "5", ".", ".", ".", ".", "."],
#              [".", "9", "1", ".", ".", ".", ".", ".", "3"],
#              ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
#              [".", ".", ".", "8", ".", "3", ".", ".", "5"],
#              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#              [".", ".", ".", ".", ".", ".", "2", ".", "."],
#              [".", ".", ".", "4", "1", "9", ".", ".", "8"],
#              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
#
# print(isValidSudoku(board))