# Weather Info MCP Server - UV Project Setup

A Model Control Protocol (MCP) server that provides real-time weather information using the OpenWeatherMap API. This project is configured for modern Python development using UV package manager.

## Quick Start with UV

### 1. Create the Project

```bash
uv init weather-info-mcp
cd weather-info-mcp
```

### 2. Add Dependencies

```bash
uv add "mcp[cli]" requests
```

### 3. Replace the Generated Code

Replace the contents of `main.py` with the weather server code:

```python
from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("Weather-info")

@mcp.tool()
def get_weather_data(location: str) -> dict:
    api_key = "your_openweather_api_key_here"  # Replace with your API key
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
        return "Connection Error occurred"
    except requests.exceptions.Timeout:
        return "Timeout Error occurred"
    except requests.exceptions.RequestException as e:
        return f"General Error: {e}"

@mcp.resource("weather://template")
def weather_data_template():
    return {
        "default": "Current weather in {city}: {temperature}, {weather}. Humidity: {humidity}, Wind: {wind_speed}.",
        "short": "{city}: {temperature}, {weather}",
        "detailed": (
            "Weather update for {city}\n"
            "- Temperature: {temperature}\n"
            "- Condition: {weather}\n"
            "- Humidity: {humidity}\n"
            "- Wind Speed: {wind_speed}\n"
        )
    }

if __name__ == "__main__":
    mcp.run()
```

### 4. Get Your API Key

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Replace `"your_openweather_api_key_here"` in the code with your actual API key

## Installation Options

### Option 1: Install in Claude Desktop

Install the server directly in Claude Desktop:

```bash
uv run mcp install main.py
```

This will make the weather tool available in your Claude Desktop conversations.

### Option 2: Test with MCP Inspector

For development and testing, use the MCP Inspector:

```bash
uv run mcp dev main.py
```

This opens an interactive interface where you can test the weather tool functionality.

### Option 3: Run Standalone

Run the server directly:

```bash
uv run main.py
```

## Usage Example

Once installed in Claude Desktop, you can ask:

- "What's the weather in Tokyo?"
- "Get me the current weather for New York"
- "How's the weather in London today?"

The server will return formatted weather information including temperature, conditions, humidity, and wind speed.

## Project Structure

```
weather-info-mcp/
├── main.py           # MCP server implementation
├── pyproject.toml    # UV project configuration
└── README.md         # This file
```

## Configuration

### Environment Variables (Recommended)

For better security, use environment variables:

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

Then update the code to use:

```python
import os
api_key = os.getenv("OPENWEATHER_API_KEY")
```

### UV Project Configuration

The `pyproject.toml` file is automatically configured with:

```toml
[project]
dependencies = [
    "mcp[cli]",
    "requests",
]
```

## Development

### Adding More Features

You can extend the server by adding more tools:

```python
@mcp.tool()
def get_forecast(location: str, days: int = 5) -> dict:
    # Implementation for weather forecast
    pass
```

### Testing

Test your changes with:

```bash
uv run mcp dev main.py
```

## Troubleshooting

**Server won't start:**
- Ensure you have a valid OpenWeatherMap API key
- Check that all dependencies are installed: `uv sync`

**Connection errors:**
- Verify internet connection
- Check API key validity
- Ensure OpenWeatherMap service is accessible

**Tool not appearing in Claude:**
- Restart Claude Desktop after installation
- Check that the installation completed successfully

## Requirements

- Python 3.8+
- UV package manager
- OpenWeatherMap API key (free)
- Internet connection

## License

This project is open source and available under the MIT License.

***

**Ready to get started?** Just run the commands above and you'll have weather information at your fingertips in Claude Desktop! 🌤️

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/49358074/96e53b29-29f7-4e4f-89f2-6628679a9b06/main.py)
