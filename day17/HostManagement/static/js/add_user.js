$(function () {
    $("form").submit(function () {
        if ($("#username").val() == "" || $("#password").val() == "") {
            $("#check").text("用户名或密码不能为空！").css("color", "red");
            return false
        }
        else {
            return true
        }

    })
});