## Imports

import pandas as pd
import csv
import nltk

## Downloads

def sepposnegcom(comment_file):

    ## Reading Dataset

    dataset = pd.read_csv(comment_file, encoding_errors = 'ignore')
    dataset = dataset.iloc[:, 0:]

    ## Getting Full Comments to csv file

    # full_com = dataset
    # full_comments = full_com.to_csv("Full Comments.csv")

    ## Sentiment analysis of comments using vadar sentiment analyser

    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    analyser = SentimentIntensityAnalyzer()

    def vader_sentiment_result(sent):
        scores = analyser.polarity_scores(sent)

        if scores["neg"] > scores["pos"]:
            return 0
        return 1

    dataset['vader_sentiment'] = dataset['Comment'].apply(lambda x : vader_sentiment_result(x))

    ## Separating Positive and Negative Comments

    for (sentiment), group in dataset.groupby(['vader_sentiment']):
         group.to_csv(f'{sentiment}.csv', index=False)
 
    pos = (pd.read_csv("1.csv", engine = 'python')).iloc[:, :-1]
    neg = (pd.read_csv("0.csv", engine = 'python')).iloc[:, :-1]

    positive_comments = pos.to_csv("Positive Comments.csv", index=False)
    negative_comments = neg.to_csv("Negative Comments.csv",index=False)

    video_positive_comments = str(len(pos.axes[0])) + ' Comments'  #Finding total rows in positive comments
    video_negative_comments = str(len(neg.axes[0])) + ' Comments'  #Finding total rows in negative comments

    ## return function
    return positive_comments, negative_comments, video_positive_comments, video_negative_comments

# if __name__ == "__main__":
#     comment_file = "Full Comments (2).csv"
#     sepposnegcom(comment_file)
