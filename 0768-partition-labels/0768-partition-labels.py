class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = [0] * 26
        for i , ch in enumerate(s):
            last_occ[ord(ch)- ord("a")] = i

        partition_start = 0
        partition_end = 0
        partition_sizes = []

        for i, ch in enumerate(s):
            partition_end = max(partition_end, last_occ[ord(ch)- ord("a")])
            if i == partition_end:
                partition_sizes.append(i - partition_start + 1)
                partition_start = i + 1

        return partition_sizes