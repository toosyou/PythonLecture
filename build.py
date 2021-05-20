import re
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path')

    args = parser.parse_args()

    with open(args.path, 'r') as f:
        slide = f.read()
        no_pop_quiz = re.sub(r'---(?:(?!---).)+pop quiz(?:(?!---).)+', '', slide, flags=re.I | re.M | re.S)

        with open(args.path.replace('_pq', ''), 'w') as f:
            f.write(no_pop_quiz)