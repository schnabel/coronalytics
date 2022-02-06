import awswrangler as wr
import pandas as pd
from rki import urls

BUCKET = 'beaker42-coronalytics'
def lambda_handler(event, context):
    try:
        for record in event['Records']:
            state = record["body"]
            print(f'Loading state data for {state}')
            df = pd.read_csv(urls[state])

            path = f"s3://{BUCKET}/csv/{state}.csv"
            wr.s3.to_csv(df, path, index=False)
    except Exception as e:
        print(e)
        raise e