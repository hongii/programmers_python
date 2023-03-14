def solution(dartResult):
    nums = []
    i = 0
    while i < len(dartResult):
        if dartResult[i] in ["S", "D", "T"]:
            i += 1
            continue
            
        if dartResult[i] == "*":
            y = nums.pop()
            if len(nums) != 0:
                x = nums.pop()
                nums.append(x * 2)
            nums.append(y * 2)
        elif dartResult[i] == "#":
            x = nums.pop()
            nums.append(x * (-1))
        else:
            if dartResult[i+1].isdecimal():
                num, bonus = int(dartResult[i:i+2]), dartResult[i+2]
                i += 1
            else: 
                num, bonus = int(dartResult[i]), dartResult[i+1]

            if bonus == "S":
                nums.append(num ** 1)
            elif bonus == "D":
                nums.append(num ** 2)
            elif bonus == "T":
                nums.append(num ** 3)
        i += 1
        # print(nums)
    return sum(nums)
            
            
            