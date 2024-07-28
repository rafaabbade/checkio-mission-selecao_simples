"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        
    {
        "input": [(1, 2, 3, 4, 5)],
        "answer": [1, 3, 4]
    },
    {
        "input": [('a', 'b', 'c', 'd', 'e')],
        "answer": ['a', 'c', 'd']
    },
    {
        "input": [(10, 20, 30)],
        "answer": [10, 30, 20]
    },
    {
        "input": [(100, 200, 300, 400, 500, 600, 700)],
        "answer": [100, 300, 600]
    }

    ]
}
