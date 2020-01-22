
class Node:

    def __init__(self, value=None, left_child=None, right_child=None):
        super().__init__()
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __gt__(self, other):
        return self.value > other.value


to_encode = input()

# bstr = bytes('az', 'utf-8')
# chars = {chr(c): 0 for c in range(bstr[0], bstr[1])}
chars = {}

for c in to_encode:
    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1

sorted_c = sorted((value, Node(value=key)) for (key, value) in chars.items())
print([n[1].value for n in sorted_c])

root = None
while True:
    if len(sorted_c) == 1:
        root = sorted_c.pop()[1]
        break
    first, second = sorted_c.pop(0), sorted_c.pop(0)
    temp_node = Node(left_child=first[1], right_child=second[1])
    sorted_c.append((first[0] + second[0], temp_node))
    sorted_c.sort()

print(root)


# sorted_c.append((0, 'd'))
# sorted_c.sort()
# print(sorted_c)

# for i in range(len(sorted_c)):
