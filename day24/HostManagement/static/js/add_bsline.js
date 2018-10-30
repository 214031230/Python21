$(function () {
    $("form").submit(function () {
        if ($("#name").val() == "") {
            $("#check").text("业务名称不能为空！").css("color", "red");
            return false
        }
        else {
            return true
        }

    })
});