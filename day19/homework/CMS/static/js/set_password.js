$(function () {
    $("#password_new_2").blur(function () {
        if ($("#password_new_1").val() != $("#password_new_2").val()) {
            $(".error_dif").text("两次密码输入不一致！")
        }
    }).focus(function () {
        $(".error_dif").text("")
    });
});