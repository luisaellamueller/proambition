import pandas as pd

import pandas as pd

# Load the Excel file (replace with your file path if needed)
# /Users/luisamuller/ProAmbition/EvaluatoinQuestionnaire/sentiment_analysis_output.xlsx 
file_path = '/path/here.xlsx''
df = pd.read_excel(file_path)

# Getting the column names 
polarity_column = 'Polarity'
subjectivity_column = 'Subjectivity'

# Calculating overall average polarity and subjectivity
average_polarity = df[polarity_column].mean()
average_subjectivity = df[subjectivity_column].mean()

# Count the number of positive, negative, and neutral sentiments based on polarity
positive_count = (df[polarity_column] > 0).sum()
negative_count = (df[polarity_column] < 0).sum()
neutral_count = (df[polarity_column] == 0).sum()

# Here, I print the results ( see evaluation questionnaire)
print(f"Average Polarity: {average_polarity}")
print(f"Average Subjectivity: {average_subjectivity}")
print(f"Positive Responses: {positive_count}")
print(f"Negative Responses: {negative_count}")
print(f"Neutral Responses: {neutral_count}")

# To evaluate the overall sentiment:
if average_polarity > 0:
    sentiment_overall = "Overall positive sentiment"
elif average_polarity < 0:
    sentiment_overall = "Overall negative sentiment"
else:
    sentiment_overall = "Overall neutral sentiment"

print(sentiment_overall)
