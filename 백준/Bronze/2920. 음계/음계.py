ascending = [1,2,3,4,5,6,7,8]
codes = list(map(int, input().split()))
if codes == ascending:
    print("ascending")
elif codes == ascending[::-1]:
    print("descending")
else:
    print("mixed")