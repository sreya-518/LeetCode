#Using Queues
from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        i = 0 
        rotations = 0
        while rotations<len(queue) and queue:
            if queue[0] == sandwiches[i]:
                i += 1
                queue.popleft()
                rotations = 0
            else:
                queue.append(queue.popleft())
                rotations += 1
        return len(queue) 


        