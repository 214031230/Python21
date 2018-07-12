// 箭头翻页开始
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
// 箭头翻页结束
// 时钟开始
function runDate() {
    var myDate = new Date();
    var hEle = document.getElementsByClassName("H")[0];
    var h  = myDate.getHours();
    if (h < 10){
        h = "0" + h;
    }
    hEle.innerText = h;
    var mEle = document.getElementsByClassName("M")[0];
    var m = myDate.getMinutes();
    if (m < 10){
        m = "0" + m;
    }
    mEle.innerText = m;
    var sEle = document.getElementsByClassName("S")[0];
    var s = myDate.getSeconds();
    if (s < 10){
        s  = "0" + s;
    }
    sEle.innerText = s;
    window.setTimeout(runDate,1000)
}
window.onload = runDate;
// 时钟结束

// 购物车悬停框开始
var cartinfoEle = document.getElementsByClassName("topbar_cart_info")[0];
var cartEle = document.getElementsByClassName("topbar_cart")[0];
cartEle.onmouseover = function () {
    cartinfoEle.style.display = "block";
};
cartEle.onmouseout = function () {
    cartinfoEle.style.display = "none";
};

// 圆点翻页开始
var radiusEle = document.getElementsByClassName("radius");
for (var i = 0; i < radiusEle.length; i++) {
    radiusEle[i].onclick = function () {
        for (var i = 0; i < radiusEle.length; i++) {
            radiusEle[i].style.backgroundColor = "#666666"
        }
        this.style.backgroundColor = "white";
    };
}
// 圆点翻页结束



