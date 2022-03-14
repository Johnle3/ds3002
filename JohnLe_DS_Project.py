


# 1.) Fetch / download / retrieve a remote data file by URL, S3 key, or ingest a
# local file mounted. Suggestions for remote data sources are listed at the
# end of this document.

#reading in a csv file from a local file downloaded off of kaggle
import pandas as pd
fff = pd.read_csv('/Users/johnle/School/Spring 2022/SARC 5400/fossilfund_dataset.csv')
print(fff)

# 2.) Convert the general format and data structure of the data source (from
# TSV to CSV, from CSV to JSON, from JSON into a SQL database table,
# etc.) EXTRA – Use and API (like twitter) to pull information realtime.

# CSV to JSON
import json
import time
fff = pd.read_csv('/Users/johnle/School/Spring 2022/SARC 5400/fossilfund_dataset.csv')
try:
    ffftojson = fff.to_json('/Users/johnle/School/Spring 2022/SARC 5400/fossilfund_dataset.json')
except:
    print("Error", ffftojson['error']['message'] )

# 3.) Modify the number of columns from the source to the destination,
# reducing or adding columns.

# Selecting certain columns
data = pd.read_json('/Users/johnle/School/Spring 2022/SARC 5400/fossilfund_dataset.json')
df = data[['Fund profile: Shareclass name',
           'Fund profile: Ticker',
           'Fund profile: Fund name',
           'Fund profile: Shareclass inception date',
           'Fund profile: Category group',
           'Fund profile: Sustainability mandate',
           'Fund profile: Fund net assets',
           'Fund profile: Percent rated',
           'Fossil Free Funds: Fossil fuel grade',
           'Deforestation Free Funds: Deforestation grade',
           'Gender Equality Funds: Gender equality grade',
           'Gun Free Funds: Civilian firearm grade',
           'Weapon Free Funds: Military weapon grade',
           ]]
#print(df)

# 5.) Generate a brief summary of the data file ingestion including:
# a. Number of records
# b. Number of columns
try:
    col = len(df.columns)
    print('number of columns:', + col)
except:
    print("Error",col['error']['message'] )
try:
    rows= len(df)
    print('number of rows:', + rows)
except:
    print("Error",row['error']['message'] )