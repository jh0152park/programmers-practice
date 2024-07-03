function solution(cacheSize, cities) {
    var answer = 0;
    let size = 0;
    let cache = [];
    
    if(cacheSize === 0) {
        return cities.length * 5;
    }
    
    let city = "";
    for(let i = 0; i < cities.length; i++) {
        city = cities[i].toLowerCase();
        
        if(cache.includes(city)) {
            answer += 1;
            cache = cache.filter((c) => c != city);
            size--;
        }
        else {
            answer += 5;
        }
        
        if(size >= cacheSize) {
            cache.shift();
            size--;
        }
        
        cache.push(city);
        size++;
    }
    
    return answer;
}