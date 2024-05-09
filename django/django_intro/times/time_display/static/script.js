
        function updateTime() {
            var now = new Date();
            var hours = now.getHours();
            var minutes = now.getMinutes();
            var seconds = now.getSeconds();
            var timeString = hours + ':' + minutes + ':' + seconds;
            document.getElementById('current-time').innerText ="Time: "+ timeString;
        }

        updateTime();
        setInterval(updateTime, 1000);
