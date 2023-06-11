class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if index >= len(self.arr):
            self.arr.extend([[(0, 0)] for _ in range(index - len(self.arr) + 1)])

        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        left = 0
        right = len(self.arr[index]) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.arr[index][mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        
        return self.arr[index][right][1]
