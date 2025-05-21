#!/usr/bin/env python3

def print_fibonacci(length):
    sequence=[0,1]
    for _ in range(2,length):
        sequence.append(sequence[-1]+sequence[-2])
    print(sequence[:length])