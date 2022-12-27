# Redis_Unauthorized_Exp

Redis未授权写入ssh公钥

![image](https://github.com/The-poison/Redis_Unauthorized_Exp/blob/main/images/image-20221227133653983.png)

Usage: python redis_unauthorized.py target_ip target_port public_key.txt
Usage: python redis_unauthorized.py 192.168.1.110 6379 public_key.txt



生成ssh公私钥

![image](https://github.com/The-poison/Redis_Unauthorized_Exp/blob/main/images/image-20221227132508725.png)

将公钥复制到脚本文件目录下

![image](https://github.com/The-poison/Redis_Unauthorized_Exp/blob/main/images/image-20221227132746033.png)

执行脚本文件

Usage: python redis_unauthorized.py target_ip target_port public_key.txt
Usage: python redis_unauthorized.py 192.168.1.110 6379 public_key.txt

![image](https://github.com/The-poison/Redis_Unauthorized_Exp/blob/main/images/image-20221227132925180.png)

写入成功，使用工具进行连接即可

![image](https://github.com/The-poison/Redis_Unauthorized_Exp/blob/main/images/image-20221227133033032.png)
