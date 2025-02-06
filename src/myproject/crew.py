from crewai.flow.flow import Flow, start, listen
from litellm import completion  # Replace with your preferred LLM API client
import asyncio

class run_crew(Flow):
    api_key = "AIzaSyDuKDPsTiuoY6Ltwpk9SeZ1iRFfv7VcOtU"
    model = "gemini/gemini-1.5-flash"

    @start()
    async def generate_topic(self):
        print("Generating Blog Topic...")
        response = await asyncio.to_thread(completion,
            model=self.model,
            api_key=self.api_key,
            messages=[{
                "role": "user",
                "content": "Generate a creative blog topic for 2024."
            }]
        )
        topic = response.get("choices", [{}])[0].get("message", {}).get("content", "No topic generated")
        print(f"Generated Topic: {topic}")
        return topic

    @listen(generate_topic)
    async def generate_outline(self, topic):
        print(f"Generating Outline for topic: {topic}")
        response = await asyncio.to_thread(completion,
            model=self.model,
            api_key=self.api_key,
            messages=[{
                "role": "user",
                "content": f"Based on the topic '{topic}', create a detailed outline for a blog post."
            }]
        )
        outline = response.get("choices", [{}])[0].get("message", {}).get("content", "No outline generated")
        print("Generated Outline:")
        print(outline)
        return outline

if __name__ == "__main__":
    flow = run_crew()
    final_output = asyncio.run(flow.kickoff_async())
    print("Final Output:", final_output)
