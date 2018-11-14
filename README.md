# -python-selenium-
在风之动漫网上下载海贼王到本地，输入需要下载的章节，将漫画下载的本地

在风之动漫网上下载海贼王，输入需要下载的章节，将漫画下载的本地
实现思路：
 1 海贼王的漫画目录链接是：https://www.fzdm.com/manhua/02/
 2 第X话的漫画。连接是https://www.fzdm.com/manhua/02/X/，例如，924话链接是https://www.fzdm.com/manhua/02/924/
 3 第X话漫画中，第一页的链接是：https://www.fzdm.com/manhua/02/924/，第二页是https://www.fzdm.com/manhua/02/924/index_1.html
   第三页是https://www.fzdm.com/manhua/02/924/index_2.html，经尝试，index_0.html就是第一页的链接
 4 利用迭代，可以获得一到最后一页的图片，但是无法准确知道那一页是最后一页，利用try..exception..函数，抛出异常，并结束。
 5 因为，图片的链接使用js脚本加载的，无法直接在静态网页中获得http链接，所以使用selenium定位图片位置，然后使用get_attribute('src')
   获得图片的链接
 6 之后用resquests请求，将图片下载的本地

需要改进的部分
1.预先读取每一章节的页数，然后直接将range()定到定位的数字，不再通过抛出异常了完成程序
2.因为风之动漫这个网站本身的问题，337话以前的内容，url的格式不同，所以在获得输入之后，先判断，然后在给出对应的url
3.本次代码并没有模块化，后期进行改进

收获
本次最大的收获是关于图片的下载后的存储位置
os.mkdir(dirname)
#此处相当于文件路径 test/image.jpg，也就是将image.jpg文件存入test文件夹中
filename=dirname+'/'+'image.jpg'
#打开文件夹并写入图片
with open(filename,'wb') as f:
  f.write(response.content)
  
