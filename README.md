boring-stuff
==================

Boring Problems and Solutions :)

##Resources
- https://www.hackerrank.com
- https://leetcode.com/
- http://beust.com/algorithms.pdf
- http://www.codewars.com/dashboard
- http://www.geeksforgeeks.org/
- http://www.problee.com
- http://codingbat.com
- http://codepad.org
- http://crazyforcode.com
- http://www.cs.usfca.edu/~galles/visualization/Algorithms.html
- http://www.interviewbit.com
- http://www.hiredintech.com/app/

##Problems

###Sorting

1. Selection Sort - Implement and describe complexity
2. [Sort Array012] - Sort an array that contains only the integers 0, 1, and 2 in linear time. (e.g. [1,0,2,2,1] == [0,1,1,2,2]) 
3. Insertion Sort - Implement and describe complexity
4. Bubble Sort - Implement and describe complexity
5. Counting Sort - Implement and describe complexity
6. [Bucket Sort] - Implement and describe complexity
7. Merge Sort - Implement and describe complexity
8. Quick Sort - Implement and describe complexity
9. Heap Sort - Implement and describe complexity
10. Shell Sort - Implement and describe complexity

###Searching

1. Binary Search - Write method to return True if integer is in array
2. Binary Search w Pivot - An element in a sorted array can be found in O(log n) time via binary search. But suppose I rotate the sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. Devise a way to find an element in the rotated array in O(log n) time. If not found, return -1.
3. Bitonic Array - An array is bitonic if it is comprised of an increasing sequence of integers followed immediately by a decreasing sequence of integers. Write a program that, given a bitonic array of N distinct integer values, determines whether a given integer is in the array. Given 3LogN and 2LogN solutions.
4. Count Paths - Give a 2d array of size nxm with elements 1 and 0, find the number of paths from location [0,0] to [n-1,m-1] where a 1 indicates a open space and 0 indicates a closed space.
[1,0,0,1]
[1,1,1,0] = 4 paths
[0,1,1,0]
[0,1,1,1]
5. [Word Ladder] - Given a starting word, ending word and wordset. Find length of shortest transformation path from begin Word to end Word. 
Note: All words lowercase and alphabetical chars only. All words have same length. 
Rules: 1. change only 1 char at a time. 2. intermediate word must be in wordset.
ex. 
beginWord = "hit", endWord = "cog"
wordSet = ["hot","dot","dog","lot","log"] 
Example: Length of transformation: 5 (includes starting and ending words)
"hit" -> "hot" -> "dot" or "lot" -> "dog" or "log" -> "cog"

###Arrays

1. Sum3EqualsZero - Given array of integers, return true if any 3 elements in array sum to zero
2. [MaxContigSumArray] - Given array of integers, return max sum of contiguous elements in array. Write iterative and recursive solutions.
3. MaxSum3Array - Given array of integers, return max sum of 3 element subset
4. SetMatrixToZero - If an element in a M x N matrix is zero, set its entire row and column to zero.
5. FindOnesInMatrix - Given a 2D SORTED matrix, return the row index with the most ones
6. MajorityElement - given a array of integers, print out the element that appears more than n/2 times. Otherwise print not found.
7. [Platforms Train Station] - Given arrival and departure times of all trains that reach a railway station, find the minimum number of platforms required for the railway station so that no train waits. We are given two arrays which represent arrival and departure times of trains that stop. Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}, dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}, Output: 3. There are at-most three trains at a time (time between 11:00 to 11:20)
8. Max Incremental Subsequence - Given an array of unsorted integers, return the largest incremental subsequence (i.e. a sub array where elements are sorted in ascending order). Input: {0,1,2,3,4,2}. Output:{2,3,4}.
9. [Intersection Two Arrays] - Given two unsorted integer arrays, return a 3rd array with the intersection (distinct elements that appear in both arrays). Optimize for time and space complexity.
10. Find Peak - Implement a function taht returns a local max in an array in O(log(n))
Example: [1,5,2,3,4] Sol = 5 or 4. An element is a peak because it's neighbors are less than it.
11. [Sets all Equal] - WAF that takes an array of "sets" of String objects, and determines if they are equal. Each "set" in the input array is represented as an array of String objects, in 
no particular order, and possibly containing duplicates. Nevertheless, when determining whether two of these "sets" are equivalent, you should disregard order and duplicates. For example, the sets represented by these arrays are all equivalent: {"a", "b"}{"b", "a"}{"a", "b", "a"}
12. [Find Celebrity] - Party of n people. Only one person is known to everyone at the party. This "Celebrity" may or may not be in attendence. Celebrity knows no one at the party. Given an array of unique numbers and a function HaveAquaintance(A,B) which returns true if A knows B. Find the celebrity in a minimum number of questions. 
13. [Distinct Elements 2 Arrays] - Given 2 arrays, return array of numbers that exist in array 1 but not in array 2. Provide a solution in linear (2n is possible) time.
14. [Largest Connected Group] - Given 2D array of X/-, find the size of the largest connected group of X's
	x x - -
	x - - -
	x - - x
	- - x -
13. [Find Max Difference] - The maximum difference for a pair of elements in some array a is defined as the largest difference between any a[i] and a[j] where i < j and a[i] < a[j]. Return -1 if the array is in decending order or no such number exists. ex. a = {2, 3, 10, 2, 4, 8, 1} Output: 8. (10-2 = 8)



###Strings

1. IsAnagram - Return true if two strings are anagrams (each string contains the exact same alpha-numeric characters and the same count)
2. RemoveDuplicates - Given String of alpha-numeric characters, return String of distinct characters
3. ReverseString - Given String, return String with characters in reverse order
4. ReplaceSpaces - Given String, replace all spaces with HTML '%20'
5. IsRotation - Return true if str2 is rotation of str1
6. ReverseStringInplace - Reverses a string inplace
7. [FindFirstUniqueChar] - Return the first non-repeated character in a string. If not found, return null. Assume the string is NOT sorted. 
8. ReverseWords - Given a sentence, return the sentence in reverse order. (e.g. "I am a student" == "student a am I")
9. Longest Substring No Dupes - Given a string, please get the length of the longest substring which does not have duplicated characters. Supposing all characters in the string are in the range from ‘a’ to ‘z’. Input: "ababc", Output: 3.
10. CSV Parser - Write Method that takes a string representing a CSV and returns a useful JSON data structure.
11. Expand it! - Given a String in format "a2c2b5" where a character is followed by an integer of number of times repeated, expand the string. ex: "a2c2b5" sol = "aaccbbbbb"

###Math

1. PowersOfTwo - Compute 2^2^n in linear time
2. Swap Integers - Swap two integers in an array without using temporary variables
3. [Sum Two Arrays] - Write method to sum 2 arrays and return a new array. Arrays can be of different lengths. e.g. [1,3] + [1,0,0] == [1,1,3]
4. Smallest Number > k - Write method to find the smallest number which is greater than a given number k and has SAME SET OF DIGITS as given number
5. [Find Missing Integer] - Given an array of sorted consecutive integers, return the missing integer (or -1 if no integer is missing). E.g. [3,4,6,7] == 4. Complete solutions in both O(n) and O(log n) time. Follow-up: write a method that handles an unsorted array of integers between 0 and N in O(N) time. e.g. [3,5,7,4] == 6 
6. [P99 Website Latency] - Given an unsorted array of floats between 0 and 1, representing website latency times, return the 99th percentile time (the time that is greater than 99% of other times). This is an important metric in software development to identify worst case issues for users. Follow-up: Instead of an array, assume you are receiving an infinite stream of latency times and can't store them all. Create a Class to return the P99 at any given moment (methods void putTime(double time), double getP99()). Follow-up: Update your methods to handle variable percentiles (60th, 85th) and latency ranges (3 - 7 seconds). 
7. Multiply -  Implement multiplication of two numbers without using * operator

###Hash Tables

1. Open Addressing - Write a HashTable class that uses "linear probing" to resolve collisions (methods Get, Put, Remove)
2. [Chaining] - Write a HashTable class that uses LinkedLists to resolve collisions (methods Get, Put, Remove)
3. Dynamic Resizing - Add dynamic resizing to either above implementations

###Linked Lists

1. Double Linked List - Implement a Doubly Linked List
2. Remove Duplicates - Remove duplicates from both sorted and unsorted Singly Linked List
3. Delete Node - Delete node in middle of Single Linked List given access to only that node
4. [Is Circular] - Return true if single linked list is circular (corrupted). Go on to find the first node in the loop. Go on to find the size of the loop.
5. Circular Node - Find the first node in a circular single linked list
6. Sum Two Lists - Add two numbers together. Each number's digits are stored in a Single Linked List in reverse order (e.g. 134 == 4 --> 3 --> 1)
7. Find Intersection of Two lists - Given two lists, find the node at which they intersect and become one list
8. Linked List Basics - Series of easy problems that cover linked lists    
9. [Reverse Linked List] - Write Iterative and Recursive Solutions that reverse a linked list and return the new first node
10. Clone Linked List - Clone a linked structure with two pointers per node. Suppose that you are given a reference to the first node of a linked structure where each node has two pointers: one pointer to the next node in the sequence and one pointer to an arbitrary node.
11. Compare Two Lists - You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. The lists are equal only if they have the same number of nodes and corresponding nodes contain the same data. Write Recursive and Iterative solutions.
12. Delete Kth Node in LinkedList - Given a linked list and the position of a node to delete. Delete the node at the given position and return the head node.
13. Reverse Doubly Linked List
14. Insert Node Into Doubly Linked List
15. Merge Lists - Given 2 sorted lists, merge them into one list.


###Recursion

1. Fibonacci - Write method to generate the nth fibonacci number
2. Robot Squares - Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in 2 directions: right and down. How many possible paths are there for the robot?
3. String Permutations - Compute all permutations of a given string
4. [Powerset] - Return all possible subsets of a set (Recursive solution, Iterative, Bit Manipulation no loops)
5. [PowersetM] - Return all subsets of a set having M elements (Recursive, Iterative)
6. Valid Parentheses Pairs - Print all valid (e.g. properly opened and closed) combinations of n-pairs of parentheses. Input: 3, Output: ((())), (()()), (())(), ()(()), ()()()
7. Cents Combos - Given an infinite number of coins (25 cents, 10, 5, 1), return the number of possible ways of representing N cents.
8. Paint Fill - Implement the "paint fill" function one might see on an image editing program. Given a 2 dimensional matrix array of Colors, fill in the surrounding area until you hit a border or another filled-in square.

###Trees

1. Count Nodes at k distance - Given a binary tree, print the nodes k distance away from a target node
2. Implement Tree - That stores integers and has methods getParent(), setParent(), getChildren(), addChild(), removeChild(), getValue(), setValue()
3. Implement BinaryTree - That stores Strings with methods setParent, setValue, setLeftChild, setRightChild
4. Parse Tree Equation - Use BinaryTree to implement a mathematical equation parser. From equations list this, (3 + (4 * 5)), return a Binary tree that holds this equation
5. Tree Traversals - Write methods to print out root nodes using PreOrder, InOrder, and PostOrder algorithms
6. First Common Ancestor - Find the first common ancestor of two nodes in a binary tree. Avoid using additional data structures if possible. *** Java and CPP solutions
7. Min Height Tree - Given a sorted Array of Strings build the Binary Search Tree of minimal height.
8. Binary Search Tree - Implement a Binary Search Tree with methods Get(), Put(), and Delete()
9. Sub Tree of Binary Tree - Given two binary trees, S and T, determine if S is a subtree of T.
10. In Order Traversal of binary tree
11. Sum of 2 Nodes in BST- Given a binary search tree and an integer k, find two nodes whose values sum up to k.
12. Is Subtree - Assume you have two Binary Trees--t1 has millions of nodes and t2 has hundreds of nodes. Return true if t2 is a subtree of t1 (i.e. root of t2 is a node in t1)
13. Find_paths - Given a binary tree and an integer k, print all paths that sum up to k
14. Build Binary Search Tree - Given an array of strings, build a binary search tree. You can use the BinaryTree helper class.
15. Print Path To Key - You are given a Binary Search Tree. Write an algorithm to print the Path Array of a given key. PATH ARRAY:
a) If the given key is not present in the tree than the Path Array is equal to “-1”
b) If the given key is present in the BST, path array tells you the path (in terms of left & right direction) that you take from root to reach the given key. If you go towards right add “0” to the path array and if you go towards left add “1” to Path Array.
16. [Expression Tree] - Implement a method that builds a binary tree given a postfix expression like 73+2*. Write a second method to return the postfix expression String given a binary tree. Write a third method that returns the Infix expression String. Terms in the input expression are separated by spaces.
17. [Mirror Tree] - Write a method that takes a Binary Tree and returns a mirror image of that tree (i.e. all the left sides are on the right and vis versa). 
18. [Max Weight Subtree] - Given a BinaryTree, write a method that returns the substree of maximum weight. Each node in the subtree carries an integer (+/-) value which represents that node's weight.
19. Zig_Zag_Tree - Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
20. Binary Search Tree to LL- Convert a binary search tree to a linked list.
21. Iterative InOrder Traversal - Implement in-order traversal of tree iteratively.
22. Max Path Sum - find the max sum of a path in a binary search tree.
23. Find Predecessor/Find Successor - implment functions to find predecessor and successor in BST
24. Invert Tree- WAF to invert a tree. 
25. Delete Node - WAF to delete node from a tree.
26. Common Ancestor - Given two nodes in a binary tree, implement a function that returns the closet common ancestor of both nodes in the tree.


###Stacks

1. Implement Stack - Push, Pop, Peek, IsEmpty methods
2. Stacks with Array - Implement 3 stacks using a single array.
3. Set of Stacks - Consider a Stack of plates. If one stack gets too high, create a new stack of plates. Implement a special stack that holds these multiple stacks. When the first stack passes some threshold, the class creates a new stack and continues. Implement both Push and Pop methods.
4. Towers of Hanoi - 
5. Sort Stack - Write a method to sort a stack in ascending order using Push, Pop, Peek, and IsEmpty.
6. Evaluate Expression - Evaluate a space-delimited postfix expression String. e.g. "( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )" == 101
7. Stack With Max - Create a data structure that efficiently supports the stack operations (push and pop) and also a return-the-maximum operation. Assume the elements are reals numbers so that you can compare them.

###Queues

1. Implement Queue w Linked List - Enqueue, Dequeue, Size methods.
2. Implement Queue w Resizing Array - Enqueue, Dequeue, Size methods.
3. Queue With Stacks - Implement a queue using 2 Stacks
4. Queue With Circular Linked List - Implement a queue using a circular linked list (no links are null and the value of last.next = first). Keep only one Node instance variable (last).

###Heaps

1. Binary Heap - Implement a Binary Heap of integers with methods - isEmpty(), getSize(), getMin(), deleteMin(), buildBinaryTreeFromList(), insertElement()
2. Binary Heap in CPP - ""

###Graphs

1. Implement a Directed Graph using the Adjacent List technique
2. BFS - Find the Vertex in a Graph that holds the key "E" using Breadth First Search.
3. DFS - Implement Recursive and Iterative versions of Depth-First Search, which visit and print out every Vertex in Graph
4. Topological Sort - Implement Recursive (DFS) and Iterative versions of Topological Sort
5. [Chess Moves] - Write a class that calculates the minimum number of moves required to move from point A to point B on a 10x10 chess board. Implement methods to handle moves for Rook, Queen, King, and Knight.
6. [Amazon Locker] - Write a method to find the nearest Amazon locker, given a starting Vertex, which has methods getNeighbors() and isLocker(). The graph can be infinitely big, and you don't know the location of the amazon lockers. 
7. Implement a Graph and Vertex
8. Pretty Print - Starting with a single Vertex, implement a method that prints out a string representation of a Graph that resembles a visual web 

###Sets

1. [Implement Set] - Implement hash function, add, contains methods and constructor methods.

###Design

1. [Parking Lot] - Model an OOP design for an attendant-less parking lot. To start, walk through the entire customer experience, keeping track of each time software is required.




*[Brackets] highlight questions that we were asked in an interview 