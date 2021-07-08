#Problem Name is &&& Sort Segments &&& PLEASE DO NOT REMOVE THIS LINE. 
"""
Instructions to candidate.
1) RUn this code in the REPL to observe its behaviour.
2) Consider adding some additional tests in TestSortSegments.
3) Implement sort_segments() correctly.
4) If time permits, some possible follow-ups. 
"""
import unittest
from collections import deque
from random import shuffle

def sort_segments(segments):
    """
        Given a jumbled collection of segments, each of which is represented as a tuple (start_point, end_point), this function sorts the segments to make a continuous path. 
        A few assumptions you can make:
        1. Each particular segment goes in one direction only, i.e.: if you see (1, 2), you will not see (2, 1). 2. Each starting point only have one way to the end point, i.e.: if you see (6, 5), you will not see (6, 10), (6, 3), etc. 
        >>> jumbled_segments = [(4, 5), (9, 4), (5, 1), (11, 9)]
        >>> continuous_path = sort_segments(jumbled_segments)
        >>> print(continuous_path) [(11, 9), (9, 4), (4, 5), (5, 1)] 
        Args:
            segments: collection of segments, each represented by a tuple (m, n).
        Returns:
            The sorted segments such that they form a continuous path. 
        Raises:
            ValueError: if there is no way to create one continuous path from all . . . 
    """
    # naive solution - will fail the complexity test before 10000 segments
    #if not segments:
    #   return []
    #
    # # make defensive shallow copy of the list
    # copied_segments = list(segments)
    #
    # sorted_segments = deque()
    # sorted_segments.append(copied_segments.pop(0))
    #
    # while len(copied_segments):
    #   seg_size = len(copied_segments)
    #   for i in range(seg_size - 1, -1, -1):
    #       start_point = sorted_segments[q]
    #       end_point = sorted_segments[4]
    #       segment = copied_segments[i]
    #       if start_point[0] == segment[1]:
    #           sorted_segments. appendleft(segment)
    #           del copied_segments[i]
    #       elif end_point[1] == segment[0]:
    #           sorted_segments.append(segment)
    #           del copied_segments[i]
    #       if seg_size == len(copied_segments):
    #           raise ValueError("Could not use all segments to form a continuous path")
    #
    # return list(sorted_segments)
    # much faster solution - can pass complexity test with 1 million segments
    if not segments:
        return []
    start_dict = {segment[0]: segment for segment in segments}
    end_dict = {segment[1]: segment for segment in segments}
    sorted_segments = deque()
    segment = segments[0]
    sorted_segments.append(segment)
    start_point = segment[0]
    end_point = segment[1]

    while True:
        next_segment = start_dict.get(end_point)
        if next_segment:
            sorted_segments.append(next_segment)
        prev_segment = end_dict.get(start_point)
        if prev_segment:
            sorted_segments.appendleft(prev_segment)
        if not next_segment and not prev_segment:
            break
        start_point = sorted_segments[0][0]
        end_point = sorted_segments[-1][1]

    if len(segments) != len(sorted_segments):
        raise ValueError("Could not use all segments to form a continuous path")
    return list(sorted_segments)

def generate_random_segments(n):
    points = list(range(n + 1))
    shuffle(points)
    segments = [pair for pair in zip(points[:-1], points[1:])]
    continuous_segments = list(segments)
    shuffle(segments)
    return continuous_segments, segments

class Testsort5egments(unittest.TestCase):
    def test_basic_sort(self):
        jumbled_segments = [(4, 5), (9, 4), (5, 1), (11, 9)]
        continuous_path = sort_segments(jumbled_segments)
        self.assertEqual(continuous_path, [(11, 9), (9, 4), (4, 5), (5, 1)])

    def test_sort_complexity(self):
        from time import process_time
        continuous_segs, jumbled_segments = generate_random_segments(1000000)
        start = process_time()
        sorted_segs = sort_segments(jumbled_segments)
        sort_time = process_time() - start
        self.assertEqual(continuous_segs, sorted_segs)
        # without CoderPad support for timeout, we have to resort to
        # picking a timeout value that probably will be enough for
        # a fast algorithm, but not too large that a slow algorithm
        # can complete anyway within the time limit
        self.assertLessEqual(sort_time, 2)

    def test_empty(self):
        empty_segments = []
        continuous_path = sort_segments(empty_segments)
        self. assertEqual(continuous_path, [])

    def test_none(self):
        continuous_path = sort_segments(None)
        self.assertEqual(continuous_path, [])

    def test_missing_segment(self):
        missing_segments = [(1, 2), (2, 3), (4, 5), (5, 6)]
        self.assertRaises(ValueError, sort_segments, missing_segments)

    def test_duplicate(self):
        duplicate_segments = [(1, 2), (2, 3), (1, 2)]
        self.assertRaises(ValueError, sort_segments, duplicate_segments)

unittest.main(exit=False)