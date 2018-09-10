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
        // 使用ajax提交，同样需要携带csrfmiddlewaretoken，通过属性选择器拿到标签的值
        // 头像
        fd.append("avatar", $("#id_avatar")[0].files[0]);
        // 头像不能通过val取值
        $.ajax({
            url: "/register/",
            type: "post",
            data: fd,
            contentType: false,
            processData: false,
            success: function (res) {
                if (res.code === 1) {  // res 是后端返回的json对象，当code等于1的时候，注册校验失败
                    $.each(res.error, function (k, v) {  // each 遍历循环所有的错误，并显示出来
                        // 遍历所有字段的错误提示，将错误提示信息展示在页面上对应的位置
                        console.log(k, v[0]);  // 在控制台打印错误信息
                        $("#id_" + k).next().text(v[0]).parent().addClass("has-error")
                        // next 获取同级的下一个标签，即span 并内容为错误信息，给父类标签添加一个bs样式，显示input框为红色
                    })
                }
                else {
                    location.href = res.url // 当code == 0 的时候注册成功跳转到登录页面 res.url 是后端返回的页面
                }
            }
        })
    });
    // 给input标签绑定获取焦点就删除错误提示的动作
    $(".form-horizontal input").focus(function () {
        $(this).next().text().parent().removeClass("has-error");
    });

    // 预览头像
    $("#id_avatar").change(function () {  // change 当标签值发生更改的事件
        // 取到用户选中的头像文件
        var fileObj = this.files[0];
        // 新建一个FileReader对象，从本地磁盘加载文件数据
        var fr = new FileReader();
        fr.readAsDataURL(fileObj);
        // 读取文件是需要时间的 使用onload加载完毕以后在修改图片的图片路径为头像路径
        fr.onload = function () {
            $("#id_img_avatar").attr("src", fr.result)
        }
    });
});