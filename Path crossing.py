class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        seen = set(path)

        if len(seen) != len(path):
            return True
        else:
            return False
        This is so shallow girl
        """

        start = [0,0]
        seen = set()
        seen.add(tuple(start))

        for direction in path:
            if direction == "N":
                start[0] += 1
                if tuple(start) in seen:
                    return True
                else:
                    seen.add(tuple(start))

            if direction == "S":
                start[0] -= 1
                if tuple(start) in seen:
                    return True
                else:
                    seen.add(tuple(start))

            if direction == "E":
                start[1] += 1
                if tuple(start) in seen:
                    return True
                else:
                    seen.add(tuple(start))

            if direction == "W":
                start[1] -= 1
                if tuple(start) in seen:
                    return True
                else:
                    seen.add(tuple(start))
        
        return False

        
