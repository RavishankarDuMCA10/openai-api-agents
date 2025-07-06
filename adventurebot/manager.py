from agents import Runner, trace, gen_trace_id, Agent
from agents.result import RunResult
from agents.mcp import MCPServerStdio
from .models import TripQuery, TripContext
from .agents import(
    create_weather_agent, WeatherAnalysis,
    create_activity_search_agent, SearchResult,
    create_recommendation_agent, TripPlan,
)

class AdventureManager:
    """Manages the simplified adventure planning workflow with handoff and custom tool examples."""

    def __init__(self):
        self.activity_search_agent: Agent[TripContext] = create_activity_search_agent()
        self.recommendation_agent: Agent[TripContext] = create_recommendation_agent()

    async def run(self, query: TripQuery) -> None:
        """Run the simplified adventure planning workflow"""
        trace_id = gen_trace_id()
        print(f"Starting adventure planning... (Trace ID: {trace_id})")
        print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")

        # Create the context object
        trip_context = TripContext(query=query)

        with trace("Adventure Planning (Simplified)", trace_id=trace_id):
            # 1. Get Weather Information
            weather_info = await self._get_weather_info(trip_context)

            # 2. Search for Activities (potentially involves handoff)
            search_results, search_agent_used = await self._search_for_activities(trip_context, weather_info)

            # 3. Generate Trip Plan (includes evaluation and recommendations)
            trip_plan = await self._generate_trip_plan(search_results, weather_info, trip_context)

            # Display the final trip plan
            self._print_trip_plan(trip_plan)