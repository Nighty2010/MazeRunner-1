
import unittest
import sys
import os
# import pytest

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from SusannaKursAlgo2 import SusannaKursAlgo

mazealgo = SusannaKursAlgo()


class DimMazeTest(unittest.TestCase):

    def test_setdim(self):
        mazealgo.setDimCols(10)
        mazealgo.setDimRows(99)
        self.assertTrue(mazealgo.dimCols == 10)
        self.assertTrue(mazealgo.dimRows == 99)
        self.assertRaises(Exception, mazealgo.setDimRows, -10)
        self.assertRaises(Exception, mazealgo.setDimCols, -10)


class MazeLoadTest(unittest.TestCase):
    def test_loadmaze_fileload(self):
        self.assertTrue(mazealgo.loadMaze(os.path.realpath(
            os.path.dirname(__file__)) + "/../../../MazeExamples/maze1.txt"))
        self.assertFalse(mazealgo.loadMaze(os.path.realpath(
            os.path.dirname(__file__)) + "/../../../MazeExamples/maze9.txt"))

    def test_loadmaze_dimension(self):
        mazealgo.loadMaze(os.path.realpath(
            os.path.dirname(__file__)) + "/../../../MazeExamples/maze1.txt")
        self.assertTrue(mazealgo.dimRows == 6)
        self.assertTrue(mazealgo.dimCols == 5)

    def test_loadmaze_startpos(self):
        mazealgo.loadMaze(os.path.realpath(
            os.path.dirname(__file__)) + "/../../../MazeExamples/maze1.txt")
        self.assertTrue(mazealgo.startRow == 0)
        self.assertTrue(mazealgo.startCol == 4)

    def test_loadmaze_endpos(self):
        mazealgo.loadMaze(os.path.realpath(
            os.path.dirname(__file__)) + "/../../../MazeExamples/maze1.txt")
        self.assertTrue(mazealgo.endRow == 2)
        self.assertTrue(mazealgo.endCol == 4)

    def test_loadmaze_isingrid(self):
        mazealgo.loadMaze(os.path.realpath(
            os.path.dirname(__file__)) + "/../../../MazeExamples/maze1.txt")
        self.assertTrue(mazealgo.isInGrid(column=4, row=5))
        self.assertFalse(mazealgo.isInGrid(4, 5))
        self.assertTrue(mazealgo.isInGrid(row=4, column=4))

    def test_loadmaze_broken(self):
        self.assertFalse(mazealgo.loadMaze(os.path.realpath(
            os.path.dirname(__file__)) + "/../../../MazeExamples/maze1_broken.txt"))


class MazeNeighbours(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MazeNeighbours, self).__init__(*args, **kwargs)
        mazealgo.loadMaze(os.path.realpath(
            os.path.dirname(__file__)) + "/../../../MazeExamples/maze1.txt")

    def test_neighbour_up(self):
        lResultArr = mazealgo.getNeighbours(0, 0)
        self.assertTrue(len(lResultArr) == 2)

    def test_neighbours(self):
        lResultArr = mazealgo.getNeighbours(3, 2)
        self.assertTrue(len(lResultArr) == 3)
        print(lResultArr)
        self.assertTrue(lResultArr == [[2, 2], [4, 2], [3, 3]])

        lResultArr = mazealgo.getNeighbours(5, 4)
        self.assertTrue(len(lResultArr) == 2)
        self.assertTrue(lResultArr == [[4, 4], [5, 3]])
