# RLHF 标注工具-简化版
[English](README_en.md)

是[RLHF-Label-Tool](https://github.com/SupritYoung/RLHF-Label-Tool)的一个简化版。RLHF-Label-Tool是一个偏好数据集标注工具。

**项目截图：**
<img width="1206" alt="image" src="project.PNG">


## 安装依赖
- Python 3.x
- 安装依赖包：`pip install -r requirements.txt`

## 快速开始
1. 待标注的数据集文件是[input_file.jsonl](data/input_file.jsonl)。里面的数据如下：
```
{"question": "How are you doing?", "response": ["I am good", "I am bad","Terrible","Mind your own business"],"reference":"Normally the answer should be nice."}
{"question": "who are you?", "response": ["LLM", "Apple","Banana","Sea"], "reference":"This chatbot should be a robot or something."}
```
请按上述格式将此文件替换成你的待标注数据集，文件位置和命名保持不变。

2. 当前目录下，运行下面命令
```bash
streamlit run app.py --server.port 8080
```
3. 每条数据只能选1个Accept和1个Reject，假如全部选dismiss，这条数据会被丢弃，除非你再改回来。
4. 点`Save`，结果保存为`/data/output_result.jsonl`。
## 贡献与许可

致谢：https://github.com/SupritYoung/RLHF-Label-Tool

本项目基于 MIT License 进行发布和授权。
