# 🚀 Tech Mining 学习路径（Fei Meng 教授方向）

[![GitHub stars](https://img.shields.io/github/stars/sw20041218/tech-mining-study?style=flat-square)](https://github.com/sw20041218/tech-mining-study/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sw20041218/tech-mining-study?style=flat-square)](https://github.com/sw20041218/tech-mining-study/network)
[![MIT License](https://img.shields.io/github/license/sw20041218/tech-mining-study?style=flat-square)](./LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/sw20041218/tech-mining-study?style=flat-square)](https://github.com/sw20041218/tech-mining-study/commits/main)

> 📚 科技挖掘 & 科学计量学从零到实证研究之路

---

## 🧭 学习路线图

| 周次   | 学习内容                            | 技术工具                                     |
| ------ | ----------------------------------- | -------------------------------------------- |
| Week01 | Python 分词、关键词统计、词云可视化 | `jieba`, `pandas`, `matplotlib`, `wordcloud` |
| Week02 | TF-IDF 与 LDA 主题建模              | `sklearn`, `gensim`, `pyLDAvis`              |
| Week03 | SAO 三元组抽取与语义结构分析        | `spaCy`, `LTP`, `re`                         |
| Week04 | 技术网络与合作图谱分析              | `networkx`, `matplotlib`                     |
| Week05 | 项目实战：技术演化趋势分析          | 综合工具                                     |

---

## 💻 使用技术（Tech Stack）

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python)
![Jieba](https://img.shields.io/badge/中文分词-jieba-lightgrey)
![Gensim](https://img.shields.io/badge/主题模型-gensim-green)
![NetworkX](https://img.shields.io/badge/图分析-networkx-orange)
![SpaCy](https://img.shields.io/badge/自然语言处理-spacy-brightgreen)

---

## 🗂️ 项目结构

```
TechMining-Learning-Path/
├── README.md
├── Week01_PythonBasics/
│   └── keyword_analysis.py
├── Week02_TextMining/
│   └── lda_modeling.py
├── data/
│   └── paper_data.csv
├── assets/
│   └── wordcloud_example.png
```

---

## 📖 使用说明

```bash
# 克隆仓库
git clone git@github.com:sw20041218/tech-mining-study.git

# 进入目录
cd tech-mining-study

# 安装依赖（建议使用虚拟环境）
pip install -r requirements.txt

# 运行 Week01 分词词云代码
python Week01_PythonBasics/keyword_analysis.py
```

---

## 📚 参考资料

- Fei Meng 教授 DBLP 页面: https://dblp.org/pid/78/5984-4.html

### 工具文档：

- [jieba 中文分词](https://github.com/fxsjy/jieba)
- [gensim 文本建模](https://radimrehurek.com/gensim/)
- [networkx 图分析](https://networkx.org/)
- [pyLDAvis 可视化](https://github.com/bmabey/pyLDAvis)

---

## 🤝 贡献指南（Contributing）

欢迎学习者一起参与改进学习路径：

1. Fork 本仓库  
2. 新建分支：`git checkout -b feature/your-topic`  
3. 提交修改：`git commit -m 'add new topic module'`  
4. 推送分支：`git push origin feature/your-topic`  
5. 发起 Pull Request

---

## 📌 License

本项目基于 MIT License 开源，欢迎自由使用和再创作。

---

## ✨ 项目目标

通过实战学习科技文本分析与计量研究方法，构建从文本 → 语义结构 → 图谱 → 趋势分析的完整技术路径，为参与真实科研课题或创新管理研究打好基础。
