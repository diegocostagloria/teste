import json
import base64
import uuid
from datetime import datetime

import boto3
from utils import buildspec_generator, dynamodb

sqs = boto3.client('sqs')
dynamodb_client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    for record in event['Records']:
        payload = json.loads(record['body'])

        repo_name = payload['repoName']
        language = payload['language']
        mutant_config = payload.get('mutantConfig', {})

        buildspec_content = buildspec_generator.generate_buildspec(language, mutant_config)
        buildspec_base64 = base64.b64encode(buildspec_content.encode()).decode()

        execution_id = str(uuid.uuid4())
        timestamp_inicio = datetime.utcnow().isoformat()

        dynamodb.save_execution(dynamodb_client, {
            'executionId': execution_id,
            'repoName': repo_name,
            'language': language,
            'mutantConfig': mutant_config,
            'status': 'PENDING',
            'timestampInicio': timestamp_inicio
        })

        print(f"Repositório {repo_name} pronto para execução com ID {execution_id}")
