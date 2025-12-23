from fastmcp import FastMCP

mcp = FastMCP("Audio Cure")

@mcp.tool
def getPainAudio() -> str:
    """用于治疗各种头疼的音频文件链接"""
    return "https://cn.bing.com/"


if __name__ == "__main__":
    mcp.run()