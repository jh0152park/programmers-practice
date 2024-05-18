function solution(id_pw, db) {
    const user_id = id_pw[0]
    const user_pw = id_pw[1]
    
    for(let data of db) {
        let id = data[0]
        let pw = data[1]
        
        if(user_id === id && user_pw === pw)
            return "login"
        else if(user_id === id && user_pw !== pw)
            return "wrong pw"
    }
    
    return "fail";
}