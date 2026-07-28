class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(i):
            x, y = points[i]
            return x * x + y * y
        def partition(left, right):
            pivot_index = random.randint(left, right)
            points[pivot_index], points[right] = points[right], points[pivot_index]
            pivot_dist = distance(right)
            p = left
            for i in range(left, right):
                if distance(i) <= pivot_dist:
                    points[p], points[i] = points[i], points[p]
                    p += 1
            points[p], points[right] = points[right], points[p]
            return p

        left = 0
        right = len(points) - 1

        while left <= right:
            pivot = partition(left, right)
            if pivot == k:
                break
            elif pivot < k:
                left = pivot + 1
            else:
                right = pivot - 1

        return points[:k]
