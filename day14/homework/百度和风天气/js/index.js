$(function () {
    $(".hefeng").mouseover(function () {
        $(".hefenginfo").stop().slideDown(500);
    }).mouseout(function () {
        $(".hefenginfo").stop().slideUp(500);
    });
    $(".hefenginfo").mouseover(function () {
        $(".hefenginfo").stop().slideDown(500);
    }).mouseout(function () {
        $(".hefenginfo").stop().slideUp(500);
    });
    var run = function () {
        $.ajax({
            url: 'https://free-api.heweather.com/s6/weather/now?location=beijing&key=b73a12edfab24ef6827447dc7557f50d',
            type: "get",
            dataType: 'text',
            success: function (data) {
                // 把字符串转换成可操作的数组
                var jsonData = JSON.parse(data);
                console.log(jsonData);
                $(".city").text(jsonData.HeWeather6[0].basic.parent_city+"：");
                $(".hefeng>.cond_code").attr("src","./images/cond-icon-heweather/"+jsonData.HeWeather6[0].now.cond_code+".png")
                $(".hefeng>.wendu").text(jsonData.HeWeather6[0].now.tmp+"℃");
            },
            error: function (err) {
                console.log(err);
            }
        });
        $.ajax({
            url: 'https://free-api.heweather.com/s6/air/now?location=beijing&key=b73a12edfab24ef6827447dc7557f50d',
            type: "get",
            dataType: 'text',
            success: function (data) {
                // 把字符串转换成可操作的数组
                var jsonData = JSON.parse(data);
                console.log(jsonData);
                $(".kongqi").text(jsonData.HeWeather6[0].air_now_city.qlty);
                $(".zhishu").text(jsonData.HeWeather6[0].air_now_city.pm25);
            },
            error: function (err) {
                console.log(err);
            }
        })
    };
    run()
    // var t = setInterval(run,3000);

});