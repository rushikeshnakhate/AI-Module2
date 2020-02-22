import itertools
from dataclasses import dataclass, field
from heapq import heappush, heappop
from typing import Any

REMOVED = '<removed-task>'


@dataclass()
class PriotizedItem:
    Priority: int
    item: Any = field(compare=False)


entry_finder = {}
counter = itertools.count()
pq = []


def remove_task(task):
    entry = entry_finder(task)
    entry[-1] = REMOVED


def add_task(task, priority):
    # if task in entry_finder:
    #     remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)


def pop_task():
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
