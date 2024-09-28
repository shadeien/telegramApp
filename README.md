# telegramApp
telegram mini app init guide


## 创建机器人

- 在telegram中搜索BotFather, 并且打开聊天窗口

![](https://github.com/shadeien/telegramApp/blob/main/img/botfather.png?raw=true)  
- 输入/newbot指令创建机器人
	- 输入[机器人名称]
	- 输入[机器人ID], 必须bot结尾
	- 创建成功后会有一个提示，记录提供的token
![](https://github.com/shadeien/telegramApp/blob/main/img/createbot.png?raw=true) 
- 我们可以通过账号搜索
![](https://github.com/shadeien/telegramApp/blob/main/img/search.png?raw=true) 

## 创建app

- 在telegram中搜索BotFather, 并且打开聊天窗口
- 输入/newapp指令创建机器人
	- 选择一个机器人, 可以直接输入上面创建的'@[机器人ID]', 或者在输入框下面的按钮选择
	- 输入web app的名称
	- 上传一张640*360的图片, 作为telegram加载app时候的loading 
	- 上传一个demo的git图片演示介绍, 可以输入/empty跳过
	- 输入web app的url, 我们部署的前端服务链接
- app创建成功

- 输入 /setmenubutton, 可以对机器人进行menu button设置
![](https://github.com/shadeien/telegramApp/blob/main/img/setmenubutton.png?raw=true) 



- [非必须]有需要修改的app信息的时候输入 /editapp, 按照提示修改
- [非必须]输入 /myapps, 可以查询我们创建的app