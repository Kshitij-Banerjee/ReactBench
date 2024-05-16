import sys
import os
import yaml
import secrets
import string

from setup.copy_directory import copy_directory
from setup.find_files import find_files

def load_yaml_file(directory):
    yaml_file_path = os.path.join('Evals', directory, 'test_config.yaml')
    with open(yaml_file_path, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def copy_test_suite(test_id):
		copy_directory('../TestSuite', './TestRuns/TestRun_' + test_id)

def run_completions(test_id):
    evals_directory = os.path.join('.', 'TestRuns', 'TestRun_' + test_id, 'Evals')
    gt_files = find_files(evals_directory, '*_GroundTruth.ts')
    print(gt_files)
    print("Running completions...")

def run_metrics_evaluation():
    print("Running metrics evaluation...")

def build_report():
    print("Building report...")

def generate_test_id(length=6):
    alphanumeric = string.ascii_letters + string.digits
    test_id = ''.join(secrets.choice(alphanumeric) for _ in range(length))
    return test_id

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_runner.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    config = load_yaml_file(directory)
    test_id = f"%s_%s" % (config['model']['name'] , generate_test_id())
    print('Generated Test ID:', test_id)

    for step in config['steps']:
        step_name = step['name']
        print(f"Performing step: {step_name}")
        if step_name == 'copy_test_suite':
            copy_test_suite(test_id)
        elif step_name == 'run_completions':
            run_completions(test_id)
        elif step_name == 'run_metrics_evaluation':
            metrics = step.get('metrics', [])
            if 'test_metrics' in metrics:
                run_metrics_evaluation()
        elif step_name == 'build_report':
            build_report()
        else:
            print(f"Unknown step: {step_name}")
