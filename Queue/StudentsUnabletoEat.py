class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)
        res = n

        for sandwich in sandwiches :
            cnt = 0
            while cnt < n and sandwich != q[0]:
                val = q.popleft()
                q.append(val)
                cnt += 1
            
            if sandwich == q[0]:
                q.popleft()
                res -=1
            else:
                break
        return res
        