#  steam赛博羊毛

![Static Badge](https://img.shields.io/badge/v3.10.*-blue?style=flat&logo=python&logoColor=white&labelColor=gray)

## 介绍

为了薅赛博羊毛，写了这个脚本，目前支持`Egg`、`Cats`、`Banana`。
可以获取到每个游戏的`道具`，然后可以通过市场卖掉。换取少量的`steam`余额。
当然你也可以利用`ASF`去完成道具转移。
PS: 目前需要利用海盗海汉化过的SDA去完成`Steam`的二次登录。
## install

```bash
pip install -r requirements.txt
```

## usage

```bash
# account----password
cp config.example.txt config.txt
python main.py
```

## 支持的游戏
- Egg
- Cats
- Banana

## 需要手动修改的地方

- 如果你的`steam`安装位置位置并不在`C:\Program Files (x86)\Steam`，请修改`main.py`中的`directory_path`变量。

## TODO
- [ ] 修改代码里面写死的参数，改为配置文件
- [ ] 增加定时任务去跑`ASF`的IPC接口（懂得都懂）
- [ ] SDA CODE使用`mafile`自动生成，不借助外部工具