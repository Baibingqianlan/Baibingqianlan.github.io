---
layout: post
---

coding.net也是代码托管网站，但是能被百度收录，所以将 jekyll博客从Github复制到Coding.net了。

原来coding对jekyll支持不好，所以有许多人用其它办法来实现。现在不用那么麻烦了。只需要修改_config.yml中的baseurl属性就可以了。

github是在host的后面直接接你的博客，coding则是又加了一级，这一级就是你的仓库名。所以将_config.yml配置文件设置为忽略中的一员，两个网站用不同的配置，就完美解决了。

