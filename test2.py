import pandas as pd

snowpark_df = session.table('SYNTHETIC_PROFILE_500K')

df = snowpark_df.to_pandas()
test_df = df[['VISITOR_ID', 'VISITOR_CREATED', 'PROPERTY_COUNTRY', 'BADGE_EMAIL_OPTED_IN']]
filtered_test_df = test_df[(test_df['PROPERTY_COUNTRY'] == 'US') & (test_df['BADGE_EMAIL_OPTED_IN'] == 'TRUE')]
filter_test_df.head()
