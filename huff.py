
class Node:

    def __init__(self, value=None, freq=0, left_child=None, right_child=None):
        super().__init__()
        self.value = value
        self.freq = freq
        self.left_child = left_child
        self.right_child = right_child

    def __gt__(self, other):
        return self.freq > other.freq


to_encode = input()

# bstr = bytes('az', 'utf-8')
# chars = {chr(c): 0 for c in range(bstr[0], bstr[1])}
chars = {}

for c in to_encode:
    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1

sorted_n = sorted(Node(value=char, freq=freq) for (char, freq) in chars.items())

while True:

    # If the procedure is done, only one node will be left inside the list
    # This will be the root node of the tree
    if len(sorted_n) == 1:
        break

    # Extract the first two nodes, containing the least possible values.
    first, second = sorted_n.pop(0), sorted_n.pop(0)
    # Create a temporary node containing the two selected nodes as children
    temp_node = Node(left_child=first, right_child=second, freq=(first.freq + second.freq))
    # Add the temporary node back to our (now unsorted) list
    sorted_n.append(temp_node)
    # Sort the list again
    sorted_n.sort()


print(sorted)
