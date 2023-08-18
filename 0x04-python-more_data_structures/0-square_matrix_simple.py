#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
      if len(matrix) != 0:
        sqr = []
        for row in matrix:
            new = []
            for pack in row:
                new.append(pack**2)
            sqr.append(new)
        return sqr
