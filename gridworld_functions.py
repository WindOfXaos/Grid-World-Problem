import copy
from helper_functions import *


def generateActions(env):
    grid = env['grid']
    blocks = getLocation(grid, -1)
    car = getLocation(grid, 0)
    y, x = car
    height, width = len(grid), len(grid[0])
    actions = []

    if (y != 0) and isEmpty(car, blocks, "up"):
        actions.append('^')
    if (y != height - 1) and isEmpty(car, blocks, "down"):
        actions.append('v')
    if (x != width - 1) and isEmpty(car, blocks, "right"):
        actions.append('>')
    if (x != 0) and isEmpty(car, blocks, "left"):
        actions.append('<')

    return actions


def applyAction(old_env, action):
    env = copy.deepcopy(old_env)
    grid = env['grid']
    carY, carX = getLocation(grid, 0)

    if action == '>':
        grid[carY][carX] = 1
        grid[carY][carX + 1] = 0  # moves to the right column
        env['direction'] = action

    if action == '<':
        grid[carY][carX] = 1
        grid[carY][carX - 1] = 0  # moves to the left column
        env['direction'] = action

    if action == '^':
        grid[carY][carX] = 1
        grid[carY - 1][carX] = 0  # moves to the up row
        env['direction'] = action

    if action == 'v':
        grid[carY][carX] = 1
        grid[carY + 1][carX] = 0  # moves to the down row
        env['direction'] = action

    return env


def computeCost(env, action):
    if env['direction'] != action:
        return 2
    else:
        return 1


def isGoal(env):
    for row in env['grid']:
        # returns False if it finds (2 -> goal) in the grid and True otherwise.
        if 2 in row:
            return False
    return True


def h(env):
    grid = env['grid']
    car = getLocation(grid, 0)
    goal = getLocation(grid, 2)

    if goal:
        return 0
    else:
        return abs(goal[0] - car[0]) + abs(goal[1] - car[1])
