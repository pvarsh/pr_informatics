# Principles of Urban Informatics
# Assignment 4
# tests (with py.test) for all three problems
#
# Usage:
#    py.test test_assignment_4.py   # if all the programs run correctly you won't see much output
#                                   # if one run of a program returns incorrect values the whole output of that run will be printed
#
# What you need to use this:
#    just the py.test library
#    http://pytest.org/latest/
#
# by brigitte.jellinek@nyu.edu
#


#
# tests like these are used in professional software development
# to make sure that the program as a whole does what it's supposed to do,
# and to make sure that single methods or classes to what they're supposed to do
#


#
# each test case is a method starting with test_
# in each test case you can use all of python to prepare
# data for the test.
# then you run the method you want to test, and
# write an ASSERTION about what the result of the method should be
#


#
# this tests the built-in function len,
# which doesnt' make much sense
# but shows off how to write a test case:
def test_len():
  list = [1,2,3,2,1]
  assert len(list) == 5


# ==================================================
# Test cases for  problem 1

from problem1 import solveOnlyLists, solveDict, solveSorted

def test_solveOnlyLists():
  list = [1,2,3,2,1]
  assert set(list) == set( solveOnlyLists( list ) )

def test_solveDict():
  list = [1,2,3,2,1]
  assert set(list) == set( solveOnlyLists( list ) )

def test_solveSorted():
  list = [1,2,3,2,1]
  assert set(list) == set( solveOnlyLists( list ) )

test_solveOnlyLists()
test_solveDict()
test_solveSorted()


# ==================================================
# Test cases for  problem 2

from problem2 import searchGreaterNotSorted, searchGreaterSorted, searchGreaterBinSearch, searchInRange

def test_searchGreaterNotSorted():
  assert 4 == searchGreaterNotSorted( [5,4,1,3,5], 2) 
  assert 0 == searchGreaterNotSorted( [2,4,2,0,-3,5], 5) 
  assert 1 == searchGreaterNotSorted( [1,0,2,-1,2,10], 2) 

def test_searchGreaterSorted():
  assert 4 == searchGreaterSorted( [1,2,3,4,5,5], 2) 
  assert 0 == searchGreaterSorted( [-3,0,2,4,5], 5) 
  assert 1 == searchGreaterSorted( [-1,0,1,2,2,10], 2) 

def test_searchGreaterBinSearch():
  assert 0 == searchGreaterBinSearch( [], 2) 
  assert 1 == searchGreaterBinSearch( [1], 0)
  assert 0 == searchGreaterBinSearch( [1], 1)
  assert 0 == searchGreaterBinSearch( [1], 2)
  assert 0 == searchGreaterBinSearch( [1,2], 2) 
  assert 1 == searchGreaterBinSearch( [1,2], 1) 
  assert 2 == searchGreaterBinSearch( [1,2], 0) 
  assert 0 == searchGreaterBinSearch( [1,2,3], 3) 
  assert 1 == searchGreaterBinSearch( [1,2,3], 2) 
  assert 2 == searchGreaterBinSearch( [1,2,3], 1) 
  assert 3 == searchGreaterBinSearch( [1,2,3], 0) 
  assert 3 == searchGreaterBinSearch( [1,3,4,5,5], 3) 
  assert 5 == searchGreaterBinSearch( [-3,0,2,2,4,5], -1)
  assert 4 == searchGreaterBinSearch( [1,2,3,4,5,5], 2) 
  assert 0 == searchGreaterBinSearch( [-3,0,2,4,5], 5) 
  assert 1 == searchGreaterBinSearch( [-1,0,1,2,2,10], 2) 

def test_searchInRange():
  # NO LONGER VALID! CHANGED WITH VERSION 2 of ASSIGNMENT
  # assert 0 == searchInRange( [1,3,4,5,5],         3,  3) 
  assert 0 == searchInRange( [1,3,4,5,5],         1,  2) 
  # NO LONGER VALID! CHANGED WITH VERSION 2 of ASSIGNMENT
  #assert 4 == searchInRange( [-3,0,2,2,4,5],     -1,  5)
  assert 5 == searchInRange( [-3,0,2,2,4,5],     -1,  5) 
  assert 2 == searchInRange( [-1,0,1,1,2,10,10],  2, 11) 

test_searchGreaterNotSorted()
test_searchGreaterSorted()
test_searchGreaterBinSearch()
test_searchInRange()


# ==================================================
# Test cases for  problem 3
  
from problem3 import buildNaive,queryNaive,buildOneDim,queryOneDim,buildTwoDim,queryTwoDim
  
#  def buildNaive(points,n):
#  def queryNaive(x0, y0, x1, y1):
def test_naive():
  buildNaive( [[0.5, 0.3], [0.1, 0.1]], 0 )
  assert 2 == queryNaive( 0,0,     1,1 )
  assert 1 == queryNaive( 0,0,     0.2,0.2 )
  assert 0 == queryNaive( 0,0,     0.04,0.03 )

#  def buildOneDim(points,n):
#  def queryOneDim(x0, y0, x1, y1):
def test_OneDim():
  buildOneDim( [[0.5,0.5]], 2 )
  assert 1 == queryOneDim( 0,0,     1,1 )
  assert 1 == queryOneDim( 0,0,     0.5,0.5 )
  assert 0 == queryOneDim( 0,0,     0.1,0.1 )
  assert 0 == queryOneDim( 0,0,     0,0 )
  buildOneDim( [[0.5, 0.3], [0.1, 0.1]], 2 )
  assert 2 == queryOneDim( 0,0,     1,1 )
  assert 1 == queryOneDim( 0,0,     0.2,0.2 )
  assert 0 == queryOneDim( 0,0,     0.05,1 )
  assert 0 == queryOneDim( 0,0,     1,0.05 )

#  def buildTwoDim(points,n):
#  def queryTwoDim(x0, y0, x1, y1):
def test_TwoDim():
  buildTwoDim( [[0.5,0.5]], 2 )
  assert 1 == queryTwoDim( 0,0,     1,1 )
  assert 1 == queryTwoDim( 0,0,     0.5,0.5 )
  assert 0 == queryTwoDim( 0,0,     0.1,0.1 )
  assert 0 == queryTwoDim( 0,0,     0,0 )
  buildTwoDim( [[0.5, 0.3], [0.1, 0.1]], 2 )
  assert 2 == queryTwoDim( 0,0,     1,1 )
  assert 1 == queryTwoDim( 0,0,     0.2,0.2 )
  assert 0 == queryTwoDim( 0,0,     0.05,1 )
  assert 0 == queryTwoDim( 0,0,     1,0.05 )
  buildTwoDim( [[0,0],[1,0],[0,1],[1,1],[0.5,0.5],[0.51,0.5],[0.5,0.51]], 2 )
  assert 7 == queryTwoDim( 0,0,     1,1 )
  assert 3 == queryTwoDim( 0.1,0.1, 0.9,0.9 )
  assert 0 == queryTwoDim( 0.2,0,   0.4,1   )
  assert 0 == queryTwoDim( 0,0.2,   1,0.4   )

# ==================================================
test_naive()
test_OneDim()
test_TwoDim()
