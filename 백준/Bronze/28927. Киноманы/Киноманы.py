max_ = list(map(int, input().split()))
mel = list(map(int, input().split()))

max_time = max_[0] * 3
max_time += max_[1] * 20
max_time += max_[2] * 120

mel_time = mel[0] * 3
mel_time += mel[1] * 20
mel_time += mel[2] * 120

if max_time == mel_time:
    print("Draw")
elif max_time > mel_time:
    print("Max")
else:
    print("Mel")
