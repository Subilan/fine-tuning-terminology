import json
import datetime

with open('fine_tuned_models.json') as fts:
    data = json.load(fts)
    translator = data['translator']
    teacher = data['teacher']
    result = []
    for t in translator:
        time = datetime.datetime.fromtimestamp(t['finished_at'])
        print(f"## on {time.strftime('%Y.%m.%d')}")
        print(f"- Job ID: `{t['id']:s}`")
        print(f"- 继承自: `{t['model']:s}`")
        print(f"- 产出模型: `{t['fine_tuned_model']:s}`")
        print(f"- 训练数据集: `{t['training_file']:s}`")
        print(f"- 消耗Token: {t['trained_tokens']:d}")
        print(f"- 预估消耗费用: ${t['trained_tokens'] / 1000 * 0.008:.2f}")