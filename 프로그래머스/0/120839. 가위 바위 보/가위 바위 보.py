def solution(rsp):
    option = {
        "2": "0",
        "0": "5",
        "5": "2"
    }
    return "".join([option[i] for i in rsp])