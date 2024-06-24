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

/*

function solution(genres, plays) {

  sortedGenre.forEach((genre) => {
    // 장르별로 재생 횟수가 많은 노래 2개씩 추출
    const genreSong = Object.values(info)
      .filter((song) => song.genre === genre)
      .sort((a, b) => b.play - a.play)
      .slice(0, 2);

    // 고유 번호를 result에 담음
    genreSong.forEach((gs) => {
      const uniqueId = Object.values(info).indexOf(gs);
      result.push(uniqueId);
    });
  });

  return result;
}

*/