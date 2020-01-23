class Node:

    def __init__(self, value=None, freq=0, left_child=None, right_child=None):
        super().__init__()
        self.value = value
        self.freq = freq
        self.left_child = left_child
        self.right_child = right_child

    def __gt__(self, other):
        return self.freq > other.freq
