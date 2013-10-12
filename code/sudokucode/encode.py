import sys
import utils


if len(sys.argv) == 2:
    sudoku_coder = utils.SudokuCoder()
    print sudoku_coder.encode(sys.argv[1])
else:
    print "Usage: python encode.py [plaintext]"
