import os

def file_delete():
    file_to_delete = ["0.csv", "1.csv", "comments.csv", "Full Comments.csv", "Positive Comments.csv", "Negative Comments.csv"]

    for f in file_to_delete:
        os.remove(f)
