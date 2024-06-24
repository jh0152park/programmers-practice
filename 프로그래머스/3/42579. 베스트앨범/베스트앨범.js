function solution(genres, plays) {
    let results = [];
    let obj = {};
    let songInfo = {};
    
    for(let i = 0; i < genres.length; i++) {
        obj[genres[i]] = (obj[genres[i]] || 0) + plays[i];
        songInfo[i] = { play: plays[i], genre: genres[i]}
    }
    
    let sortedGenres = Object.keys(obj).sort((a, b) => obj[b] - obj[a]);
    
    sortedGenres.forEach((genre) => {
        const topSongs = Object.values(songInfo).
        filter((song) => song.genre === genre).
        sort((a, b) => b.play - a.play).
        slice(0, 2);
        
        topSongs.forEach((song) => {
            results.push(Object.values(songInfo).indexOf(song));
        })
    })
       
    return results;
}
