import numpy as np
import re
import sys

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = set(x)
check_it = [x, 1, 3, x, x, x, 8, 2, x], \
  [x, 5, x, x, x, 1, x, x, x], \
  [x, x, x, x, 7, x, 5, x, x], \
  [x, x, x, x, 5, 7, x, 9, 6], \
  [x, 4, x, 3, x, x, x, x, 8], \
  [x, x, x, 2, 8, x, 7, x, 3], \
  [x, 2, 9, x, 6, 3, x, x, x], \
  [3, x, 8, x, x, x, x, x, x], \
  [x, 6, 1, 9, 2, x, x, x, 4]
s = np.array(check_it)
square1 = s[0][:3], s[1][:3], s[2][:3]
square2 = s[0][3:6], s[1][3:6], s[2][3:6]
square3 = s[0][6:9], s[1][6:9], s[2][6:9]
square4 = s[3][:3], s[4][:3], s[5][:3]
square5 = s[3][3:6], s[4][3:6], s[5][3:6]
square6 = s[3][6:9], s[4][6:9], s[5][6:9]
square7 = s[6][:3], s[7][:3], s[8][:3]
square8 = s[6][3:6], s[7][3:6], s[8][3:6]
square9 = s[6][6:9], s[7][6:9], s[8][6:9]


def square_finder(row, col):  # simply finds the square of a given row and col
  if row < 3:
    if col < 3:
      return "square1"
    if 3 <= col < 6:
      return "square2"
    else:
      return "square3"
  if 3 <= row < 6:
    if col < 3:
      return "square4"
    if 3 <= col < 6:
      return "square5"
    else:
      return "square6"
  else:
    if col < 3:
      return "square7"
    if 3 <= col < 6:
      return "square8"
    else:
      return "square9"


def square_print(row, col):  # executes square_finder and prints out only the ints in the square as a set
  square_name = square_finder(row, col)
  square = []
  num_in_square = []
  for each in eval(square_name):
    for m in each:
      square.append(m)
  for num in square:
    if type(num) == int:
      num_in_square.append(num)
  num_in_square = set(num_in_square)
  return num_in_square


def set_single_check(row, col):  # looks if the current square has a set length of 1
  single_check = s[row, col]  # if so sets it to that number
  if type(single_check) == set:
    if len(single_check) == 1:
      for the_num in single_check:
        s[row, col] = the_num


def note_updater():  # fills each square with its possibilities
  row_counter = -1
  int_counter = 0
  while row_counter != 8:  # adds 1 to row until 8
    row_counter += 1
    col_counter = -1
    for each in s[row_counter]:
      col_counter += 1
      square_ints = square_print(row=row_counter, col=col_counter)
      if type(each) == int:
        int_counter += 1
      elif type(each) == set:
        deduct = []
        for a in s[row_counter]:
          if type(a) == int:
            deduct.append(a)
        for y in s[:, col_counter]:
          if type(y) == int:
            deduct.append(y)
        deduct = set(deduct)
        s[row_counter, col_counter] = each - deduct - square_ints
  if int_counter == 81:
    print(s)
    sys.exit()

  else:
    return False


def row_checker(row, col):
  repeat_check = 0
  check_these = s[row, col]
  for each_num in check_these:
    counter = -1  # does the following for each number in the given square
    for each in s[row]:  # does the following for each of the ones in row
      counter += 1
      if type(each) == int:  # if type is int skip if is the square we are checking skip
        continue
      elif counter == col:
        continue
      else:
        if re.search(str(each_num), str(each)) is not None:
          repeat_check += 1
    if repeat_check == 0:
      s[row, col] = each_num
    else:
      repeat_check = 0


def column_checker(row, col):
  repeat_check = 0
  check_these = s[row, col]
  for each_num in check_these:  # does the following for each number in the given square
    counter = -1
    for each in s[:, col]:  # does the following for each of the ones in column
      counter += 1
      if type(each) == int:  # if type is int skip if is the square we are checking skip
        continue
      elif counter == row:
        continue
      else:
        if re.search(str(each_num), str(each)) is not None:
          repeat_check += 1
    if repeat_check == 0:
      s[row, col] = each_num
    else:
      repeat_check = 0


def square_checker(row, col):
  repeat_check = 0  # finds the square,evaluates, temp sets the square to 0
  the_square = eval(square_finder(row, col))  # checks each num in notes and if there is no repeats
  nums_to_check = s[row, col]  # sets that number to the designated square
  s[row, col] = 0  # if no singles, sets the square back to original value
  for each_num in nums_to_check:
    if s[row, col] != 0:
      continue
    else:
      for each_square in the_square:
        for each in each_square:
          if type(each) == int:
            continue
          if type(each) == set:
            if re.search(str(each_num), str(each_square)) is not None:
              repeat_check += 1
      if repeat_check == 0:
        s[row, col] = each_num
      else:
        repeat_check = 0
  if s[row, col] == 0:
    s[row, col] = nums_to_check


def recursive():
  while note_updater() is False:
    r = -1
    while r != 8:
      r += 1
      c = -1
      while c != 8:
        c += 1
        if type(s[r, c]) == int:
          continue
        if type(s[r, c]) == set:
          note_updater()
          row_checker(row=r, col=c)
          if type(s[r, c]) == set:
            column_checker(row=r, col=c)
            if type(s[r, c]) == set:
              square_checker(row=r, col=c)
              if type(s[r, c]) == set:
                set_single_check(row=r, col=c)
      if r == 8:
        recursive()


recursive()
