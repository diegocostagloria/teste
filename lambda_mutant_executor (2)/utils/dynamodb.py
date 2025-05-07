def save_execution(client, data):
    table = client.Table('MutantExecutions')
    table.put_item(Item=data)
