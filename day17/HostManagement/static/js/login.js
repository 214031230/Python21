$(function () {
    $("form").submit(function () {
        if ($("#username").val() == "" || $("#password").val() == "") {
            $("#check").text("用户名或密码不能为空").css("color", "red");
            return false
        }
        // if ($.trim($("#code").val().toUpperCase()) == $.trim($("#user_code").val().toUpperCase())) {
        if ($.trim($("#code").val().toUpperCase()) == "666") {
            return true
        }
        else {
            $("#check").text("验证码不正确").css("color", "red");
            return false
        }
    })
});