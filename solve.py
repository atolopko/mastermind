from random import randrange
import sys
import numpy as np
import pdb

# code repr is 4-char string, with each color as digit 0-5
colors = 6
code_len = 4
max_codes = colors ** code_len
all_codes = [np.base_repr(code, 6).rjust(code_len, '0') for code in range(0, max_codes)]

initial_guess = all_codes[randrange(0, max_codes)]

# print(all_codes)

def next_code_query(admissable_codes):
    """ 
    As the code breaker, generate the next code query (guess). Do this
    by simply guessing one of the remaining admissable_codes!
    """
    return admissable_codes[randrange(len(admissable_codes))]


def query_response(query, code) -> (int, int):
    correct = 0
    misplaced = 0
    code = list(code)
    for i in range(0, code_len):
        c = query[i]
        if c == code[i]:
            correct += 1
            code[i] = None
    for i in range(0, code_len):
        c = query[i]
        for j in range(0, code_len):
            if c == code[j]:
                misplaced += 1
                code[j] = None
                break
    return correct, misplaced


def code_admissible(query, code, resp_correct, resp_misplaced) -> bool:
    correct, misplaced = query_response(query=code, code=query)
    return correct == resp_correct and misplaced == resp_misplaced


def prune_solutions(query, resp_correct, resp_misplaced, admissable_codes):
    new_admissable_codes = []
    for candidate_code in admissable_codes:
        if code_admissible(query, candidate_code, resp_correct=resp_correct, resp_misplaced=resp_misplaced):
            new_admissable_codes.append(candidate_code)
            # print(f'admit {code}')
    return new_admissable_codes


def play_round(code, admissible_codes):
    query = next_code_query(admissible_codes)
    num_correct, num_misplaced = query_response(query=query, code=code)
    new_admissible_codes = prune_solutions(query, num_correct, num_misplaced, admissible_codes)
    # print(f'code={code}, query={query}, correct={num_correct}, misplaced={num_misplaced}, admissible_codes={len(new_admissible_codes)}')
    assert len(new_admissible_codes) < len(admissible_codes)
    # print(new_admissible_codes)
    return new_admissible_codes

        
if __name__ == "__main__":
    # code = sys.argv[1]
    # assert code in all_codes

    admissible_codes = all_codes
    rounds_taken = []

    for code in all_codes:
        # print(f'Trying to break code {code}')
        round = 0
        admissible_codes = all_codes
        while len(admissible_codes) > 1:
            # print(f'ROUND {round}')
            admissible_codes = play_round(code, admissible_codes)
            if len(admissible_codes) == 1:
                print(f'{code} BROKEN in {round} rounds!')
            round += 1
        rounds_taken.append(round)

    print(np.histogram(rounds_taken, bins=10, range=(0, 10)))
    print(f"Max turns required={max(rounds_taken)}")

