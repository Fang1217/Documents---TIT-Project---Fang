import pandas as pd
import numpy as np

class Node:
    def __init__(self, symbol, probability, left=None, right=None):
        self.symbol = symbol
        self.probability = probability
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.probability > other.probability

def huffman_coding(text):
    # Return encoding table DataFrame
    text = text.upper()
    letter_counts = {}
    total_letters = 0

    for letter in text:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
            total_letters += 1

    if total_letters == 0:
        return pd.DataFrame() # return empty dataframe as there are no letters
    
    unique_letters = list(letter_counts.keys())
    probabilities = [letter_counts[letter] / total_letters for letter in unique_letters]

    nodes = [Node(symbol, prob) for symbol, prob in zip(unique_letters, probabilities)]

    while len(nodes) > 1:
        nodes.sort()
        right, left = nodes.pop(), nodes.pop()
        parent = Node(None, left.probability + right.probability, left, right)
        
        # insert combined node in front such that the combined probability will
        # have higher precedence if there exist other symbols with equal probability.
        nodes.insert(0, parent) 

    codes = {}
    curr_node = nodes[0]
    curr_code = ""

    def traverse(node, code):
        if node is None:
            return
        if node.symbol is not None:
            codes[node.symbol] = code
            return

        traverse(node.left, code + "0")  # Second last 
        traverse(node.right, code + "1") # Last

    traverse(curr_node, curr_code)
    
    data = {
        'Letter': unique_letters
    }
    df = pd.DataFrame(data)
    df['Codeword'] = [codes[letter] for letter in unique_letters]
    df['Probability'] = [round(probability, 4) for probability in probabilities]
    df['Length'] = [len(codes[letter]) for letter in unique_letters]

    return df

def calculate_efficiency(dataframe):
    df = pd.DataFrame(dataframe)
    if df.empty:
        return 0
    l_bar = sum(df['Length'] * df['Probability'])
    print("Average code length: " + str(l_bar))

    entropy = sum(df['Probability'] * np.log2(1/df['Probability']))
    print("Entropy: " + str(entropy))

    efficiency = round(entropy/l_bar*100, 4)
    print("Efficiency: " + str(efficiency) + " %")

    return efficiency


def main():
    text = input("Enter the text to encode: ").upper()
    test = huffman_coding(text)
    print(test)
    calculate_efficiency(test)

if __name__ == "__main__":
    main()