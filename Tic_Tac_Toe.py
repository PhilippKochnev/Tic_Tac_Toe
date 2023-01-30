print("Игра крестики нолики на двоих")
print("__________")
board = [[" " for _ in range(3)] for _ in range(3)]

def draw_board():
  print("  0 1 2")
  for i, row in enumerate(board):
    print(i, " ".join(row))

def get_move(player):
  while True:
    col = input(f"{player}, Ведите столбец: ")
    row = input(f"{player}, Введите строку: ")
    if col.isdigit() and row.isdigit():
      col, row = int(col), int(row)
      if 0 <= col < 3 and 0 <= row < 3:
        if board[row][col] == " ":
          board[row][col] = player
          return
        else:
          print("Это место уже занято, попробуй еще раз.")
      else:
        print("Неверный ход, попробуй еще раз.")
    else:
      print("Неверный ход, попробуй еще раз.")

def has_winner():
  # проверить строки
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return True
  # проверить столбцы
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return True
  # проверить диагонали
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return True
  if board[2][0] == board[1][1] == board[0][2] and board[2][0] != " ":
    return True
  return False

def main():
  while True:
    draw_board()
    get_move("X")
    if has_winner():
      print("X Выйграл!")
      break
    draw_board()
    get_move("O")
    if has_winner():
      print("O выйграл!")
      break

main()
