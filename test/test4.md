## SSL简介

**SSL**[](http://en.wikipedia.org/wiki/Transport_Layer_Security)

**OpenSSL**

证书标准

**X.509**

### 公钥密码体制

公钥密码体制分为三个部分，公钥、私钥、加密解密算法，它的加密解密过程如下：

- 加密：通过加密算法和公钥对内容(或者说明文)进行加密，得到密文。加密过程需要用到公钥。 

- 解密：通过解密算法和私钥对密文进行解密，得到明文。解密过程需要用到解密算法和私钥。注意，由公钥加密的内容，只能由私钥进行解密，也就是说，由公钥加密的内容，如果不知道私钥，是无法解密的。

公钥密码体制的公钥和算法都是公开的(这是为什么叫公钥密码体制的原因)，私钥是保密的。大家都以使用公钥进行加密，但是只有私钥的持有者才能解密。在实际的使用中，有需要的人会生成一对公钥和私钥，把公钥发布出去给别人使用，自己保留私钥。

## **ssl安全协议原理**

SSL可以说是非对称加密与对称加密的完美结合。非对称用于传输对称加密的Key，内容信息用对称加密技术处理！

1. 客户端向一个需要https访问的网站发起请求。

2. 服务器将证书发送给客户端进行校验。证书里面包含了其公钥。这里要特别说一下客户端到底 如何来校验对方发过来的数字证书是否有效。

1. 首先在本地电脑寻找是否有这个服务器证书上的ca机构的根证书。如果有继续下一步，如果没有弹出警告。

1. 使用ca机构根证书的公钥对服务器证书的指纹和指纹算法进行解密。

1. 得到指纹算法之后，拿着这个指纹算法对服务器证书的摘要进行计算得到指纹。

1. 将计算出的指纹和从服务器证书中解密出的指纹对比看是否一样如果一样则通过认证。

1. 

3. 校验成功之后，客户端会生成一个随机串然后使用服务器证书的公钥进行加密之后发送给服务器。

4. 服务器通过使用自己的私钥解密得到这个随机值。

5. 服务器从此开始使用这个随机值进行对称加密开始和客户端进行通信。

6. 客户端拿到值用对称加密方式 使用随机值进行解密。

为什么不一直使用非对称进行加密，而是在类似握手之后开始使用对称加密算法进行https通信：

非对称加密的消耗和所需的计算以及时间远比对称加密消耗要大，所以在握手和认证之后，服务器和客户端就开始按照约定的随机串，对后续的数据传输进行加密。

## **SSL证书**

### CA(Certificate Authority)

#### CA概念

CA(Certificate Authority)是证书的签发机构，它是负责管理和签发证书的第三方机构，是受到广泛信任的机构。一般在我们的电脑中，浏览器里，或者手机里都会内置一批这样的受信机构的根证书。其实证书谁都可以签，你也可以自己给自己签发证书，但是由于你自己并不是被广泛信任的机构，所以你自己签发的证书并没有什么用。公网也不会信任你的证书。

首先要有一个CA根证书，然后用CA根证书来签发用户证书。

用户进行证书申请：一般先生成一个私钥(server.key)，然后用私钥生成证书请求(server.csr)(证书请求里应含有公钥信息)，再利用证书服务器的CA根证书来签发证书。

特别说明:

（1）自签名证书(一般用于顶级证书、根证书): 

（2）根证书：根证书是CA认证中心给自己颁发的证书,是信任链的起始点。任何安装CA根证书的服务器都意味着对这个CA认证中心是信任的。

数字证书则是由证书认证机构（CA）对证书申请者真实身份验证之后，用CA的根证书对申请人的一些基本信息以及申请人的公钥进行签名（相当于加盖发证书机构的公章）后形成的一个数字文件。数字证书包含证书中所标识的实体的公钥（就是说你的证书里有你的公钥），由于证书将公钥与特定的个人匹配，并且该证书的真实性由颁发机构保证（就是说可以让大家相信你的证书是真的），因此，数字证书为如何找到用户的公钥并知道它是否有效这一问题提供了解决方案。

#### CA证书信任链

比如我是CA机构我签发了一封证书 我这份证书是信任B证书的另外B证书又信任了其他的C证书......那么这条链条下去的都可以信任。所以一旦CA机构的根证书不可信了，那么所有由他签发出来的证书将全部变得不可信，后果很严重。

![](https://note.youdao.com/yws/res/91019/WEBRESOURCEf0cc50d1f312429b0c8d97f340cc3603)

#### **crt**



证书的发布机构 

证书的有效期 

公钥 

证书所有者（Subject） 

签名所使用的算法 

指纹以及指纹算法

Issuer (证书的发布机构):指出是什么机构发布的这个证书，也就是指明这个证书是哪个公司创建的(只是创建证书，不是指证书的使用者)。对于上面的这个证书来说，就是指"SecureTrust CA"这个机构。



◆Valid from , Valid to (证书的有效期):也就是证书的有效时间，或者说证书的使用期限。 过了有效期限，证书就会作废，不能使用了。



◆Public key (公钥):这个我们在前面介绍公钥密码体制时介绍过，公钥是用来对消息进行加密的，第2章的例子中经常用到的。这个数字证书的公钥是2048位的，它的值可以在图的中间的那个对话框中看得到，是很长的一串数字。



◆Subject (主题):这个证书是发布给谁的，或者说证书的所有者，一般是某个人或者某个公司名称、机构的名称、公司网站的网址等。 对于这里的证书来说，证书的所有者是Trustwave这个公司。



◆Signature algorithm (签名所使用的算法):就是指的这个数字证书的数字签名所使用的加密算法，这样就可以使用证书发布机构的证书里面的公钥，根据这个算法对指纹进行解密。指纹的加密结果就是数字签名。



◆Thumbprint, Thumbprint algorithm (指纹以及指纹算法): 这个是用来保证证书的完整性的，也就是说确保证书没有被修改过。 其原理就是在发布证书时，发布者根据指纹算法(一个hash算法)计算整个证书的hash值(指纹)并和证书放在一起，使用者在打开证书时，自己也根据指纹算法计算一下证书的hash值(指纹)，如果和刚开始的值对得上，就说明证书没有被修改过，因为证书的内容被修改后，根据证书的内容计算的出的hash值(指纹)是会变化的。 注意，这个指纹会使用"CA"证书机构的私钥用签名算法(Signature algorithm)加密后和证书放在一起。





### 编码格式

同样的X.509证书,可能有不同的编码格式,目前有以下两种编码格式.

**PEM**

查看PEM格式证书的信息:

Apache和*NIX服务器偏向于使用这种编码格式.

**DER**

查看DER格式证书的信息:

Java和Windows服务器偏向于使用这种编码格式.

### 证书扩展名

- **CRT**

- **CER**

- **KEY**

- **CSR**

- **PFX/P12**

- **JKS**

- DER： DER = DER扩展用于二进制DER编码证书。这些文件也可能承载CER或CRT扩展。

### csr证书签名请求

Certificate Signing Request,即证书签名请求,这个并不是证书,而是向权威证书颁发机构获得签名证书的申请,其核心内容是一个公钥(当然还附带了一些别的信息),在生成这个申请的时候,同时也会生成一个私钥,私钥要自己保管好.

生成秘钥后，就可以利用秘钥生成csr

```
#key
openssl genrsa -out ca.key 2048
#csr
openssl req -new -key ca.key -out ca.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:CN
State or Province Name (full name) []:Guangdong
Locality Name (eg, city) [Default City]:Shenzhen
Organization Name (eg, company) [Default Company Ltd]:SY
Organizational Unit Name (eg, section) []:SY
Common Name (eg, your name or your server's hostname) []:192.168.88.153
Email Address []:1450469526@qq.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:SY
```

**CN(Common Name)**

在生成CSR时，公用名（Common Name）是必须填写的，可以填写域名或其他名称

申请CA根证书：可以填写组织的名称或其他名字

申请CA用户证书：可以填写Common Name是网站域名全称，包括您的主机名+域名，比如：www.trustauth.cn、trustauth.cn和mail.trustauth.cn虽然有相同的主域名trustauth.cn，但它们是3个完全不同的Common Name。您的公用名（Common Name）必须与您要用服务器证书的主机的全名完全相同，trustauth.cn的证书是不能用在host.trustauth.cn上的。如果申请的是通配符证书证书，Common Name请用*.trustauth.cn 。如果申请的是多域名证书，只需用从中选出一个最主要的域名，作为Common Name来生成CSR就可以了。其他的域名可以通过订单页面提交

**O(Organization)**

Organization（组织名）是必须填写的，如果申请的是OV、EV型证书，组织名称必须严格和企业在政府登记名称一致，一般需要和营业执照上的名称完全一致。不可以使用缩写或者商标。如果需要使用英文名称，需要有DUNS编码或者律师信证明。

**OU(Organization Unit)**

OU单位部门，这里一般没有太多限制，可以直接填写IT DEPT等皆可。

**C(City)**

City是指申请单位所在的城市。

**ST(State/Province)**

ST是指申请单位所在的省份。

**C(Country Name）**

C是指国家名称，这里用的是两位大写的国家代码，中国是CN。

## ssl证书生成

### OpenSSL 生成SSL证书的流程

#### **openssl中后缀名的文件**

.key格式：私有的密钥

.csr格式：证书签名请求（证书请求文件），含有公钥信息，certificate signing request的缩写

.crt格式：证书文件，certificate的缩写

.crl格式：证书吊销列表，Certificate Revocation List的缩写

.pem格式：用于导出，导入证书时候的证书的格式，有证书开头，结尾的格式

#### **CA根证书生成（自签名证书）**

方法一：

生成CA私钥（.key）–>生成CA证书签名请求（.csr）–>自签名得到根证书（.crt）（CA给自已颁发的证书）。

```
# Generate CA private key 
  openssl genrsa -out ca.key 2048
# Generate CSR 
  openssl req -new -key ca.key -out ca.csr
# Generate Self Signed certificate（CA 根证书）
  openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt    


```

在实际的软件开发工作中，往往服务器就采用这种自签名的方式，因为毕竟找第三方签名机构是要给钱的，也是需要花时间的。

方法二：

生成CA私钥（.key）–>自签名得到根证书（.crt）

⽣成根证书私钥

```
openssl genrsa -out ca.key 2048
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt
```

#### **CA用户证书生成**

生成私钥（.key）–>生成证书请求（.csr）–>用CA根证书签名和ca的秘钥(.key)得到证书（.crt）

**服务器端用户证书：**

```
# private key
 $openssl genrsa -des3 -out server.key 1024 
# generate csr
 $openssl req -new -key server.key -out server.csr
# generate certificate
 $openssl ca -in server.csr -out server.crt -cert ca.crt -keyfile ca.key
```

**客户端用户证书**

```
$openssl genrsa -des3 -out client.key 1024 
$openssl req -new -key client.key -out client.csr
$openssl ca -in client.csr -out client.crt -cert ca.crt -keyfile ca.key
```

**生成pem格式证书：**

有时需要用到pem格式的证书，可以用以下方式合并证书文件（crt）和私钥文件（key）来生成

```
$cat client.crt client.key> client.pem 
$cat server.crt server.key > server.pem
```

**结果：**

服务端证书：ca.crt, server.key, server.crt, server.pem

客户端证书：ca.crt, client.key, client.crt, client.pem

#### nginx启用https

4.1配置nginx，开启https

开启https请求

进入nginx目录，编辑nginx.conf – vim nginx.conf

找到HTTPS server

ssl_certificate 服务端crt证书路径

ssl_certificatie_key 服务端私钥路径

![](https://note.youdao.com/yws/res/91070/WEBRESOURCEc57b56860a88ee25d18d2c84e8ec2af3)

配置完以后 启动或者容器一下nginx

启动：在nginx目录执行 

```
./sbin/nginx
```

重启：在nginx目录执行 

```
./sbin/nginx -s reload
```

在浏览器访问是成功的，因为我们是自签证书，因此显示不安全

![](https://note.youdao.com/yws/res/91075/WEBRESOURCE2db68e5ff3590e17d2fa6fc253a59f7d)

#### nginx启用客户端认证(双向认证)

vim nginx.conf继续编辑nginx.conf

ssl_client_certificate 指定客户端认证时使⽤的根证书路径，⽤来验证客户端证书的正确性，我们使用的自签ca证书签发的客户端证书，因此使用ca.crt

ssl_verify_client on 为开启客户端校验

![](https://note.youdao.com/yws/res/91080/WEBRESOURCE188b14fdf919f4e07c76ce56294499d0)

配置完成后重启nginx ./sbin/nginx -s reload

为了方便测试。我们直接使用curl 命令进行测试

```
curl 
```

ip为访问的具体ip地址

-k编码忽略服务端证书的校验，因为我们这里服务端证书也是自签的，所以要加上-k

不加-k,会有异常提示

![](https://note.youdao.com/yws/res/91084/WEBRESOURCEdcd9941de9f38de94f0fb8f9d7f1fac0)

提示需要携带客户端的证书，说明我们配置的客户端认证已经生效了

```
curl --cert client.crt --key client.key 
```

![](https://note.youdao.com/yws/res/91086/WEBRESOURCE68fb2b8f5b0f47b93dcf909b5b0b8a1b)

### OpenSSL 生成SSL证书

x509证书一般会用到三类文，key，csr，crt。

Key 是私用密钥，通常是rsa算法。

csr 是证书请求文件，用于申请证书。在制作csr文件的时，必须使用自己的私钥来签署申，还可以设定一个密钥。

crt是CA认证后的证书文，签署人用自己的key给你签署的凭证。 

1.key私钥的生成 

```
openssl genrsa -des3 -out server.key 2048 
```

- -des3:生成的密钥使用des3方式进行加密。

- -out 

- 1024为要生成的私钥的长度。

这样是生成rsa私钥，des3算法，openssl格式，2048位强度。server.key是密钥文件名。为了生成这样的密钥，需要一个至少四位的密码。可以通过以下方法生成没有密码的key，如果是nginx的话，需要设置为无密码的

```
openssl rsa -in server.key -out server.key 
```

 server.key就是没有密码的版本了。  

2. 生成CA的crt证书

```
openssl req -new -x509 -key server.key -out ca.crt -days 3650 
```

生成的ca.crt文件是用来签署下面的server.csr文件。 

 

3. 待签名的csr文件的生成方法

```
openssl req -new -key server.key -out server.csr 
```

需要依次输入国家，地区，组织，email。最重要的是有一个common name，可以写你的名字或者域名。如果为了https申请，这个必须和域名吻合，否则会引发浏览器警报。生成的csr文件交给CA签名后形成服务端自己的证书。 

 

4. crt生成方法

CSR文件必须有CA的签名才可形成证书，可将此文件发送到verisign等地方由它验证，要交一大笔钱，何不自己做CA呢。

```
openssl x509 -req -days 3650 -in server.csr -CA ca.crt -CAkey server.key -CAcreateserial -out server.crt
```

输入key的密钥后，完成证书生成。-CA选项指明用于被签名的csr证书，-CAkey选项指明用于签名的密钥，-CAserial指明序列号文件，而-CAcreateserial指明文件不存在时自动生成。

最后生成了私用密钥：server.key和自己认证的SSL证书：server.crt

证书合并：

```
cat server.key server.crt > server.pem
```

方法二

1.创建ＣＡ

创建ＣＡ的私钥

```
[root@k8s-node1 ssl]# openssl genrsa -des3 -out rootCA.key 4096 

```

创建ＣＡ的自签证书

```
[root@k8s-node1 ssl]# openssl req -x509 -new -nodes -sha256 -days 3650 -key rootCA.key -out rootCA.crt                                                 
Enter pass phrase for rootCA.key:                                                                                                                      
You are about to be asked to enter information that will be incorporated                                                                               
into your certificate request.                                                                                                                         
What you are about to enter is what is called a Distinguished Name or a DN.                                                                            
There are quite a few fields but you can leave some blank                                                                                              
For some fields there will be a default value,                                                                                                         
If you enter '.', the field will be left blank.                                                                                                        
-----                                                                                                                                                  
Country Name (2 letter code) [XX]:CN                                                                                                                   
State or Province Name (full name) []:guangdong                                                                                                        
Locality Name (eg, city) [Default City]:shenzhen                                                                                                       
Organization Name (eg, company) [Default Company Ltd]:sy                                                                                               
Organizational Unit Name (eg, section) []:sy                                                                                                           
Common Name (eg, your name or your server's hostname) []:196.168.137.139                                                                               
Email Address []:sy 
```

2.签发证书

生成证书的私钥

```
openssl genrsa -out server.key  4096
```

生成待签名的csr证书签名请求文件

```
[root@k8s-node1 ssl]# openssl req -new -key server.key -out server.csr                                                                                 
You are about to be asked to enter information that will be incorporated                                                                               
into your certificate request.                                                                                                                         
What you are about to enter is what is called a Distinguished Name or a DN.                                                                            
There are quite a few fields but you can leave some blank                                                                                              
For some fields there will be a default value,                                                                                                         
If you enter '.', the field will be left blank.                                                                                                        
-----                                                                                                                                                  
Country Name (2 letter code) [XX]:CN                                                                                                                   
State or Province Name (full name) []:guangdong                                                                                                        
Locality Name (eg, city) [Default City]:shenzheng                                                                                                      
Organization Name (eg, company) [Default Company Ltd]:sy                                                                                               
Organizational Unit Name (eg, section) []:sy                                                                                                           
Common Name (eg, your name or your server's hostname) []:192.168.137.139                                                                               
Email Address []:sy                                                                                                                                    
                                                                                                                                                       
Please enter the following 'extra' attributes                                                                                                          
to be sent with your certificate request                                                                                                               
A challenge password []:123456                                                                                                                         
An optional company name []:sy     
```

使用CＡ的密钥key和ca证书crt进行对csr文件进行签名

```
[root@k8s-node1 ssl]# openssl x509 -req -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -days 365 -sha256 -in server.csr  -out server.crt             
Signature ok                                                                                                                                           
subject=/C=CN/ST=guangdong/L=shenzheng/O=sy/OU=sy/CN=192.168.137.139/emailAddress=sy                                                                   
Getting CA Private Key                                                                                                                                 
Enter pass phrase for rootCA.key:              
```

### **OpenSSL **

1. 首先创建SSL证书私钥，期间需要输入两次用户名和密码，生成文件为blog.key，用于ca签名的秘钥

```
openssl genrsa -des3 -out blog.key 2048
```



2. 利用私钥生成一个不需要输入密码的密钥文件，生成文件为blog_nopass.key，用于生成csr的秘钥

```
openssl rsa -in blog.key -out blog_nopass.key
```



3. 创建SSL crt证书签名请求文件，生成SSL证书时需要使用到，用于生成ssl证书blog.csr

在生成过程中，我们需要输入一些信息，需要注意的是Common Name需要和网站域名一致；

```
openssl req -new -key blog.key -out blog.csr
```



4. 生成SSL证书，有效期为365天，生成文件为blog.crt；



```
openssl x509 -req -days 365 -in blog.csr -signkey blog.key -out blog.crt
```

5.配置nginx

```
server {
    listen       80; # 同时支持HTTP
    listen       443 ssl; # 添加HTTPS支持
    server_name  engureguo.com;
  
    #SSL配置
    ssl_certificate      /usr/share/nginx/html/ssl/blog.crt; # 配置证书
    ssl_certificate_key  /usr/share/nginx/html/ssl/blog_nopass.key; # 配置证书私钥
    ssl_protocols        TLSv1 TLSv1.1 TLSv1.2; # 配置SSL协议版本
    ssl_ciphers          ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE; # 配置SSL加密算法
    ssl_prefer_server_ciphers  on; # 优先采取服务器算法
    ssl_session_cache    shared:SSL:10m; # 配置共享会话缓存大小
    ssl_session_timeout  10m; # 配置会话超时时间
 
    location / {
        root   /usr/share/nginx/html/www;
        index  index.html index.htm;
    }
 
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

ssl_certificate 为ca签发的crt证书，发送给客户端加密生成随机秘钥。

ssl_certificate_key 为生成的csr的秘钥，用于解密crt证书生成的秘钥，获取到随机秘钥。

### keytool生成证书

#### key用法

生成证书

```
keytool -genkey -alias server_cert -keypass 123456 -keyalg RSA -keysize 1024 -validity 365 -keystore  server.keystore -storepass 123456
```

```

What is your first and last name?
  [guanlan]:  
What is the name of your organizational unit?
  [guanlan]:  
What is the name of your organization?
  [Qs]:  
What is the name of your City or Locality?
  [shenzhen]:  
What is the name of your State or Province?
  [GuangDong]:  
What is the two-letter country code for this unit?
  [10.5.44.3]:  
Is CN=guanlan, OU=guanlan, O=Qs, L=shenzhen, ST=GuangDong, C=10.5.44.3 correct?
  [no]:  yes
```

查看证书详情

```
keytool -list -v -keystore 
```

 keystore文件生成cer文件：

```
keytool -export 
```

打印证书信息：

```
keytool -list -rfc -keystore server.keystore  -storepass 123456 | tee server.txt
```

### keystore 生成nginx ssl证书

1.通过jdk工具生成keystore（jks）文件

设置自签口令

```
keytool -genkey -alias server_cert -keypass 123456 -keyalg RSA -keysize 1024 -validity 365 -keystore keystore.jks -storepass 123456
```

2.转换为p12

```
keytool -importkeystore -srckeystore keystore.jks -destkeystore keystore.p12 -deststoretype PKCS12
```

输入新密钥库口令（至少6位）

源秘钥库口令若未设置为空，直接回车

输入自签口令（至少6位）

3.使用openssl命令导出.crt

```
openssl pkcs12 -in keystore.p12 -nokeys -out key_store.crt
```

4.使用openssl命令导出.key

```
openssl pkcs12 -in keystore.p12 -nocerts -nodes -out my_store.key
```

5.使用openssl导出.cer

```
openssl x509 -in key_store.crt -out my_key_store.cer -outform der
```

### cfssl

```
wget https://github.com/cloudflare/cfssl/releases/download/v1.6.4/cfssl_1.6.4_linux_amd64
wget https://github.com/cloudflare/cfssl/releases/download/v1.6.4/cfssljson_1.6.4_linux_amd64
wget https://github.com/cloudflare/cfssl/releases/download/v1.6.4/cfssl-certinfo_1.6.4_linux_amd64
chmod +x cfssl*
cp -p cfssl_1.6.4_linux_amd64 /usr/bin/cfssl 
cp -p cfssljson_1.6.4_linux_amd64 /usr/bin/cfssljson
cp -p cfssl-certinfo_1.6.4_linux_amd64 /usr/bin/cfssl-certinfo
```

#### CA根证书csr生成

根证书证书签名请求

```
cfssl print-defaults csr > json/ca-csr.json
```

默认如下：

```
{
    "CN": "example.net",
    "hosts": [
        "example.net",
        "www.example.net"
    ],
    "key": {
        "algo": "ecdsa",
        "size": 256
    },
    "names": [
        {
            "C": "US",
            "ST": "CA",
            "L": "San Francisco"
        }
    ]
}
```

可修改如下：

```
{
    "CN": "szzsmw.com",
    "hosts": [
        "szzsmw.com"
    ],
    "key": {
        "algo": "ecdsa",
        "size": 256
    },
    "names": [
        {
            "C": "CN",
            "ST": "CA",
            "L": "Beijing"
        }
    ]
}
```

一般的数字证书产品的主题通常含有如下字段：

CN

CN: 公用名称 (Common Name) 简称，

对于 SSL 证书，一般为网站域名或IP地址；

而对于代码签名证书则为申请单位名称；

而对于客户端证书则为证书申请者的姓名；

hosts

hosts可以指定多个（泛）域名以及多个IP地址

key

指定了加密算法，一般使用rsa（size：2048）

names 字段

单位名称 (Organization Name) ：简称：O 字段

对于 SSL 证书，一般为网站域名；

而对于代码签名证书则为申请单位名称；

而对于客户端单位证书则为证书申请者所在单位名称；

证书申请单位所在地：

所在城市 (Locality) 简称：L 字段

所在省份 (State/Provice) 简称：S 字段

所在国家 (Country) 简称：C 字段，只能是国家字母缩写，如中国：CN

其他一些字段：

电子邮件 (Email) 简称：E 字段

多个姓名字段 简称：G 字段

介绍：Description 字段

电话号码：Phone 字段，格式要求 + 国家区号 城市区号 电话号码，如： +86 732 88888888

地址：STREET 字段

邮政编码：PostalCode 字段

显示其他内容 简称：OU 字段

#### CA根证书生成

```
cfssl gencert -initca json/ca-csr.json | cfssljson -bare ca 
```

执行后生成几个文件

生成的文件中有下面三个后面会用到:



ca-key.pem: CA 证书密钥

ca.pem: CA 证书

ca.csr

#### CA签发配置生成

生成默认签发配置文件，使用CA 证书来签发其它证书时所需要的配置

```
cfssl print-defaults config > json/ca-config.json
```

```
{
    "signing": {
        "default": {
            "expiry": "168h"
        },
        "profiles": {
            "www": {
                "expiry": "8760h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "server auth"
                ]
            }
        }
    }
}
```

- signing：签署配置

- default：默认的配置

- expiry 过期时间

- default.expiry：默认签署其他证书过期时间

- profiles：配置文件，可以配置多个不同的证书配置

- www：定义的一个profile，可以使用命令生成这个的证书

- usages 用途

过期时间可以改为439200h  （50年） 或 263520h (30年)

#### 网站证书csr

网站证书签名请求生成

```
cfssl print-defaults csr > json/www-csr.json
```

#### 网站签发证书

```
cfssl gencert \
  -ca=ca.pem \
  -ca-key=ca-key.pem \
  -config=json/ca-config.json \
  -profile=www \
  json/www-csr.json | cfssljson -bare www
```

生成下面两个重要的文件:



www-key.pem: www 密钥。

www.pem: www 证书。

查看证书

```
openssl x509  -noout -text -in  www.pem
```

配置nginx

```
ssl_certificate /xxx/keys/www.pem;
ssl_certificate_key /xxx/keys/www-key.pem;
ssl_ciphers HIGH:!aNULL:!MD5;
ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 5m;
```

# 证书合并

```
cat www.pem ca.pem > www.crt
cp www-key.pem www.key
```

```
# nginx 部署
    ssl_certificate      self.crt;
    ssl_certificate_key  self.key;
    ssl_session_timeout  5m;
    ssl_protocols  TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers EECDH+AES:EECDH+CHACHA20;
# apache 参考
<VirtualHost :9443>
DocumentRoot "/myproject"  #项目目录
SSLEngine on
SSLProtocol all -SSLv2 –SSLv3 
SSLHonorCipherOrder On
SSLCipherSuite ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256
SSLCertificateFile  /xx/xx/self.pem
SSLCertificateKeyFile /xx/xx/self.key
SSLCertificateChainFile /xx/xx/ca.pem
</VirtualHost>
```