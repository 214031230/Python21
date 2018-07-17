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

    var t1 = setInterval(runDate, 1000);
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
//     $(".radius").click(function () {
//         $(this).siblings().css("backgroundColor", "#666");
//         $(this).css("backgroundColor", "white");
//     })
// 圆点翻页结束
    // 轮播图开始
    function next() {
        for (let i = 0; i < $(".nav_right img").length; i++) {
            if ($(".nav_right img").eq(i).hasClass("hide")) {
                if (i == 5) {
                    i = -1
                }
                $(".nav_right img").eq(i + 1).addClass("hide").siblings().removeClass("hide");
                $(".radius").eq(i+1).css("backgroundColor", "white").siblings().css("backgroundColor", "#666");
                return
                return
            }
        }
    }

    function prev() {
        for (let i = 6; i >= -1; i--) {
            if ($(".nav_right img").eq(i).hasClass("hide")) {
                if (i == -1) {
                    i = 6
                }
                $(".nav_right img").eq(i - 1).addClass("hide").siblings().removeClass("hide");
                $(".radius").eq(i-1).css("backgroundColor", "white").siblings().css("backgroundColor", "#666");
                return
            }
        }
    }

    var down = setInterval(next, 3000);
    $(".nav_right_right_iconfont").click(function () {
        clearInterval(down);
        next();
    });
    $(".nav_right_left_iconfont").click(function () {
        clearInterval(down);
        prev();
    });
    $(".radius").click(function () {
        $(this).siblings().css("backgroundColor", "#666");
        $(this).css("backgroundColor", "white");
        clearInterval(down);
        for (let i = 0; i < $(".radius_item .radius").length; i++) {
            // console.log($(".radius").eq(i).css("backgroundColor"))
            if ($(".radius").eq(i).css("backgroundColor") == "rgb(255, 255, 255)") {
                $(".nav_right img").eq(i).addClass("hide").siblings().removeClass("hide");
            }
        }
    })
    // 轮播图结束

});




