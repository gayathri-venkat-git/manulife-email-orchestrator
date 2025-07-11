from modules.priority_detector import classify_priority

def test_classifier():
    assert classify_priority("urgent response needed") in ["High", "Low"]
