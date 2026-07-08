# 5 6
# 1 3
# 1 2
# 5 3
# 1 5
# 2 4
# 4 5
from collections import deque

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, m = int(inp1[0]), int(inp1[1])

    graph = dict()
    for i in range(n): graph[i+1] = []

    for i in range(m):
        inp2 = input().split(' ')
        e1, e2 = int(inp2[0]), int(inp2[1])
        graph[e1].append(e2)
        graph[e2].append(e1)

    parent = dict()
    visited = set()
    found = False
    start = None       # the neighbor closing the cycle
    end = None         # the node where the back-edge was found

    # Try every component. Stack holds (node, cameFrom) so we know each node's
    # real tree-parent when we pop it.
    for s in range(1, n + 1):
        if s in visited or found:
            continue
        stack = deque()
        stack.append((s, None))

        while len(stack) > 0 and not found:
            element, cameFrom = stack.pop()
            if element in visited:
                continue
            visited.add(element)
            parent[element] = cameFrom      # set parent only when actually traversed

            for neighbor in graph[element]:
                if neighbor not in visited:
                    stack.append((neighbor, element))
                elif neighbor != cameFrom:  # back-edge: visited, not our parent
                    found = True
                    start = neighbor        # one end of the cycle
                    end = element           # other end (has the back-edge)
                    break

    if not found:
        print("IMPOSSIBLE")
    else:
        # Climb parents from 'end' up to 'start' -> path start..end, then close
        # the loop by returning to start via the back-edge end--start.
        path = []
        cur = end
        while cur != start:
            path.append(cur)
            cur = parent[cur]
        path.append(start)      # now path = [end, ..., start]
        path.reverse()          # -> [start, ..., end]
        path.append(start)      # close the cycle

        print(len(path))
        print(' '.join(str(x) for x in path) + ' ')
