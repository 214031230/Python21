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
    })
});