import os
import pyLDAvis.gensim_models as gensimvis
import pyLDAvis
import gensim
from gensim import corpora
from gensim.models.ldamodel import LdaModel

# Step 1: 加载语料
#data_path = os.path.join("Week02", "data", "corpus.txt")
data_path = 'data/corpus.txt'

with open(data_path, "r", encoding="utf-8") as f:
    texts = [line.strip().split() for line in f if line.strip()]

# Step 2: 构建词典和语料库
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Step 3: 训练 LDA 模型
lda_model = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=5,
    random_state=42,
    update_every=1,
    chunksize=100,
    passes=10,
    alpha='auto'
)

# Step 4: 输出每个主题的关键词
for i, topic in lda_model.print_topics(num_words=10):
    print(f"主题 {i}: {topic}")

# Step 5: 可视化
vis_data = gensimvis.prepare(lda_model, corpus, dictionary)
#pyLDAvis.save_html(vis_data, os.path.join("Week02", "lda_vis.html"))
pyLDAvis.save_html(vis_data, "lda_vis.html")
print("✅ 可视化已生成：Week02/lda_vis.html")

