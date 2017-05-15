var Chrono = function(id){
    var target = {};
    var isRunning = false;
    var timer;    
    var time = {
        hour: 0,
        second: 0,
        minute: 0
    };
    
    function start(){
        timer = setInterval(function(){
            // seconds
            time.second++;
            if(time.second >= 60)
            {
                time.second = 0;
                time.minute++;
            }      

            // minutes
            if(time.minute >= 60)
            {
                time.minute = 0;
                time.hour++;
            }

            target.hour.innerHTML = time.hour < 10 ? '0' + time.hour : time.hour;
            target.minute.innerHTML = time.minute < 10 ? '0' + time.minute : time.minute;
            target.second.innerHTML = time.second < 10 ? '0' + time.second : time.second;
            
            //console.log('Time elapsed: ' + time.hour + ':' + time.minute + ':' + time.second + ' from ' + id);
            
            isRunning = true;
        }, 1000);
    }
    
    function stop()
    {
        isRunning = false;
        clearInterval(timer);
    }
    
    function init(id){
        target = {
            hour: document.querySelectorAll(id + " .chrono-hour")[0],
            minute: document.querySelectorAll(id + " .chrono-minute")[0],
            second: document.querySelectorAll(id + " .chrono-second")[0],
        };
        
        var _btnStart = document.querySelectorAll(id + " .chrono-start")[0];
        
        _btnStart.addEventListener('click', function(){
            if(!isRunning) {
                _btnStart.innerHTML = 'Detener';
                start();
            }
            else {
                _btnStart.innerHTML = 'Continuar';
                stop();
            }
        })
    }
    
    init(id);
};