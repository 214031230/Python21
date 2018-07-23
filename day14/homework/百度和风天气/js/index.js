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
                $("p").text(data)
            },
            error: function (err) {
                console.log(err);
            }
        })
    };
    var t = setInterval(run,3000);

});