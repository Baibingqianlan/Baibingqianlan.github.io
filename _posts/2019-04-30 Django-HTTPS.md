---
layout: post
---

### 1.HTTPS

HTTPS（全称：Hyper Text Transfer Protocol over Secure Socket Layer 或 Hypertext Transfer Protocol Secure，超文本传输安全协议），是以安全为目标的HTTP通道，简单讲是HTTP的安全版。即HTTP下加入SSL层，HTTPS的安全基础是SSL，因此加密的详细内容就需要SSL。 它是一个URI scheme（抽象标识符体系），句法类同http:体系。用于安全的HTTP数据传输。https:URL表明它使用了HTTP，但HTTPS存在不同于HTTP的默认端口及一个加密/身份验证层（在HTTP与TCP之间）。这个系统的最初研发由网景公司(Netscape)进行，并内置于其浏览器Netscape Navigator中，提供了身份验证与加密通讯方法。现在它被广泛用于万维网上安全敏感的通讯，例如交易支付方面.

**历史**

网景在1994年创建了HTTPS，并应用在网景导航者浏览器中。 最初，HTTPS是与SSL一起使用的；在SSL逐渐演变到TLS时，最新的HTTPS也由在2000年五月公布的RFC 2818正式确定下来。

它是由Netscape开发并内置于其浏览器中，用于对数据进行加密和解密操作，并返回网络上传送回的结果。HTTPS实际上应用了Netscape的安全套接层（SSL）作为HTTP应用层的子层。（HTTPS使用端口443，而不是像HTTP那样使用端口80来和TCP/IP进行通信。）SSL使用40 位关键字作为RC4流加密算法，这对于商业信息的加密是合适的。HTTPS和SSL支持使用X.509数字认证，如果需要的话用户可以确认发送者是谁。 

也就是说它的主要作用可以分为两种：一种是建立一个信息安全通道，来保证数据传输的安全；另一种就是确认网站的真实性，凡是使用了 https 的网站，都可以通过点击浏览器地址栏的锁头标志来查看网站认证之后的真实信息，也可以通过 CA 机构颁发的安全签章来查询 
### 2.TLS

传输层安全性协议（英语：Transport Layer Security，缩写作TLS），及其前身安全套接层（Secure Sockets Layer，缩写作SSL）是一种安全协议，目的是为互联网通信提供安全及数据完整性保障。

IETF将SSL进行标准化，1999年公布第一版TLS标准文件。随后又公布RFC 5246 （2008年8月）与RFC 6176（2011年3月）。在浏览器、邮箱、即时通信、VoIP、网络传真等应用程序中，广泛支持这个协议。主要的网站，如Google、Facebook等也以这个协议来创建安全连线，发送数据。目前已成为互联网上保密通信的工业标准。

	协议			年份
	SSL 1.0		未知
	SSL 2.0		1995
	SSL 3.0		1996
	TLS 1.0		1999
	TLS 1.1		2006
	TLS 1.2		2008
	TLS 1.3		2018

### 3.HTTPS和HTTP的区别

HTTPS和HTTP的区别主要为以下四点：
一、https协议需要到ca申请证书，一般免费证书很少，需要交费。
二、http是超文本传输协议，信息是明文传输，https 则是具有安全性的ssl加密传输协议。
三、http和https使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。
四、http的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比http协议安全。


### 4.OPENSSL
OpenSSL 是一个开源项目，其组成主要包括一下三个组件：
	
	openssl：多用途的命令行工具
	libcrypto：加密算法库	
	libssl：加密模块应用库，实现了ssl及tls

+ **对称加密**

对称加密需要使用的标准命令为 enc ，用法如下：

openssl enc -ciphername [-in filename] [-out filename] [-pass arg] [-e] [-d] [-a/-base64]
       [-A] [-k password] [-kfile filename] [-K key] [-iv IV] [-S salt] [-salt] [-nosalt] [-z] [-md]
       [-p] [-P] [-bufsize number] [-nopad] [-debug] [-none] [-engine id]

示例：

	加密： openssl enc -e -des3 -a -salt -in fstab -out jiami
	解密： openssl enc -d -des3 -a -salt -in fstab -out jiami

+ **生成随机数**

生成随机数需要用到的标准命令为 rand ，用法如下：

openssl rand [-out file] [-rand file(s)] [-base64] [-hex] num

+ **秘钥操作**

首先需要先使用 genrsa 标准命令生成私钥，然后再使用 rsa 标准命令从私钥中提取公钥。

genrsa 的用法如下，默认是2048：

openssl genrsa [-out filename] [-passout arg] [-des] [-des3] [-idea] [-f4] [-3] [-rand file(s)] [-engine id] [numbits]

	这个命令会生成一个1024/2048位的密钥，包含私钥和公钥。
	
	openssl genrsa -out private.key 1024/2048    (with out password protected)   
	
	openssl genrsa -des3 -out private.key 1024/2048    (password protected)
	

ras 的用法如下：

openssl rsa [-inform PEM|NET|DER] [-outform PEM|NET|DER] [-in filename] [-passin arg] [-out filename] [-passout arg]
       [-sgckey] [-des] [-des3] [-idea] [-text] [-noout] [-modulus] [-check] [-pubin] [-pubout] [-engine id]

	-pubout：根据私钥提取出公钥 
	openssl rsa -in private.key -pubout -out public.key 	
	openssl rsa -noout -text -in public.key


+ **证书请求**

openssl req -new -key private.key -out cert.csr (-config openssl.cnf)

openssl req -new -nodes -key private.key -out cert.csr (-config openssl.cnf)

这个命令将会生成一个证书请求，当然，用到了前面生成的密钥private.key文件
这里将生成一个新的文件cert.csr，即一个证书请求文件，你可以拿着这个文件去数字证书颁发机构（即CA）申请一个数字证书。CA会给你一个新的文件cacert.pem，那才是包含公钥给对方用的数字证书。

+ **查看证书请求**

openssl req -noout -text -in cert.csr


+ **生成证书**

自签名证书，用于自己测试，不需要CA签发
openssl req -new -x509 -key private.key -out cacert.pem -days 1095 (-config openssl.cnf)


+ **CA签发证书：**

CA是专门签发证书的权威机构，处于证书的最顶端。自签是用自己的私钥给证书签名，CA签发则是用CA的私钥给自己的证书签名来保证证书的可靠性，

利用OpenSSL可以自己作为CA进行证书签发，当然这并不权威。

CA签发证书生成的cacert.pem 见“建立CA颁发证书”

 

有了private.key和cacert.pem文件后就可以在自己的程序中使用了，比如做一个加密通讯的服务器

+ **从证书中提取公钥**

openssl x509 -in cacert.pem -pubkey >> public.key

查看证书信息

openssl x509 -noout -text -in cacert.pem

 

+ **建立CA颁发证书**

(1) 环境准备

首先，需要准备一个目录放置CA文件，包括颁发的证书和CRL(Certificate Revoke List)。
mkdir ./CA

 

(2) 创建配置文件

之前生成秘钥和证书可以进行命令行配置，但是在创建CA的时候必须使用配置文件，因为做证书颁发的时候只能使用配置文件。

创建配置文件如下：vi openssl.cnf

	 1     ################################################################ 
	 2     # openssl example configuration file. 
	 3     # This is mostly used for generation of certificate requests. 
	 4     ################################################################# 
	 5     [ ca ] 
	 6     default_ca= CA_default          # The default ca section 
	 7     ################################################################# 
	 8      
	 9     [ CA_default ] 
	10      
	11     dir=/opt/iona/OrbixSSL1.0c/certs # Where everything is kept 
	12     certs=$dir                       # Where the issued certs are kept 
	13     crl_dir= $dir/crl                # Where the issued crl are kept 
	14     database= $dir/index.txt         # database index file 
	15     new_certs_dir= $dir/new_certs    # default place for new certs 
	16     certificate=$dir/CA/OrbixCA      # The CA certificate 
	17     serial= $dir/serial              # The current serial number 
	18     crl= $dir/crl.pem                # The current CRL 
	19     private_key= $dir/CA/OrbixCA.pk  # The private key 
	20     RANDFILE= $dir/.rand             # private random number file 
	21     default_days= 365                # how long to certify for 
	22     default_crl_days= 30             # how long before next CRL 
	23     default_md= md5                  # which message digest to use 
	24     preserve= no                     # keep passed DN ordering 
	25      
	26     # A few different ways of specifying how closely the request should 
	27     # conform to the details of the CA 
	28      
	29     policy= policy_match            # For the CA policy 
	30     
	31     [ policy_match ]  
	32     countryName= match 
	33     stateOrProvinceName= match 
	34     organizationName= match 
	35     organizationalUnitName= optional 
	36     commonName= supplied 
	37     emailAddress= optional 
	38      
	39     # For the `anything' policy 
	40     # At this point in time, you must list all acceptable `object' 
	41     # types 
	42      
	43     [ policy_anything ] 
	44     countryName = optional 
	45     stateOrProvinceName= optional 
	46     localityName= optional 
	47     organizationName = optional 
	48     organizationalUnitName = optional 
	49     commonName= supplied 
	50     emailAddress= optional 
	51      
	52     [ req ] 
	53     default_bits = 1024 
	54     default_keyfile= privkey.pem 
	55     distinguished_name = req_distinguished_name 
	56     attributes = req_attributes 
	57      
	58     [ req_distinguished_name ] 
	59     countryName= Country Name (2 letter code) 
	60     countryName_min= 2 
	61     countryName_max = 2 
	62     stateOrProvinceName= State or Province Name (full name) 
	63     localityName = Locality Name (eg, city) 
	64     organizationName = Organization Name (eg, company) 
	65     organizationalUnitName  = Organizational Unit Name (eg, section) 
	66     commonName = Common Name (eg. YOUR name) 
	67     commonName_max = 64 
	68     emailAddress = Email Address 
	69     emailAddress_max = 40 
	70      
	71     [ req_attributes ] 
	72     challengePassword = A challenge password 
	73     challengePassword_min = 4 
	74     challengePassword_max = 20 
	75     unstructuredName= An optional company name 

 

根据配置文件。创建以下三个文件：

	touch index.txt	
	touch index.txt.attr	
	touch serial 内容为01

(3) 生成CA私钥和证书

	openssl genrsa -out ca.key 1024
	
	openssl req -new -x509 -key ca.key -out ca.pem -days 365 -config openssl.cnf   
	(CA只能自签名证书，注意信息与要颁发的证书信息一致)


(4) 颁发证书

颁发证书就是用CA的秘钥给其他人签名证书，输入需要证书请求，CA的私钥及CA的证书，输出的是签名好的还给用户的证书

这里用户的证书请求信息填写的国家省份等需要与CA配置一致，否则颁发的证书将会无效。
	
	openssl ca -in ../cert.csr -out cacert.pem -cert ca.pem 
	-keyfile ca.key -config openssl.cnf

对比CA颁发的证书提取公钥和私钥导出的公钥是否一致：


同时产生01.pem，这个是CA的备份保留，与生成发送给请求证书的内容一致，serial内序号自动+1。

### 5.DJANGO+SSL

过openssl生成证书

	cd /usr/local/nginx
	mkdir ssl
	cd ssl

创建服务器私钥，长度1024位, des3加密算法的

	openssl genrsa -des3 -out server.key 1024

创建签名请求证书.csr

	openssl req -new -key server.key -out server.csr 

在加载SSL支持的Nginx并使用上述私钥时除去必须的口令

	cp server.key server.key.org
	openssl rsa -in server.key.org -out server.key

标记证书使用上述私钥和CSR 
	
	openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

修改nginx.conf


	 1 http {
	 2     include       mime.types;
	 3     default_type  application/octet-stream;
	 4 
	 5     #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
	 6     #                  '$status $body_bytes_sent "$http_referer" '
	 7     #                  '"$http_user_agent" "$http_x_forwarded_for"';
	 8 
	 9     #access_log  logs/access.log  main;
	10 
	11     sendfile        on;
	12     #tcp_nopush     on;
	13 
	14     #keepalive_timeout  0;
	15     keepalive_timeout  65;
	16 
	17     #gzip  on;
	18 
	19     server {
	20        #listen       80;
	21         listen       443;
	22         server_name  localhost;
	23 
	24         #charset koi8-r;
	25         charset utf-8;
	26 
	27        ssl on;
	28        ssl_certificate /usr/local/nginx/ssl/server.crt;
	29        ssl_certificate_key /usr/local/nginx/ssl/server.key;
	30         #access_log  logs/host.access.log  main;
	31 
	32         location / {
	33             include uwsgi_params;
	34             uwsgi_connect_timeout 30;
	35             uwsgi_pass unix:/home/deepcam/python/cmdb/uwsgi.sock;
	36             index index.html index.htm;
	37             client_max_body_size 75M;
	38         }



参考：

1. [my coding.net](http://zhwa3232.coding.me/baibingqianlan.github.io/)
2. [https://baike.baidu.com/item/TLS](https://baike.baidu.com/item/TLS)
3. [https://baike.baidu.com/item/https/285356?fr=aladdin](https://baike.baidu.com/item/https/285356?fr=aladdin)
4. [OpenSSL - 利用OpenSSL自签证书和CA颁发证书](https://www.cnblogs.com/binchen-china/p/5651142.html)
5. [openssl用法详解](https://www.cnblogs.com/yangxiaolan/p/6256838.html)
6. [http://www.cnblogs.com/weixx1111/p/8985446.html](http://www.cnblogs.com/weixx1111/p/8985446.html)
