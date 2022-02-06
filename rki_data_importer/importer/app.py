import json

import awswrangler as wr
import pandas as pd

BUCKET = 'beaker42-coronalytics'

def lambda_handler(event, context):
    try:
        DATA_URL = 'https://www.arcgis.com/sharing/rest/content/items/66876b81065340a4a48710b062319336/data'
        df = pd.read_csv(DATA_URL)
            
        path = f"s3://{BUCKET}/csv/data.csv"
        wr.s3.to_csv(df, path, index=False)
 
    except Exception as e:
        print(e)
        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
