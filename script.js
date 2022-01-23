function launchtrain(trainame) {
    var elem = document.getElementById(trainame);
    var randomColor = Math.floor(Math.random()*16777215).toString(16);
        elem.style.fill = '#'+ randomColor;
        elem.classList.add("move");
}

function traincascade() {
    var minutes = 6;
    var seconds = 52;
    var secondsstring = seconds.toString();

    const timer = setInterval(function() {
    seconds++
    if (seconds >= 60) {
        minutes ++
        seconds = 0
    }
    if (seconds < 10) {
        secondsstring = '0' + seconds.toString();
    } else {
        secondsstring = seconds.toString()
    }
    document.getElementById("timer").innerHTML = minutes.toString() + ':' + secondsstring;
    }, 600);
    /** Every 600ms represents 1 minute */
    
    launchtrain('train1')
    setTimeout(function(){launchtrain('train2')}, 6000)
    setTimeout(function(){launchtrain('train3')}, 9000)
    setTimeout(function(){launchtrain('train4')}, 12000)
    setTimeout(function(){launchtrain('train5')}, 15000)
    setTimeout(function(){launchtrain('train6')}, 21000)
    setTimeout(function(){launchtrain('train7')}, 27000)
    setTimeout(function(){launchtrain('train8')}, 33000)
    setTimeout(function(){launchtrain('train9')}, 39000)
    setTimeout(function(){launchtrain('train10')}, 45000)
    setTimeout(function(){launchtrain('train11')}, 51000)
    setTimeout(function(){launchtrain('train12')}, 63000)
    setTimeout(function(){launchtrain('train13')}, 78000)
    setTimeout(function(){launchtrain('train14')}, 90000)
    setTimeout(function(){launchtrain('train15')}, 96000)
    setTimeout(function(){launchtrain('train16')}, 108000)
    setTimeout(function(){clearInterval(timer)}, 130200)
}
