#!/usr/bin/python3
'''0-lockboxes: Lockboxes'''
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    '''Check if all the boxes can be unlocked'''
    boxes_len = len(boxes)
    if boxes_len == 0:
        return False
    visited = set([0])
    stack: List[int] = [*boxes[0]]
    while (len(stack) != 0):
        key = stack.pop()
        if key > boxes_len - 1:
            continue
        if key in visited:
            continue
        visited.add(key)
        stack.extend(boxes[key])
    return len(visited) == len(boxes)
