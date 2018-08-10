$(function () {
    $(".view").click(function () {
        $(this).addClass("active").siblings().removeClass("active")
    })
    $(".adduser").click(function () {
        location.href="/add_user/"
    })
    $(".change").click(function () {
        location.href="/user_list/"
    })
});