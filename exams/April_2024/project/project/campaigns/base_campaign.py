from abc import ABC, abstractmethod
from typing import List

# from project.influencers.base_influencer import BaseInfluencer


class BaseCampaign(ABC):
    campaign_ids_collection = set()

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers = []

    @property
    @abstractmethod
    def engagement_rate_coefficient(self):
        pass

    @property
    def campaign_id(self):
        return self.__campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Campaign ID must be a positive integer greater than zero.")
        if value in self.campaign_ids_collection:
            raise ValueError(f"Campaign with ID {value} already exists. Campaign IDs must be unique.")
        self.campaign_ids_collection.add(value)
        self.__campaign_id = value

    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= self.engagement_rate_coefficient * self.required_engagement
