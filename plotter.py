import matplotlib.animation as animation
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot(code, chars):

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # The label locations
    x = np.arange(len(chars))
    # The width of the bars
    width = 0.35
    font_size = 15

    # Sort character frequency dictionary based on values rather than keys
    chars = {k: v for k, v in sorted(chars.items(), key=lambda item: -item[1])}

    # Labels for the bars
    labels = [l for l in chars]

    # Create character count and encoded character length lists
    char_freq = [chars[c] for c in labels]
    char_encoded_len = [len(code[c]) for c in labels]

    # The two bars in the plot
    # Original character count
    rects1 = ax1.bar(x - width / 2, char_freq, width, label='Original distribution', color='salmon')
    ax1.set_ylabel('Frequency', color='salmon', size=font_size)
    ax1.tick_params(axis='y', labelcolor='salmon', labelsize=font_size/1.25)

    # Huffman encoded count
    rects2 = ax2.bar(x + width / 2, char_encoded_len, width,
                     label='Huffman code length', color='lightseagreen')
    ax2.set_ylabel('Encoded Length', color='lightseagreen', size=font_size)
    ax2.tick_params(axis='y', labelcolor='lightseagreen', labelsize=font_size/1.25)

    # Add some text for labels, title and custom x-ax1is tick labels, etc.
    ax1.set_title('Distribution of original and encoded character length after Huffman code', size=font_size)
    ax1.set_xlabel('Character', size=font_size)
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, size=font_size/1.25)

    fig.legend()
    plt.show()


def myanimate():
    import sys
    import time
    # k = 0
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    # ani = animation.FuncAnimation(fig, animate, interval=1000)
    try:
        buff = ''
        while True:
            buff += sys.stdin.read(1)
            # if buff.endswith('\n'):
            #     print buff[:-1]
            #     buff = ''
            #     k = k + 1
            code, chars = run(buff)
            ax1.clear()
            ax2.clear()
            plot(code, chars, fig, ax1, ax2)
            plt.show()
    except KeyboardInterrupt:
        sys.stdout.flush()
