import os

from openai import OpenAI
from mcp.server.mcpserver import MCPServer
from mcp.server.transport_security import TransportSecuritySettings

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

mcp = MCPServer("Claude ChatGPT Bridge")


@mcp.tool()
def ask_chatgpt(message: str) -> str:
    """Envia una pregunta a ChatGPT i retorna la seva resposta."""
    response = client.responses.create(
        model="gpt-5",
        input=message,
    )
    return response.output_text


security = TransportSecuritySettings(
    enable_dns_rebinding_protection=False
)

app = mcp.streamable_http_app(
    transport_security=security,
    stateless_http=True,
)