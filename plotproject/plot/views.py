from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import io
import urllib, base64
# Create your views here.

def index(request):
    return HttpResponse("123")
def index1(request):
    return HttpResponse("456")

def plot_view(request):
    # 數據
    x = [0,0.5, 1, 1.5, 2, 2.5,3]
    y = [0,0.5, 1, 1.5, 2, 2.5,3]
    plt.figure(edgecolor='black')
    plt.axes(facecolor='lightblue')
    # 建立圖表
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Plot')
    
    # plt.figure(figsize=(8, 6))

    # 將圖表轉成圖像
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 將圖像轉換為base64編碼字符串
    graphic = base64.b64encode(image_png).decode('utf-8')

    # 在模板中使用圖表
    return render(request, 'plot/plot.html', {'graphic': graphic})
    return HttpResponse("789")
