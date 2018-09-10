$(function () {
    // 前端校验两次密码是否一致，后端也会校验
    $("#password_new_2").blur(function () {
        if ($("#password_new_1").val() != $("#password_new_2").val()) {
            $(".error_dif").text("两次密码输入不一致！")
        }
    }).focus(function () {  // 获取标签焦点以后删除错误信息
        $(".error_dif").text("")
    });
});