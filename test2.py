import pandas as pd

df = pd.read_snowflake('SYNTHETIC_PROFILE_500K')
test_df = df[['VISITOR_ID', 'VISITOR_CREATED', 'PROPERTY_COUNTRY', 'BADGE_EMAIL_OPTED_IN']]
filtered_test_df = test_df[(test_df['PROPERTY_COUNTRY' == 'US') & (TEST_DF['BADGE_EMAIL_OPTED_IN'] == 'TRUE')]
