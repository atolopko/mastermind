from solve import query_response, code_admissible, prune_solutions

def test_query_response():
    assert query_response('1111', '1111') == (4, 0)
    assert query_response('1234', '1234') == (4, 0)
    assert query_response('4321', '1234') == (0, 4)
    assert query_response('1111', '1231') == (2, 0)
    assert query_response('1321', '1231') == (2, 2)
    assert query_response('0000', '1111') == (0, 0)
    assert query_response('1234', '0123') == (0, 3)
    assert query_response('1111', '1234') == (1, 0)
    

def test_code_admissible():
    assert code_admissible('1234', '0100', 0, 1)
    assert code_admissible('1234', '0010', 0, 1)
    assert code_admissible('1234', '0001', 0, 1)
    assert code_admissible('1234', '2000', 0, 1)
    assert code_admissible('1234', '0020', 0, 1)
    assert code_admissible('1234', '0002', 0, 1)
    assert code_admissible('1234', '0100', 0, 1)
    assert not code_admissible('1234', '2100', 0, 1)

    assert code_admissible('1234', '2100', 0, 2)
    assert not code_admissible('1234', '2130', 0, 2)
    assert not code_admissible('1234', '2104', 0, 2)

    assert code_admissible('1234', '1111', 1, 0)
    assert not code_admissible('1234', '1211', 1, 0)

    assert code_admissible('1234', '1121', 1, 1)
    assert code_admissible('1234', '1112', 1, 1)
    assert not code_admissible('1234', '1114', 1, 1)
    assert not code_admissible('1234', '1142', 1, 1)

    assert code_admissible('1234', '1241', 2, 1)
    assert not code_admissible('1234', '1243', 2, 1)
    assert not code_admissible('1121', '1112', 2, 1)
    assert code_admissible('1121', '1113', 2, 1)

    assert not code_admissible('1234', '1241', 1, 2)
    assert code_admissible('1234', '1321', 1, 2)

    assert not code_admissible('1234', '1234', 1, 3)
    assert code_admissible('1234', '1423', 1, 3)
    assert not code_admissible('1234', '1243', 1, 3)


def test_prune_solutions():
    assert prune_solutions('1234', 0, 0, ['1000', '0100', '2000', '0000', '0055', '5555']) == ['0000', '0055', '5555']
    assert prune_solutions('1234', 1, 1, ['1020', '1300']) == ['1020', '1300']
    assert prune_solutions('1234', 1, 1, ['1200', '1004']) == []
    assert prune_solutions('1234', 2, 2, ['1324', '1243', '1432', '4231', '4321', '1111', '1234']) == ['1324', '1243', '1432', '4231']
