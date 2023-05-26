import heapq
from collections import defaultdict

def huffman_encode(message):
    """
    A function to encode a message using Huffman coding and return the encoded message and the Huffman tree.
    
    :param message: a string representing the message to be encoded
    :return: a tuple containing the encoded message and the Huffman tree
    """
    # calculate the frequency of each character in the message
    freq = defaultdict(int)
    for char in message:
        freq[char] += 1
    
    # create a priority queue of (frequency, character) pairs
    pq = [(f, c) for c, f in freq.items()]
    heapq.heapify(pq)
    
    # build the Huffman tree by repeatedly combining the two lowest frequency nodes until we have only one node left
    while len(pq) > 1:
        freq1, left = heapq.heappop(pq)
        freq2, right = heapq.heappop(pq)
        combined_freq = freq1 + freq2
        heapq.heappush(pq, (combined_freq, (left, right)))
        
    # get the encoding for each character by traversing the Huffman tree
    encoding = {}
    def traverse(node, code=''):
        if isinstance(node, tuple):
            traverse(node[0], code + '0')
            traverse(node[1], code + '1')
        else:
            encoding[node] = code
    traverse(pq[0][1])
    
    # encode the message using the Huffman encoding
    encoded_msg = ''.join(encoding[c] for c in message)
    
    return encoded_msg, pq[0][1]
