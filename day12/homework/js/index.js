var divEle = document.getElementsByClassName("nav_right_left_iconfont")[0];
divEle.onmouseover = function () {
    if (divEle.style.backgroundPosition = "-84px") {
        divEle.style.backgroundPosition = "0";
    }
};
divEle.onmouseout = function () {
    if (divEle.style.backgroundPosition = "0") {
        divEle.style.backgroundPosition = "-84px";
    }
};

var div2Ele = document.getElementsByClassName("nav_right_right_iconfont")[0];
div2Ele.onmouseover = function () {
    if (div2Ele.style.backgroundPosition = "-124px") {
        div2Ele.style.backgroundPosition = "-43px";
    }
};
div2Ele.onmouseout = function () {
    if (div2Ele.style.backgroundPosition = "-43px") {
        div2Ele.style.backgroundPosition = "-124px";
    }
};