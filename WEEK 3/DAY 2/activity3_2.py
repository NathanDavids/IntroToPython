list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# Access the nested lists and extend with the sub list
list1[2][1][2].extend(sub_list)

print(list1)