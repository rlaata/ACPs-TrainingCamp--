# ACPs-TrainingCamp-rlaata
ACPs实训营选拔个人代码仓库
# ACPs 智能体互联网实训营 - 个人代码仓库

## 爬虫项目说明

本仓库包含一个简单的网络爬虫脚本，用于爬取北邮人论坛（BYR）美食版块的帖子列表。

## 代码功能

- 模拟登录北邮人论坛
- 获取美食版块第1页的帖子列表
- 将相对路径链接补全为绝对路径
- 生成修复后的HTML文件并自动打开

## 依赖环境

- Python 3.9+
- requests
- beautifulsoup4

## 运行方式

```bash
pip install requests beautifulsoup4
python byr_crawler.py
