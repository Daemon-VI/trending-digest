from digest.search import build_query


def test_build_query():
    assert 'language:python' in build_query("python")
    assert 'good first issue' in build_query("python")
