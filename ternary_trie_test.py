import pytest
from ternary_trie import TernaryTrieNode

@pytest.fixture
def root():
    root =  TernaryTrieNode("ROOT")

    root.insert("cute")
    root.insert("cubs")
    root.insert("cube")
    root.insert("cup")
    root.insert("cot")
    root.insert("cya")
    root.insert("act")
    root.insert("acted")
    root.insert("day")
    root.insert("daze")

    return root

def test_1(root):
    # Check if cute is in the trie
    cur_node = root

    assert cur_node.value == 'c'
    assert cur_node.end == False
    cur_node = cur_node.next

    assert cur_node.value == 'u'
    assert cur_node.end == False
    cur_node = cur_node.next

    assert cur_node.value == 't'
    assert cur_node.end == False
    cur_node = cur_node.next

    assert cur_node.value == 'e'
    assert cur_node.end == True


def test_2(root):
    # Check if act is in the trie
    cur_node = root

    cur_node = cur_node.left
    assert cur_node.value == 'a'
    assert cur_node.end == False
    cur_node = cur_node.next

    assert cur_node.value == 'c'
    assert cur_node.end == False
    cur_node = cur_node.next

    assert cur_node.value == 't'
    assert cur_node.end == True
    assert cur_node.next is not None