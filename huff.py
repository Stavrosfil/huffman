import Node as Node
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def main():

    to_encode = input()
    char_freq = None

    # bstr = bytes('az', 'utf-8')
    # chars = {chr(c): 0 for c in range(bstr[0], bstr[1])}
    chars = {}

    for c in to_encode:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    sorted_n = sorted(Node.Node(value=char, freq=freq) for (char, freq) in chars.items())

    while True:

        # If the procedure is done, only one node will be left inside the list
        # This will be the root node of the tree
        if len(sorted_n) == 1:
            break

        # Extract the first two nodes, containing the least possible values.
        first, second = sorted_n.pop(0), sorted_n.pop(0)
        # Create a temporary node containing the two selected nodes as children
        temp_node = Node.Node(left_child=first, right_child=second, freq=(first.freq + second.freq))
        # Add the temporary node back to our (now unsorted) list
        sorted_n.append(temp_node)
        # Sort the list again
        sorted_n.sort()

    code = {}
    generate_huffman_code(sorted_n.pop(), code, '')
    # print(code)
    # print(encode(to_encode, code))
    plot(code, chars)


def plot(code, chars):

    # The label locations
    x = np.arange(len(chars))
    # The width of the bars
    width = 0.35
    fig, ax = plt.subplots()

    # The ranges of the two dictionaries, for plot normalization
    # TODO: oneline with list unpacking
    range1 = 0
    range2 = 0
    for char in chars:
        range1 = max(range1, chars[char])
        range2 = max(range2, len(code[char]))

    # Sort character frequency dictionary based on values rather than keys
    chars = {k: v for k, v in sorted(chars.items(), key=lambda item: item[1])}

    # Labels for the bars
    labels = [l for l in chars]

    # Create normalized character count and encoded character length lists
    char_freq = [chars[c] / range1 for c in labels]
    char_encoded_len = [len(code[c]) / range2 for c in labels]

    # The two bars in the plot
    rects1 = ax.bar(x - width / 2, char_freq, width, label='Original distribution', color='salmon')
    rects2 = ax.bar(x + width / 2, char_encoded_len, width, label='Huffman code length', color='lightseagreen')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title('Distribution of original and encoded character length after Huffman code')
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Char')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()


def encode(msg, code):
    encoded = ''
    for c in msg:
        encoded += code[c]

    return(encoded)
    # return(''.join([code[c] for c in msg]))


def generate_huffman_code(root, ans, code):

    if root.value is not None:
        ans[root.value] = code
    else:
        generate_huffman_code(root.left_child, ans, code + '0')
        generate_huffman_code(root.right_child, ans, code + '1')


if __name__ == "__main__":
    main()
