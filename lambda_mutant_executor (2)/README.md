# Lambda Mutant Executor

Este projeto implementa um Lambda que consome mensagens de uma fila SQS, gera dinamicamente um `buildspec.yml` baseado na linguagem do repositório (Java, Python ou Kotlin), e aciona uma API de execução de testes mutantes. Também registra os dados de execução no DynamoDB.

## Funcionalidades
- Consome mensagens com `repoName`, `language`, e `mutantConfig`
- Gera token do GitHub
- Usa motor de template Jinja2 para criar `buildspec.yml` customizado
- Codifica em base64 e envia para execução externa
- Registra a execução no DynamoDB

## Estrutura
```
project_root/
├── main.py
├── requirements.txt
├── templates/
│   ├── java_buildspec.yml.j2
│   ├── python_buildspec.yml.j2
│   └── kotlin_buildspec.yml.j2
├── utils/
│   ├── buildspec_generator.py
│   ├── dynamodb.py
│   └── github.py
└── README.md
```

## Exemplo de entrada na fila SQS
```json
{
  "repoName": "empresa/nome-do-projeto",
  "language": "java",
  "mutantConfig": {
    "targetClasses": "com.empresa.*",
    "reportDir": "target/pit-reports",
    "threshold": 80
  }
}
```
