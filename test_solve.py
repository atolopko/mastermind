from solve import query_response, is_code_admissible, prune

def test_query_response():
    assert query_response('1111', '1111') == (4, 0)
    assert query_response('1234', '1234') == (4, 0)
    assert query_response('4321', '1234') == (0, 4)
    assert query_response('1111', '1231') == (2, 0)
    assert query_response('1321', '1231') == (2, 2)
    assert query_response('0000', '1111') == (0, 0)
    assert query_response('1234', '0123') == (0, 3)
    assert query_response('1111', '1234') == (1, 0)
    assert query_response('1450', '0000') == (1, 0)
    

def test_is_code_admissible():
    assert is_code_admissible('0100', '1234', 0, 1)
    assert is_code_admissible('0010', '1234', 0, 1)
    assert is_code_admissible('0001', '1234', 0, 1)
    assert is_code_admissible('2000', '1234', 0, 1)
    assert is_code_admissible('0020', '1234', 0, 1)
    assert is_code_admissible('0002', '1234', 0, 1)
    assert is_code_admissible('0100', '1234', 0, 1)
    assert not is_code_admissible('2100', '1234', 0, 1)

    assert is_code_admissible('2100', '1234', 0, 2)
    assert not is_code_admissible('2130', '1234', 0, 2)
    assert not is_code_admissible('2104', '1234', 0, 2)

    assert is_code_admissible('1111', '1234', 1, 0)
    assert not is_code_admissible('1211', '1234', 1, 0)

    assert is_code_admissible('1121', '1234', 1, 1)
    assert is_code_admissible('1112', '1234', 1, 1)
    assert not is_code_admissible('1114', '1234', 1, 1)
    assert not is_code_admissible('1142', '1234', 1, 1)

    assert is_code_admissible('1241', '1234', 2, 1)
    assert not is_code_admissible('1243', '1234', 2, 1)
    assert not is_code_admissible('1112', '1121', 2, 1)
    assert is_code_admissible('1113', '1121', 2, 1)

    assert not is_code_admissible('1241', '1234', 1, 2)
    assert is_code_admissible('1321', '1234', 1, 2)

    assert not is_code_admissible('1234', '1234', 1, 3)
    assert is_code_admissible('1423', '1234', 1, 3)
    assert not is_code_admissible('1243', '1234', 1, 3)


def test_prune():
    assert prune('1234', 0, 0, ['1000', '0100', '2000', '0000', '0055', '5555']) == ['0000', '0055', '5555']
    assert prune('1234', 1, 1, ['1020', '1300']) == ['1020', '1300']
    assert prune('1234', 1, 1, ['1200', '1004']) == []
    assert prune('1234', 2, 2, ['1324', '1243', '1432', '4231', '4321', '1111', '1234']) == ['1324', '1243', '1432', '4231']
