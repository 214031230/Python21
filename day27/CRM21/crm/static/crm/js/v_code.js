$(function () {
    $(".v_code").click(function () {
        this.src += "?";
    });
    $(".form-control").focus(function () {
        $(".error_msg").text("");
    });
});
