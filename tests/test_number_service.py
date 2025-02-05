from app.services.number_service import classify_number

def test_classify_number():
    assert classify_number(371) == ["armstrong", "odd"]
    assert classify_number(6) == ["perfect", "even"]