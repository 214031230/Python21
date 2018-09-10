$(function () {
    // 给input标签绑定获取焦点就删除错误提示的动作
    $(".form-horizontal input").focus(function () {
        $(this).next().text().parent().removeClass("has-error");
    });

    // 预览头像
        $("#id_avatar").change(function () {
        var fileObj = this.files[0];
        var fr = new FileReader();
        fr.readAsDataURL(fileObj);
        fr.onload = function () {
            $("#id_img_avatar").attr("src", fr.result)
        }
    });
});