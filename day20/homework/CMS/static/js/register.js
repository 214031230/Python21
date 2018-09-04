$(function () {
    // ajax 提价数据
    $(".reg-btn").click(function () {
        // 因为注册功能有头像文件 数据，所以要用FormData对象提交数据
        var fd = new FormData();
        fd.append("username", $("#id_username").val());
        fd.append("password", $("#id_password").val());
        fd.append("re_password", $("#id_re_password").val());
        fd.append("phone", $("#id_phone").val());
        fd.append("email", $("#id_email").val());
        fd.append("csrfmiddlewaretoken", $("[name='csrfmiddlewaretoken']").val());
        // 头像
        fd.append("avatar", $("#id_avatar")[0].files[0]);
        $.ajax({
            url: "/register/",
            type: "post",
            data: fd,
            contentType: false,
            processData: false,
            success: function (res) {
                if (res.code === 1){
                    $.each(res.error, function (k, v) {
                        // 遍历所有字段的错误提示，将错误提示信息展示在页面上对应的位置
                        console.log(k,v[0]);
                        $("#id_" + k).next().text(v[0]).parent().addClass("has-error")
                    })
                }
                else {
                    location.href = res.url
                }
            }
        })
    });
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