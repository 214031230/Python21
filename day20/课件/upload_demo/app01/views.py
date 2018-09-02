from django.shortcuts import render, HttpResponse

# Create your views here.


def upload(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        # 从上传的文件数据中拿到 avatar对应的文件对象
        file_obj = request.FILES.get("avatar")
        # 在服务端新建一个和上传文件同名的新文件
        with open(file_obj.name, "wb") as f:
            # 从上传文件对象中一点一点读数据
            for i in file_obj:
                # 写入服务端新建的文件
                f.write(i)
        return HttpResponse("OK")
    return render(request, "upload.html")


# ajax上传文件
def ajax_upload(request):
    return render(request, "ajax_upload.html")