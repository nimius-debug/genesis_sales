from agency_swarm.agents import Agent


class GoogleBusinessExpertAgent(Agent):
    def __init__(self):
        super().__init__(
            name="GoogleBusinessExpertAgent",
            description="The GoogleBusinessExpert Agent specializes in fetching business information based on user queries, such as finding restaurants in specific locations, using the Google Business API or similar services.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
