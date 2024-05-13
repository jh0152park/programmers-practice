function solution(todo_list, finished) {
    var answer = [];
    return todo_list.filter((item, index) => !finished[index] ? item : "");
}