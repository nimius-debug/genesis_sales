from agency_swarm import Agency
from GoogleBusinessExpertAgent import GoogleBusinessExpertAgent
from CEOAgent import CEOAgent

ceo = CEOAgent()
google_business_expert = GoogleBusinessExpertAgent()

agency = Agency([ceo, 
                [ceo, google_business_expert]],
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    completion_output = agency.get_completion("find me the phone number of ecommerce business and there names in tampa.", yield_messages=False)
    print(completion_output)