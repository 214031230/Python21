$(function () {
    $(".hefeng").mouseover(function () {
        $(".hefenginfo").stop().slideDown(300);
    }).mouseout(function () {
        $(".hefenginfo").stop().slideUp(300);
    });
    $(".hefenginfo").mouseover(function () {
        $(".hefenginfo").stop().slideDown(300);
    }).mouseout(function () {
        $(".hefenginfo").stop().slideUp(300);
    });
    $(".day").mouseover(function () {
        $(this).css("color", "#0caff4")
    }).mouseout(function () {
        $(this).css("color", "black")
    }).click(function () {
        window.open("http://www.weather.com.cn/weather/101010100.shtml#7d","_blank")
    });
    var run = function () {
        $.ajax({
            url: 'https://free-api.heweather.com/s6/weather/?location=beijing&key=b73a12edfab24ef6827447dc7557f50d',
            type: "get",
            dataType: 'text',
            success: function (data) {
                // 把字符串转换成可操作的数组
                var jsonData = JSON.parse(data);
                // console.log(jsonData);
                var d = jsonData.HeWeather6[0];
                $(".city").text(d.basic.parent_city + "：");
                $(".hefeng>.cond_code").attr("src", "./images/cond-icon-heweather/" + d.daily_forecast[0].cond_code_d + ".png");
                $(".hf_head>.cond_code").attr("src", "./images/cond-icon-heweather/" + d.daily_forecast[0].cond_code_d + ".png");
                $(".hefeng>.wendu").text(d.now.tmp + "℃");
                $(".hf_day>.date").text(d.daily_forecast[0].date);
                for (var i = 0; i < 3; i++) {
                    $(".hf_tianqi .day").eq(i).children().eq(0).text(d.daily_forecast[i].date);
                    $(".hf_tianqi .day").eq(i).children().eq(1).attr("src", "./images/cond-icon-heweather/" + d.daily_forecast[i].cond_code_d + ".png");
                    $(".hf_tianqi .day").eq(i).children().eq(2).text(d.daily_forecast[i].tmp_min + "℃" + " ~ " + d.daily_forecast[i].tmp_max + "℃");
                    $(".hf_tianqi .day").eq(i).children().eq(3).text(d.daily_forecast[i].cond_txt_d);
                    $(".hf_tianqi .day").eq(i).children().eq(4).text(d.daily_forecast[i].wind_dir);
                }
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
                // console.log(jsonData);
                var d = jsonData.HeWeather6[0];
                $(".kongqi").text(d.air_now_city.qlty);
                $(".zhishu").text(d.air_now_city.pm25);
            },
            error: function (err) {
                console.log(err);
            }
        })
    };
    run();
});