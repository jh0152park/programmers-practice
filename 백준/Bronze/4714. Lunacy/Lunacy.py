import sys



while True:
    weight = float(sys.stdin.readline().strip())
    if weight < 0:
        break

    sys.stdout.write("Objects weighing %.2f on Earth will weigh %.2f on the moon.\n"%(weight, weight * 0.167))