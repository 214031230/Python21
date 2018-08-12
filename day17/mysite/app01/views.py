from django.shortcuts import render
from django.views import View


# Create your views here.
class Upload(View):
    """
    上传文件
    """
    def get(self, request):
        return render(request, "upload.html")
    
    def post(self, request):
        file_obj = request.FILES.get("code")
        file_name = file_obj.name
        with open(file_name, "wb") as f:
            for i in file_obj.chunks():
                f.write(i)
        return render(request, "upload.html", {"status": "上传成功"})
