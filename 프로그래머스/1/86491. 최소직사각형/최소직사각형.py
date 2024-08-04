def solution(sizes):
    widths = []
    heights = []
    for w, h in sizes:
        long = max(w, h)
        short = min(w, h)
        widths.append(long)
        heights.append(short)
        
    print(widths)
    print(heights)
    return max(widths) * max(heights)