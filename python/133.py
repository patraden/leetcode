from typing import Optional


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from queue import SimpleQueue

        if node is None:
            return None

        q = SimpleQueue()
        q.put(node)

        clones = {}
        visited = {node}

        while q.qsize() > 0:
            v = q.get()
            v_clone = clones.setdefault(v, Node(v.val))
            for w in v.neighbors:
                w_clone = clones.setdefault(w, Node(w.val))
                v_clone.neighbors.append(w_clone)
                if w not in visited:
                    visited.add(w)
                    q.put(w)

        return clones[node]


def test():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n3, n1]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n3, n1]

    nn1 = Solution().cloneGraph(n1)
    print(nn1.val)
    for n in nn1.neighbors:
        print(n.val, [m.val for m in n.neighbors])
        for m in n.neighbors:
            if m.val == 4:
                print(m.val, [k.val for k in m.neighbors])


if __name__ == '__main__':
    test()
