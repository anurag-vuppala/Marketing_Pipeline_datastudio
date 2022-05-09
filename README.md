# Marketing_Pipeline_datastudio

Step 1: Clean the given three datasets and remove duplications.
Step 2: Match the column names in both the Google and Facebook datasets and add a new column "platform" with the name of the platform [google, Facebook].
Step 3: Merge the two Google and Facebook datasets into a new dataset called "platform."
Step 4: Now compare the column names in the "campaign_spend" and "platform" datasets and match the column name with identical data (values) like [Data, campaign_id, platform] and join the two datasets with the joining keys (common columns in both datasets).

Step 5: Now we have a resultant dataset containing all the information from the 3 raw datasets.
Step 6: Standard normalization steps were applied to reduce redundancy in the data and a basic database model was designed.[Image below]
Step 7: Now a data set can be populated with this model and MySQL queries can be used to extract data.

Detailed steps are mentioned in the clean.ipynb file
