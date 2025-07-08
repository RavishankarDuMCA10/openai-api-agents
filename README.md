# Openai-api-agents SDK

AI agents generate plans and perform complex multi-step tasks based on the user input. The OpenAI API provides comprehensive support for building AI agents that use models, tools, knowledge and memory, audio and speech, guardrails, orchestration, and MCP that can be customized to fit specific needs and scenarios. This project explores how to develop advanced agents with the OpenAI API and the Agents Python SDK. You’ll define custom agents, set up agent runners, configure handoffs so agents can work together, add guardrails for content moderation, and extend the agents with off-the-shelf OpenAI features, custom functions, and MCP (Model Context Protocol) servers.

## Instructions

This repository has three main folders:

- `./adventurebot/`: The folder you'll work with
- `./mcp_server_weather/`: An MCP Server you'll incorporate into the project

To start developing, install all dependencies:

```bash
pip install -r requirements.txt
```

### Authentication

You need an OpenAI API key to run the Agents SDK. Get your key at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

To use the API key, install the key into your environment:

```bash
export OPENAI_API_KEY=<your-key-here>
```

## Reference:

Morten Rand-Hendriksen's course [https://www.linkedin.com/learning/openai-api-agents/building-ai-agents-with-the-openai-agents-sdk?u=2037868](https://www.linkedin.com/learning/openai-api-agents/building-ai-agents-with-the-openai-agents-sdk?u=2037868).
