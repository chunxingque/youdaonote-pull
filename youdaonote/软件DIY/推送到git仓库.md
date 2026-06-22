使用 SSH 认证（更安全）

1.  生成 SSH key：

    `ssh-keygen -t ed25519 -C "your_email@example.com"`

    一路回车即可，像这样：

        Enter  file  in  which  to  save  the  key:  [Enter]  
        Enter  passphrase  (empty  for  no  passphrase):  [Enter]

    生成后再确认：

    `ls ~/.ssh`

2.  将公钥复制到 GitHub：

    `cat ~/.ssh/id_ed25519.pub`

    然后复制输出内容，到 GitHub\
    → **Settings → SSH and GPG keys → New SSH key**

3.  git init

    git add --all

    git commit -m "first commit"

4.  修改远程仓库地址为 SSH：
    首次需要
    git remote add origin <https://github.com/redstoneleo/pycnblogs.git>
    如果是修改可用这个：
    `git remote set-url origin git@github.com:redstoneleo/LYYDownloaderServer.git`

5.  再次推送：

    `git push origin master`
    强制覆盖 GitHub 仓库
    git push -u origin master --force

