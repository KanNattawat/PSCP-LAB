""" pscp """
import json


def print_filtered_score(dict_input: str, score: float):
    """ main """
    dict_input = json.loads(dict_input)
    dict_filtered = [(int(key), value) for key, value in dict_input.items() if value > score]
    dict_sorted = sorted(dict_filtered, key=lambda i: i[0])

    print("\n".join(["{}\t{:.2f}".format(key, value) for key, value in dict_sorted]) \
          if len(dict_sorted) != 0 else "Nope")

if __name__ == "__main__":
    print_filtered_score(input(), float(input()))
