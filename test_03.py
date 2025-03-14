# Leetcode 2226. Maximum Candies Allocated to K Children

# Ultimately did not work. 
def maximumCandies_01(candies: list[int], k: int) -> int:
    if sum(candies) < k:
        return 0
    
    while k > len(candies):
        _amount_moved_over = max(candies) - min(candies)
        _index_to_modify = candies.index(max(candies))
        candies[_index_to_modify] = min(candies)
        candies.append(_amount_moved_over)

    _min = min(candies)
    _average = sum(candies) // k

    return min(_min, _average)


# Testcases passed!
# Solution accepted!
def maximumCandies(candies: list[int], k: int) -> int:
    def this_number_of_candies_can_work(n: int) -> bool:
        total = 0
        for val in candies:
            _num = val // n
            total += _num
        if total >= k:
            return True
        
        return False
    
    if sum(candies) < k:
        return 0
    
    left = 1
    right = sum(candies) // k

    while left <= right:
        middle = (left + right) // 2
        
        if this_number_of_candies_can_work(middle):
            left = middle + 1
        else:
            right = middle - 1

    return right

def main() -> None:
    print(maximumCandies(candies = [5,8,6], k = 3)) # 5
    print(maximumCandies(candies = [2,5], k = 11))  # 0
    print(maximumCandies(candies = [4,7,5], k = 4))  # 3  testcase 49 / 100 didn't pass
    print(maximumCandies(candies = [1,2,3,4,10], k = 5))  # 3  testcase 5 / 100 didn't pass
    
    # should have been a testcase since it shows you you can't just pick 
    # the minimum of the values if the len(candies) == k
    # that would be 1 here, but the actual answer is 50
    print(maximumCandies(candies = [1, 100, 100], k = 3))  



if __name__ == '__main__':
    main()