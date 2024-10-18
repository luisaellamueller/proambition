import pandas as pd
from textblob import TextBlob

# Load up the Excel file (don't forget to change the file name to your actual file)
# /Users/luisamuller/ProAmbition/EvaluatoinQuestionnaire/proambition_sentimentanalysis.xlsx
file_path = '/path/here.xlsx'
df = pd.read_excel(file_path)

# Grab the first column
text_column = df.columns[0]

# Define a function to get polarity (positive/negative) and subjectivity (opinion-based)
def get_sentiment(text):
    blob = TextBlob(str(text))
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Run the sentiment function on each row in the first column and create new columns
df[['Polarity', 'Subjectivity']] = df[text_column].apply(lambda x: pd.Series(get_sentiment(x)))

# Save the new DataFrame with sentiment results to a new Excel file
output_file = 'sentiment_analysis_output.xlsx'
df.to_excel(output_file, index=False)

# Done! Tell where the results are saved.
print(f"Sentiment analysis completed. Results saved to {output_file}")
