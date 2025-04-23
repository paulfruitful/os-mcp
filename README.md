# OS-MCP

A Python-based tool built with the MCP (Message Control Protocol) framework that provides operating system-related tools and functionalities.

## Description

OS-MCP is a tool that leverages the MCP framework to provide various operating system utilities and tools. It uses FastMCP to create a server that can handle tool requests and execute system operations.

## Requirements

- Python >= 3.13
- MCP >= 1.6.0 (with CLI support)

## Installation

1. Ensure you have Python 3.13 or higher installed
2. Install the dependencies:
```bash
pip install -r requirements.txt

## Trae
26 context(s) used

Workspace

README.md 1-1

pyproject.toml 1-11

uv.lock 247-270

.gitignore 1-13

uv.lock 1-25

... More ( 20 +)

Based on the project files I can see, I'll create a comprehensive README.md for this project. The project appears to be a Python-based tool using the MCP (Message Control Protocol) framework.

```markdown
# OS-MCP

A Python-based tool built with the MCP (Message Control Protocol) framework that provides operating system-related tools and functionalities.

## Description

OS-MCP is a tool that leverages the MCP framework to provide various operating system utilities and tools. It uses FastMCP to create a server that can handle tool requests and execute system operations.

## Requirements

- Python >= 3.13
- MCP >= 1.6.0 (with CLI support)

## Installation

1. Ensure you have Python 3.13 or higher installed
2. Install the dependencies:
```bash
pip install -r requirements.txt
 ```
```

## Features
Currently implemented tools:

- save_information : Saves provided information to a file with a specified name
## Usage
The project can be run using:

```python
python main.py
 ```

The server will start in stdio transport mode, allowing for command-line interaction with the tools.

## Project Structure
```plaintext
os-mcp/
├── main.py          # Main application entry point
├── README.md        # Project documentation
├── pyproject.toml   # Project configuration and dependencies
└── .gitignore      # Git ignore rules
 ```
```

## Development
To add new tools, extend the main.py file and use the @mcp.tool() decorator to register new functions as tools.

Example:

```python
@mcp.tool()
def your_new_tool(param1: str, param2: int):
    """
    Tool description here.
    """
    # Tool implementation
    return "Result"
 ```
```
