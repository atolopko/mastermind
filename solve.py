from random import randrange
import sys
import numpy as np

# code repr is 4-char string, with each color as digit 0-5
COLORS = 6
CODE_LEN = 4
MAX_CODES = COLORS ** CODE_LEN
ALL_CODES = [list(np.base_repr(code, 6).rjust(CODE_LEN, '0')) for code in range(0, MAX_CODES)]


def next_code_query(admissible_codes) -> list:
    """ 
    As the code breaker, generate the next code query (guess). Do this
    by simply guessing one of the remaining admissible_codes!
    """
    return admissible_codes[randrange(len(admissible_codes))]


def query_response(query, code) -> (int, int):
    correct = 0
    included = 0

    for c, q in zip(query, code):
        if c == q:
            correct += 1

    code = list(code)
    for q in query:
        if q in code:
            code.remove(q)
            included += 1

    return correct, included - correct


def is_code_admissible(candidate_code, query, resp_correct, resp_misplaced) -> bool:
    # For determining admissibility of a candidate code, the player's
    # query becomes the code, and candidate code becomes the query
    correct, misplaced = query_response(query=candidate_code, code=query)
    return correct == resp_correct and misplaced == resp_misplaced


def prune(query, resp_correct, resp_misplaced, admissible_codes) -> list:
    new_admissible_codes = []
    for candidate_code in admissible_codes:
        if is_code_admissible(candidate_code, query, resp_correct, resp_misplaced):
            new_admissible_codes.append(candidate_code)
            # print(f'admit {code}')
    return new_admissible_codes


def play_round(code, admissible_codes) -> list:
    query = next_code_query(admissible_codes)
    num_correct, num_misplaced = query_response(query, code)
    new_admissible_codes = prune(query, num_correct, num_misplaced, admissible_codes)
    # print(f'code={code}, query={query}, correct={num_correct}, misplaced={num_misplaced}, admissible_codes={len(new_admissible_codes)}')

    # Ensure progress is made
    assert len(new_admissible_codes) < len(admissible_codes)

    # print(new_admissible_codes)
    return new_admissible_codes

        
if __name__ == "__main__":
    admissible_codes = ALL_CODES
    rounds_taken = []

    for code in ALL_CODES:
        # print('=' * 80)
        # print(f'Trying to break code {code}')
        round = 1
        admissible_codes = ALL_CODES

        while len(admissible_codes) > 1:
            # print(f'ROUND {round}')
            admissible_codes = play_round(code, admissible_codes)
            round += 1

        # print(f'CODE: {code}')
        # print(f'QUERY: {admissible_codes[0]}')
        assert len(admissible_codes) == 1
        assert admissible_codes[0] == code
        print(f'{code} BROKEN in {round} rounds!')
            
        rounds_taken.append(round)

    print(np.histogram(rounds_taken, bins=10, range=(0, 10)))
    print(f"Max turns required={max(rounds_taken)}")

