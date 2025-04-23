from typing import List
from mcp.server.fastmcp import FastMCP


mcp=FastMCP('OS-Tools')

@mcp.tool()
def save_information(info:str,name:str):
    """
    Saves information to a file and uses the name as the filename.
    """
    with open(name,'w') as f:
        f.write(info)
    return f"Information saved to {name} Successfully"




if __name__ == "__main__":
    mcp.run(transport="stdio")
