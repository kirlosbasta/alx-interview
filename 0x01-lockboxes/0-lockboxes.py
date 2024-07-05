#!/usr/bin/python3
'''0-lockboxes: Lockboxes'''


def canUnlockAll(boxes):
    '''Check if all the boxes can be unlocked'''
    boxes_len = len(boxes)
    if boxes_len == 0:
        return False
    visited = set([0])
    stack = [*boxes[0]]
    while (stack):
        key = stack.pop()
        if key > boxes_len - 1:
            continue
        if key in visited:
            continue
        visited.add(key)
        stack.extend(boxes[key])
    return len(visited) == boxes_len
