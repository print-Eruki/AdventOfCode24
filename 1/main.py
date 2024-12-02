from collections import Counter
import heapq as pq

def read_input():
    left, right = [], []
    with open("input.txt", "r") as f:
        for line in f:
            curr = line.split()
            pq.heappush(left, int(curr[0]))
            pq.heappush(right, int(curr[1]))
    return left, right

def day1_part_one(left_lst: list[int], right_lst: list[int]) -> int:
    total = 0
    while left_lst and right_lst:
        left, right = pq.heappop(left_lst), pq.heappop(right_lst)
        total += abs(left - right)
    return total

def day1_part_two(left: list[int], right: list[int]) -> int:
    freq = Counter(right)
    total = 0
    for num in left:
            total += num * freq.get(num, 0)
    return total

if __name__ == "__main__":
    left, right = read_input()
    print(day1_part_one(left[:], right[:]))
    print(day1_part_two(left,right))