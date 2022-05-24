import os
import yfinance as yf
import json
import boto3
import datetime as dt
import pandas as pd

STREAM_NAME = os.environ['STREAM_NAME']
REGION = os.environ['REGION']

kinesis = boto3.client('kinesis', region_name = REGION)

def lambda_handler(event, context):
    stock_tickers = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
    start_date = '2022-05-02'
    end_date = '2022-05-03'
    interval = '1m'
    
    for ticker in stock_tickers:
        df = yf.download(ticker, start = start_date, end = end_date, interval = interval)
        
        for index, row in df.iterrows():
            dic = { 'name': ticker, 'high': row['High'], 'low': row['Low'], 'ts': index.strftime('%Y-%m-%d %X') }
            data = json.dumps(dic)+"\n"
            print(data)
            
            output = kinesis.put_record(
                StreamName = STREAM_NAME, 
                Data = data.encode('utf-8'), 
                PartitionKey = 'partitionkey')
            ##print(output)
                
    return {
        'statusCode': 200,
        'body': json.dumps('Done!')
    }