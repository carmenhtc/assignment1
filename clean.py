import pandas as pd
import sys


def clean_data(input1, input2, output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)

    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')

    merged_df = merged_df.dropna()

    merged_df = merged_df[~merged_df['job'].str.contains('insurance|Insurance')]

    cleaned_df = merged_df[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]

    cleaned_df.to_csv(output, index=False)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python clean.py <input1> <input2> <output>")
    else:
        input1 = sys.argv[1]
        input2 = sys.argv[2]
        output = sys.argv[3]

        clean_data(input1, input2, output)