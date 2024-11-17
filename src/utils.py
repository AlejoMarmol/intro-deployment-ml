from sklearn.pipeline import Pipeline
from joblib import dump
import seaborn as sns
import matplotlib.pyplot as plt

def update_model(model: Pipeline) -> None:
    dump(model, 'model/model.pkl')


def save_simple_metrics_report(train_score, test_score, validation_score, model) -> None:
    with open('report.txt', 'w') as report_file:

        report_file.write('# Model Pipeline Description'+'\n')

        for key, value in model.named_steps.items():
            report_file.write(f'### {key}:{value.__repr__()}'+'\n')

        report_file.write(f'### Train Score: {train_score}'+'\n')
        report_file.write(f'### Test Score: {test_score}'+'\n')
        report_file.write(f'### Validation Score: {validation_score}'+'\n')

def get_model_performance_test_set(y_real, y_pred) -> None:
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(8)
    sns.regplot(x = y_pred, y = y_real, ax = ax)
    ax.set_xlabel('Predicted worldwide gross')
    ax.set_ylabel('Real worldwide gross')
    ax.set_title('Behavior of model prediction')
    fig.savefig('prediction_behavior.png')
