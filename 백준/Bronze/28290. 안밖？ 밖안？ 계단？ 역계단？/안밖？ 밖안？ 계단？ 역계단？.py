import sys


types = {
    "fdsajkl;": "in-out",
    "jkl;fdsa": "in-out",
    "asdf;lkj": "out-in",
    ";lkjasdf": "out-in",
    "asdfjkl;": "stairs",
    ";lkjfdsa": "reverse"
}

s = sys.stdin.readline().strip()
print(types.get(s, "molu"))