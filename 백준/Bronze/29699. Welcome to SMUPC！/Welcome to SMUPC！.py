string = "WelcomeToSMUPC"
n = int(input())
print(string[n % len(string) - 1])