class Solution(object):
    def connect(self, root):
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            head = leftmost
            while head:
                # 왼쪽 자식 → 오른쪽 자식
                head.left.next = head.right

                # 오른쪽 자식 → 옆 노드의 왼쪽 자식
                if head.next:
                    head.right.next = head.next.left

                head = head.next  # 다음 노드로 이동

            leftmost = leftmost.left  # 다음 레벨로 이동

        return root