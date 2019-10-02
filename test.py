from exercise import minCost
import pytest

@pytest.fixture
def simple_costs():
    return [[17,2,17],[16,16,5],[14,3,19]]

@pytest.fixture
def complex_costs():
    return [[17,15,10],[16,2,17],[14,8,15],[5,4,15],[16,1,2],[8,20,1],[15,20,16],[7,3,14],[1,14,15],[17,3,11],[16,12,18],[12,20,16],[20,2,10],[19,13,10],[1,18,8]]

def test_simple(simple_costs):
    assert minCost(simple_costs) == 10

def test_complex(complex_costs):
    assert minCost(complex_costs) == 99
