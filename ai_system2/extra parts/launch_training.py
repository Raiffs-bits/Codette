import sagemaker
import boto3
from sagemaker.huggingface import HuggingFace

try:
    role = sagemaker.get_execution_role()
except ValueError:
    iam = boto3.client('iam')
    role = iam.get_role(RoleName='sagemaker_execution_role')['Role']['Arn']

hyperparameters = {
    'model_name_or_path': 'Raiff1982/deepercodette',
    'output_dir': '/opt/ml/model',
    'num_train_epochs': 3,
    'per_device_train_batch_size': 16,
    'per_device_eval_batch_size': 16,
    'warmup_steps': 500,
    'weight_decay': 0.01,
    'logging_dir': '/opt/ml/logs',
    'logging_steps': 10
}

# git configuration to download our fine-tuning script
git_config = {'repo': 'https://github.com/huggingface/transformers.git', 'branch': 'v4.37.0'}

# creates Hugging Face estimator
huggingface_estimator = HuggingFace(
    entry_point='train.py',
    source_dir='./path/to/script',
    instance_type='ml.p3.2xlarge',
    instance_count=1,
    role=role,
    git_config=git_config,
    transformers_version='4.37.0',
    pytorch_version='2.1.0',
    py_version='py310',
    hyperparameters=hyperparameters
)

# starting the train job
huggingface_estimator.fit()