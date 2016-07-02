# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count = 0
    for w in words:
        if len(w) >= 2:
            if w[0] == w[len(w)-1]:
                count += 1
    print(count)
    
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    raise NotImplementedError


def front_x(words):
    words.sort()
    # xwords is a list of words in input starting with 'x'
    xwords = []
    for w in words:
        if w[0] == 'x':
            xwords.append(w)
    xwords.sort()

    # xsort is the output list
    xsort = []
    xsort.extend(xwords)
    for word in words:
        if word[0] != 'x':
            xsort.append(word)

    print(xsort)
    
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    raise NotImplementedError


def sort_last(tuples):
    print(sorted(tuples, key=lambda x: x[len(x)-1]))

    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    raise NotImplementedError


def remove_adjacent(nums):
    if len(nums) > 0:
        simple = [nums[0]]
        prev = nums[0]
        for n in nums:
            if n != prev:
                simple.append(n)
            prev = n

        print(simple)
    else:
        print(nums)
        
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    raise NotImplementedError


def linear_merge(list1, list2):
    merged = []
    l1, l2 = 0, 0
    len1, len2 = len(list1), len(list2)

    for i in range(len1+len2):
        if l2 == len2:
            merged.extend(list1[l1:len1])
            break
        if l1 == len1:
            merged.extend(list2[l2:len2])
            break
        if list1[l1]< list2[l2]:
            merged.append(list1[l1])
            l1+=1
        else:
            merged.append(list2[l2])
            l2+=1

    print(merged)
    
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    raise NotImplementedError
