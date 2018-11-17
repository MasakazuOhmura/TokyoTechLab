import collections
import csv

import pandas as pd

SUBJECTS = 8


def print_stat():
    """ 各フレーズの一番一致率の高い形容詞の一致率を集計 """
    df = pd.read_csv('intagrated_interpretations_eight.csv')

    top_prob_li = []
    for col in df.columns:
        """ phrase1 <= col <= phrase358 """
        print("========", col, "========")

        c = collections.Counter(df[col])

        # 各phraseでもっとも一致率の高いものを記録
        top_prob = 0
        for adj, count in c.most_common():
            if isinstance(adj, str):  # excluding NaN
                top_prob = max(top_prob, count)
                prob = str(count / SUBJECTS * 100) + "%"
                print(adj, prob)

        top_prob = str(top_prob / SUBJECTS * 100) + "%"
        top_prob_li.append(top_prob)

    print()
    # 各phraseの中でもっとも一致率の高い確率を調査
    c2 = collections.Counter(top_prob_li)
    for prob, count in c2.most_common():
        print(prob, "\t", count)


def create_interpretation_csv():
    """
    以下の形式のcsvを出力
    phrase x
    (adj, count), (adj, count)...

    """
    df = pd.read_csv('intagrated_interpretations_eight.csv')
    with open("interpretations_with_stat.csv", "w") as f:
        writer = csv.writer(f)
        for col in df.columns:
            c = collections.Counter(df[col])
            writer.writerow([col])
            adj_prob_li = []
            for adj, count in c.most_common():
                if isinstance(adj, str):  # excluding NaN
                    prob = str(count / SUBJECTS * 100) + "%"
                    adj_prob_li.append((adj, prob))
            writer.writerow(adj_prob_li)


def main():
    print(__file__)
    create_interpretation_csv()


if __name__ == '__main__':
    main()
