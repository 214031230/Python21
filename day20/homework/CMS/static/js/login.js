$(function () {
    $(".code_png").click(function () {
        this.src += "?";
    });
    $(".username,.password").focus(function () {
        $(".error_msg").text("")
    });
    $(".v_code").focus(function () {
        $(".code_msg").text("")
    });
});
