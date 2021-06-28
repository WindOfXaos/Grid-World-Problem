import os
import time
import random

import ai_search
from gridworld_functions import *

"""
car => 0	goal => 2	blocked => -1	empty => 1	

-------------
| 1 | 1 | 1 |
-------------
| 0 | -1 | 1 |
-------------
| 1 | 1 | 2 |
-------------

direction => ^,v,<,>
"""

#env = {}


def printGrid(grid, direction):
    height, width = len(grid), len(grid[0])
    s = ""

    for row in grid:
        for item in row:
            if item == 0:
                s += direction
            elif item == 1:
                s += " "
            elif item == -1:
                s += "X"
            elif item == 2:
                s += "G"

    print('-'*(width*4+1))
    for i in range(width * height):
        print('| ' + s[i] + ' ', end='')
        if ((i + 1) % width) == 0:
            print('|')
            print('-'*(width*4+1))


def animate(Solution, env, strategy):
    S = Solution
    time.sleep(1)
    os.system('cls')
    print(strategy)
    for i in S:
        print(i, ": ", S[i])
    printGrid(env['grid'], env['direction'])


def shuffle(size, car, goal):
    env = {}
    numbers = [1, 1, -1]
    directions = ['^', 'v', '<', '>']

    env['grid'] = [[random.choice(numbers)
                    for i in range(size[0])] for j in range(size[1])]
    env['direction'] = random.choice(directions)
    env['grid'][car[0] - 1][car[1] - 1] = 0
    env['grid'][goal[0] - 1][goal[1] - 1] = 2

    return env


def humanSolve(env):
    while (True):

        os.system('cls')
        printGrid(env['grid'], env['direction'])

        available_actions = generateActions(env)
        print('available actions: ' + ' , '.join(available_actions))
        action = input("your action:")
        if action not in available_actions:
            print('Game Over')
            return
        env = applyAction(env, action)
        if isGoal(env):

            os.system('cls')
            printGrid(env['grid'], env['direction'])

            print("You win")
            return


def computerSolve(env, strategy, h = None, anime = False):
    S = ai_search.solve(strategy, env, generateActions,
                        applyAction, isGoal, computeCost, h)
    if S == "failure":
        return(print(strategy + "\n" + S))
    if not anime:
        print(strategy)
        for i in S:
            print(i, ": ", S[i])
        print('-'*50)
    else:
        env = copy.deepcopy(env)
        animate(S, env, strategy)
        input("Press Enter to start...")
        for action in S['solution']:
            env = applyAction(env, action)
            animate(S, env, strategy)
        input("Finished...")


###TESTING###
# env = shuffle([5, 5], [2, 2], [1, 4])

# humanSolve(env)

'''
computerSolve(env, 'DFS')
computerSolve(env, 'BFS')
computerSolve(env, 'UCS')
computerSolve(env, 'Greedy', h)
computerSolve(env, 'Astar', h)
'''