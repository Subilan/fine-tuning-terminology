import json

fine_tuned_data = json.load(open('fine_tuned_models.json'))
teacher_models = [x['fine_tuned_model'] for x in fine_tuned_data['teacher']]
translator_models = [x['fine_tuned_model'] for x in fine_tuned_data['translator']]

latest_teacher_model = teacher_models[len(teacher_models) - 1]
latest_translator_model = translator_models[len(translator_models) - 1]