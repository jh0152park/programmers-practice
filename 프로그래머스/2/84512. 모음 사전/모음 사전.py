from itertools import product


def tuple2str(words):
    new_words = []
    for word in words:
        string = []
        for c in word:
            string.append(c)
        new_words.append("".join(string))
    return new_words


def solution(word):
    entire_words = []
    letters = ['A', 'E', 'I', 'O', 'U']
    
    for length in range(1, 6):
        words = product(letters, repeat=length)
        words = tuple2str(words)
        for w in words:
            entire_words.append(w)
            
    entire_words.sort()

    return entire_words.index(word) + 1