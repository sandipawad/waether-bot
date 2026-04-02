from app.services.weather_service import get_current_weather

def test_weather():
    data = get_current_weather()
    assert "temperature" in data
    assert "windspeed" in data