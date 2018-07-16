$(function () {
    // 箭头翻页开始
    $(".nav_right_left_iconfont").mouseover(function () {
        $(this).css("backgroundPosition", "0")
    }).mouseout(function () {
        $(this).css("backgroundPosition", "-84px");
    });
    $(".nav_right_right_iconfont").mouseover(function () {
        $(this).css("backgroundPosition", "-43px")
    }).mouseout(function () {
        $(this).css("backgroundPosition", "-124px")
    });
    // 箭头翻页结束
    // 时钟开始
    function runDate() {
        var myDate = new Date();
        var h = myDate.getHours();
        if (h < 10) {
            h = "0" + h;
        }
        $(".H").text(h);

        var m = myDate.getMinutes();
        if (m < 10) {
            m = "0" + m;
        }
        $(".M").text(m);

        var s = myDate.getSeconds();
        if (s < 10) {
            s = "0" + s;
        }
        $(".S").text(s);
    }
    var t1 = setInterval(runDate,1000);
// 时钟结束

// 购物车悬停框开始
    $(".topbar_cart").mouseover(function () {
        $(".topbar_cart_info").stop().slideDown(300);
    }).mouseout(function () {
         $(".topbar_cart_info").stop().slideUp(300);
    });
    // $(".topbar_cart").mouseout(function () {
    //      $(".topbar_cart_info").stop().slideUp(300);
    // });

// 圆点翻页开始
    $(".radius").click(function () {
        $(this).siblings().css("backgroundColor","#666");
        $(this).css("backgroundColor","white");
    })
// 圆点翻页结束


});




