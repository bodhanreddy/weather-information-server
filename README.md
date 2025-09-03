# Weather Info MCP Server

A Model Control Protocol (MCP) server that provides real-time weather information using the OpenWeatherMap API. Built with FastMCP for easy integration with MCP-compatible applications and AI assistants.

## Features

-  **Real-time Weather Data**: Get current weather conditions for any location worldwide
-  **Comprehensive Information**: Temperature, weather conditions, humidity, wind speed, and more
-  **Flexible Templates**: Multiple response formats for different use cases
-  **Robust Error Handling**: Graceful handling of network issues and API errors
-  **Fast & Reliable**: 5-second timeout ensures quick responses

### Available Tools

#### `get_weather_data(location: str)`

Retrieves current weather data for the specified location.

**Parameters:**
- `location` (string): City name or location (e.g., "London", "New York", "Tokyo")

**Returns:**
- `city`: City name
- `timezone`: Timezone offset
- `temperature`: Current temperature in Celsius
- `weather`: Weather description
- `humidity`: Humidity percentage
- `wind_speed`: Wind speed in m/s

### Response Templates

The server provides three built-in response templates via the `weather://template` resource:

- **Default**: `"Current weather in {city}: {temperature}, {weather}. Humidity: {humidity}, Wind: {wind_speed}."`
- **Short**: `"{city}: {temperature}, {weather}"`
- **Detailed**: Multi-line format with comprehensive weather information

## Example Response

```json
{
  "city": "London",
  "timezone": 0,
  "temperature": "22 °C",
  "weather": "partly cloudy",
  "humidity": "65%",
  "wind_speed": "3.5 m/s"
}
```

## Error Handling

The server handles various error conditions gracefully:

- **HTTP Errors**: Invalid location or API issues
- **Connection Errors**: Network connectivity problems
- **Timeout Errors**: Requests taking longer than 5 seconds
- **General Errors**: Other unexpected issues

All errors return descriptive messages to help with troubleshooting.

## Configuration

### API Key Setup

**Important**: Replace the hardcoded API key in `main.py` with your own:

```python
api_key = "your_openweathermap_api_key_here"
```

For production use, consider using environment variables:

```python
import os
api_key = os.getenv("OPENWEATHER_API_KEY", "your_default_key")
```

## Requirements

- Python 3.7+
- `fastmcp`
- `requests`
- OpenWeatherMap API key

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

***

**Note**: This server uses the OpenWeatherMap API. Please ensure you comply with their [terms of service](https://openweathermap.org/terms) and usage limits.
