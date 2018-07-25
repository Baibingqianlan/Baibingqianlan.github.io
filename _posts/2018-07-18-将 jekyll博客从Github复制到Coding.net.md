---
layout: post
---

coding.net也是代码托管网站，但是能被百度收录，所以将 jekyll博客从Github复制到Coding.net了。

原来coding对jekyll支持不好，所以有许多人用其它办法来实现。现在不用那么麻烦了。只需要修改_config.yml中的baseurl属性就可以了。

github是在host的后面直接接你的博客，coding则是又加了一级，这一级就是你的仓库名。所以将_config.yml配置文件设置为忽略中的一员，两个网站用不同的配置，就完美解决了。

### 注意
>.gitignore只能忽略那些原来没有被 track 的文件，如果某些文件已经被纳入了版本管理中，则修改 .gitignore 是无效的。
解决方法是先把本地缓存删除，然后再提交。

	git rm -r --cached .
	git add .
	git commit -m 'We really don't want Git to track this anymore!'

### 方法

添加本地忽略文件

	git update-index --assume-unchanged FILENAME

参考：

1. [git 远程存在文件本地不想提交](https://blog.csdn.net/need_you_i_dream/article/details/80163435)
2. [我的github](https://baibingqianlan.github.io/)
3. [我的coding](http://zhwa3232.coding.me/baibingqianlan.github.io/)