from agency_swarm.tools import BaseTool
from pydantic import Field
import requests
import os
from typing import Dict, Any

# Load environment variables from .env file
api_key = os.getenv("RAPID_API_KEY")

class GoogleBusinessAPIFetchTool(BaseTool):
    """
    This tool interfaces with the Google Business API to fetch business information based on user queries.
    It can handle requests such as finding restaurants or other businesses in specific locations.
    The tool sends requests to the API, handles responses, and processes the data to extract relevant business information such as name, address, contact details, and ratings.
    """

    queries: str = Field(
        ..., description="Search query for the business data, e.g., 'plumbers in Texas','restaurants in new york' or 'coffee shops'.", 
    )
    region: str = Field(
        ..., description="The region to search for businesses, such as 'us' for united stated." , enum=["es", "uk", "us", "fr", "de"],
    )

    class ToolConfig:
        strict = True
        
    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method sends a request to the Google Business API and processes the response to extract business information.
        """
        payload = {
            "queries": [self.queries],
            "region": self.region,
            "limit": 10,
            "zoom": 13,
            "dedup": True,
        }
        url = "https://local-business-data.p.rapidapi.com/search"
        headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "local-business-data.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            return self.clean_data(response.json())
        else:
            response.raise_for_status()

    def clean_data(self, response) -> Dict[str, Any]:
        """
        Cleans the data fetched from the API response.
        Returns a dictionary with essential business details.
        """
        cleaned_data = []
        if response["status"] == "OK" and "data" in response:
            for business in response["data"]:
                cleaned_data.append({
                    "name": business.get("name"),
                    "phone_number": business.get("phone_number"),
                    "address": business.get("full_address") or business.get("address"),
                    "rating": business.get("rating"),
                    "review_count": business.get("review_count"),
                    "website": business.get("website"),
                    "working_hours": business.get("working_hours") or "Not available"
                })
        return cleaned_data