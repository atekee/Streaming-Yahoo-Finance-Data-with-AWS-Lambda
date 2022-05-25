# Streaming-Yahoo-Finance-Data-with-AWS-Lambda

In this project, I provisioned a lambda function to generate a real time data pipeline for interactive querying and further data analysis. Using [yfinance](https://pypi.org/project/yfinance/) module, I grabbed the price information for each of the following stocks:

• Facebook (FB) \
• Shopify (SHOP) \
• Beyond Meat (BYND) \
• Netflix (NFLX) \
• Pinterest (PINS) \
• Square (SQ) \
• The Trade Desk (TTD) \
• Okta (OKTA) \
• Snap (SNAP) \
• Datadog (DDOG)

The collected information includes one full day's worth of stock HIGH and LOW prices for each company listed above on Monday 05/02/2022, at a one-minute interval. For each datapoint, I generated a JSON object that looks like so:

```
{
  "high": 67.5, 
  "low": 64.61, 
  "ts": "2020-05-13 09:30:00-04:00", 
  "name": "DDOG"
}
```
In order to grab this information, I created a lambda function called [data transformer](https://github.com/atekee/Streaming-Yahoo-Finance-Data-with-AWS-Lambda/blob/main/data_transformer.py) that pulls the data from yfinance API, and pushes it into data collector.
Then, I configured AWS Glue by pointing it out the S3 Bucket created in our Data Collector, so that I could run [SQL queries](https://github.com/atekee/Streaming-Yahoo-Finance-Data-with-AWS-Lambda/blob/main/query.sql) with the streamed data using AWS Athena.
At last, I exported the results of my SQL query into [results.csv](https://github.com/atekee/Streaming-Yahoo-Finance-Data-with-AWS-Lambda/blob/main/results.csv) file that contains the highest hourly stock price for each company, and further analyzed it in my [Jupyter notebook](https://github.com/atekee/Streaming-Yahoo-Finance-Data-with-AWS-Lambda/blob/main/analysis.ipynb).

<img width="450" alt="image" src="https://user-images.githubusercontent.com/82621412/169951706-1cb91385-fad7-4473-8c7f-c662e325bdf6.png">


## Tech Used
AWS Services: Lambda, Kinesis, Glue, S3, Athena, Python, API

## Kinesis Configuration
![alt text](https://github.com/atekee/Streaming-Yahoo-Finance-Data-with-AWS-Lambda/blob/main/assets/kinesis_config.png)

## S3 Content
![alt text](https://github.com/atekee/Streaming-Yahoo-Finance-Data-with-AWS-Lambda/blob/main/assets/screen_shot_of_s3_bucket.png)
