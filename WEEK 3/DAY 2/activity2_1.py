list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result1 = [list1[i] + list2[i] for i in range(1)]
result2 = [list1[i] + list2[1] for i in range(1)]
result3 = [list1[1] + list2[i] for i in range(1)]
result4 = [list1[1] + list2[1] for i in range(1)]
finalresult = result1 + result2 + result3 + result4
print(finalresult)