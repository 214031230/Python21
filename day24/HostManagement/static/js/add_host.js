$(function () {
    $("form").submit(function () {
            if ($("#ip").val() == "" || $("#hostname").val() == "") {
                $("#check").text("主机ip或者服务名称不能为空！").css("color", "red");
                return false
            }
            else {
                return true
            }

        }
    )
});