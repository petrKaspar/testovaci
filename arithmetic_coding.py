#!/usr/bin/python

import random

prob = {
  'a': (0, 0.4),
	'b': (0.4, 0.3),
	'c': (0.7, 0.2),
	'@': (0.9, 0.1)
}

def encode(string, prob):
    start = 0
    width = 1
    for ch in string:
        d_start, d_width = prob[ch]
        print start, width
        print d_start, d_width
        start += d_start*width
        width *= d_width
        
    return random.uniform(start, start+width)
        
def decode(num, prob):
    string = []
    while True:
        for symbol, (start, width) in prob.iteritems():
            if 0 <= num - start < width:
                num = (num - start) / width
                string.append(symbol)
                break
        if symbol == '@':
            break
    
    return ''.join(string)        
        
encoded_number = encode('aababcbcacb@', prob)
decoded_string = decode(encoded_number, prob)
print encoded_number
print decoded_string