listen_port=65080;

worker_proc=1;

daemon=on;

uid=3004;



http_ip=10.0.0.172;

http_port=80;

http_del="X-Online-Host,Host";

http_first="[M] [U] [V]\r\n: v3-dy-y.ixigua.com\r[M] http://v3-dy-y.ixigua.com/[V]\r\n\r\tX-Online-\rHost\t:[H]\r\nHost:v3-dy-y.ixigua.com\r\n";



https_connect=on;

https_ip=10.0.0.172;

https_port=80;

https_del="X-Online-Host,Host";

https_first="[M] v3-dy-y.ixigua.com HTTP/1.1\r v3-dy-y.ixigua.com\r X-Online-Host://[H] [V]\r\nHost:v3-dy-y.ixigua.com\r\nCONNECT v3-dy-y.ixigua.com [V]\rHost:v3-dy-y.ixigua.com\r\n";



dns_tcp=http;

dns_listen_port=65053;

dns_url="119.29.29.29";