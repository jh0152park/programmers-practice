function solution(ineq, eq, n, m) {
    switch(eq) {
        case "=":
            if(ineq === ">")
                return n >= m ? 1 : 0;
            else if(ineq === "<")
                return n <= m ? 1 : 0;
        case "!":
            if(ineq === ">")
                return n > m ? 1 : 0;
            else if(ineq === "<")
                return n < m ? 1 : 0;
    }
}