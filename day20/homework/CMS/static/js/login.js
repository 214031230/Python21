$(function () {
    // 验证码点击刷新功能，通过修改图片路径来实现自动刷新，给路径增加？对图片没有任何影响 可以起到点击刷新的功能
    $(".code_png").click(function () {
        this.src += "?";
    });
    // 用户名和密码获取焦点的时候删除错误信息
    $(".username,.password").focus(function () {
        $(".error_msg").text("")
    });
    // 验证码获取焦点的时候删除错误信息
    $(".v_code").focus(function () {
        $(".code_msg").text("")
    });
});
