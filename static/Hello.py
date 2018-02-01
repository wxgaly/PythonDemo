# list 有序链表（可修改元素）
names = ["zhangsan", 1, "wangwu"]
a = ["a", 2.0]

names.append(a)
names.insert(1, "hah")

print("before names: ", names)

names.pop()
print("after names: ", names)

# tuple 有序元组（不可修改元素）
classes = {"class one", "class two"}
