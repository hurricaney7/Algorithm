# These code here is not runnable
# Copy and paste to leetcode to run respective algorithms

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # Pre-order traversal recursive
    def __init__(self):
        self.l = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root != None:
            self.l.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.l

    # Pre-order traversal iteration
    # 35 ms
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        path = []
        stack = [root]
        if not root:
            return []
        else:
            while len(stack) != 0:
                cur = stack.pop()
                path.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return path

    # BFS max depth
    # 50 - 60 ms
    def max_depth(self, root: TreeNode) -> int:
        queue = [(root, 1)]
        level = 0
        if not root:
            return level
        while len(queue) != 0:
            cur = queue[0]
            level = cur[1]
            del queue[0]
            if cur[0].left:
                queue.append((cur[0].left, cur[1] + 1))
            if cur[0].right:
                queue.append((cur[0].right, cur[1] + 1))
        return level

    def max_depth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            l = self.max_depth2(root.left)
            r = self.max_depth2(root.right)
        return max(l, r) + 1
