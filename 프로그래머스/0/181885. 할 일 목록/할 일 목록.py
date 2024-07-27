def solution(todo_list, finished):
    return [task for idx, task in enumerate(todo_list) if not finished[idx]]