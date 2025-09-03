from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Weather-info")

@mcp.tool()
def get_weather_data(location:str) -> dict:
    api_key = "your-api-key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "city": data["name"],
            "timezone": data["timezone"],
            "temperature": f"{data['main']['temp']} °C",
            "weather": data["weather"][0]["description"],
            "humidity": f"{data['main']['humidity']}%",
            "wind_speed": f"{data['wind']['speed']} m/s"
        }
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e}"
    except requests.exceptions.ConnectionError:
        return "Connection Error occured"
    except requests.exceptions.Timeout:
        return "Timeout Error occured"
    except requests.exceptions.RequestException as e:
        return f"General Error: {e}"


@mcp.resource("weather://template")
def weather_data_template():
    return {
        "default": "Current weather in {city}: {temperature}, {weather['description']}. Humidity: {humidity}, Wind: {wind_speed}.",
        "short": "{city}: {temperature}, {weather}",
        "detailed": (
            "Weather update for {city}\n"
            "- Temperature: {temperature}\n"
            "- Condition: {weather}\n"
            "- Humidity: {humidity}\n"
            "- Wind Speed: {wind_speed}\n"
            "- Pressure: {pressure}\n"
            "- Latitude: {latitude}\n"
            "- Longitude: {longitude}"
        )
    }

if __name__ == "__main__":
    mcp.run()
