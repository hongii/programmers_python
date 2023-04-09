def solution(elements):
    nums = set()
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            if i+j >= len(elements):
                num = elements[j:i+j] + elements[:i+j-len(elements)]
                nums.add(sum(num))
            else:
                nums.add(sum(elements[j:i+j]))
    return len(nums)