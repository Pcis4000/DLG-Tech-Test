import json

def sumList(numberList):
    
    result = {'total': 0}
    for number in numberList:
        try:
            result['total'] += int(number)
        except:
            pass
    
    return result

def lambda_handler(event, context):
    
    totals = sumList(event['body'])
    return {
        'statusCode': 200,
        'body': json.dumps(totals)
    }