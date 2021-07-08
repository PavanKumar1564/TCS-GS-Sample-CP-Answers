# Problem Name is &&& Lowest Price &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) Run this code in the REPL to observe its behaviour. The execution entry point is main. 2) Consider adding some additional tests in do_tests_pass(). 3) Implement get_lowest_prices() correctly. 4) If time permits, some possible follow-ups. Question: A popular online retailer allows vendors to specify different prices in advance for the same item throughout the day. we now need to design an algorithm that helps identify the lowest price for the item at any point of the day. Assumptions: 1) For the algorithm, assume all vendors are selling the same product and there is only one product being sold. Given a list that has vendor information - ( start_time, end_time, price ) of the deal, return a sorted list with different possible intervals and the least price of the product during the interval. 
2) The interval is inclusive of start and end time. 
3) All the 3 values passed by the vendor are integers.
"""
from collections import namedtuple 
Interval = namedtuple( "Interval", "start_time end_time price" ) 
# Class to store node level data in the binary search tree
class Node( object ):
    def __init__( self, data ):
        self.data = data
        self.left = self.right = None # left and right pointers 
# Binary Search Tree implementation
class BinarySearchTree( object ):
    def __init__( self ):
        self._root = None
        self._sorted_intervals = []

    # Actual function to insert node into the tree
    def _insert( self, node, interval ):
        # Excess to the left - trim and push
        if interval.start_time < node.data.start_time:
            new_interval = Interval( interval.start_time, min( interval.end_time, node.data.start_time ), interval.price) 

            if node.left:
                self._insert( node.left, new_interval )
            else:
                node.left = Node( new_interval )

        # Excess to the right - trim and push
        if interval.end_time > node.data.end_time:
            new_interval = Interval( max( interval.start_time, node.data.end_time ), interval. end_time, interval.price )
            if node.right:
                self._insert( node.right, new_interval )
            else:
                node.right = Node( new_interval ) 
    # Actual recursive function to do inorder traversal
    def _inorder( self, node ):
        if not node:
            return()

        if node.left:
            self._inorder( node.left )
        self._sorted_intervals.append( node.data )
        if node.right:
            self._inorder( node.right )

    # Public function to insert node into the tree
    def add_to_node( self, interval ):
        if not self._root:
            self._root = Node( interval )
        else:
            self._insert( self._root, interval )

    # Public function to return all non-overlapping intervals (sorted on start )
    def start_inorder( self ):
        self._sorted_intervals = []
        self._inorder( self._root )
        return( self._sorted_intervals )

def get_lowest_prices( input_intervals ):
    if not input_intervals:
        raise Exception( "input_intervals has e elements" )
    for each_interval in input_intervals:
        if not each_interval:
            raise Exception( "input_intervals has a Null element" )
        if each_interval.start_time >= each_interval.end_time:
            raise Exception( "start_time greater than or equal to end_time for an interval" )
        if each_interval.start_time < 0 or each_interval.end_time < 0 or each_interval.price < 0:
            raise Exception( "vendor information has negative values" )

    input_intervals = sorted( input_intervals, key = lambda x: x.price )
    bst = BinarySearchTree()
    for each_interval in input_intervals:
        bst.add_to_node( each_interval )
    print( bst.start_inorder() )
    return( bst.start_inorder() )

"""
Prints Success if all tests pass. Otherwise
TODO: implement some tests. We've included a trivial boilerplate
Additional Test Cases: returns Failure.
    Input : ( 1, 20 13 ), ( 7, 10, 8 ), ( 3, 8, 15 ), ( 1, 5, 20 )
    Output: ( 1, 7, 13 ), ( 7, 10, 8 ), ( 10, 20, 13 )

    Input : ( 7, 10, 8 ), ( 3, 8, 15 ), ( 1, 5, 20 ), ( 1, 20, 4 )
    Output: ( 1, 20, 4 )

    Input : ( 3, 6, 2 ), ( 1, 9, 3 ), ( 5, 8, 1 )
    Output: ( 1, 3, 3 ), ( 3, 5, 2 ), ( 5, 8, 1 ), ( 8, 9, 3 )
"""
def do_tests_pass():
    input_intervals = [ Interval( 1, 5, 20 ), Interval( 3, 8, 15 ), Interval( 7, 10, 8 ) ]
    expected_output = [ Interval( 1, 3, 20 ), Interval( 3, 7, 15 ), Interval( 7, 10, 8 ) ]
    output_intervals = get_lowest_prices( input_intervals )
    if output_intervals == expected_output:
        print( "All tests passed" )
    else:
        print( "Tests failed" )

if __name__ == "__main__":
    do_tests_pass() 
