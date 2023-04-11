my_list = ["apples", "spinach", "bread", "milk", ["chicken", ["tuna", "salmon"], "lamb"], "salmon"]

print(my_list[4][1][1])

my_list2 = ["apples", "bread", "milk", "fish", "sausage"]
print(my_list2)

my_healthy_list = ["quinoa", "avocado", "lowfat Greek yogurt"]
my_list2.extend(my_healthy_list)
print(my_list2)

my_list2.append("quinoa")
print(my_list2)

#append a list into a list
my_list2.append(["apple", "potato"])
print(my_list2)

#insert quinoa into original list between apples and bread
my_list.insert(1, "quinoa")
print(my_list)

