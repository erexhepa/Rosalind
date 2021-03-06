#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.
Problem Title: Pattern Matching Problem
Chapter #: 01
Problem ID: C
URL: http://rosalind.info/problems/1c/
'''
def pattern_matching(pattern):

    input_file = 'dataset_2_9.txt'

    countPattern = 0

    with open(input_file) as input_data:
        dna, k = [line.strip() for line in input_data.readlines()]

    k = int(k)
    kmer_dict = dict()

    for i in xrange(len(dna)-k+1):
        if dna[i:i+k] in kmer_dict:
            kmer_dict[dna[i:i+k]] += 1
        else:
            kmer_dict[dna[i:i+k]] = 1

    kmers = [item[0] for item in kmer_dict.items() if item[1] == max(kmer_dict.values())]

    countPattern = ' '.join(kmers)
    print(countPattern)

    return countPattern

pattern_matching('test')
