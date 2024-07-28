from abc import ABC, abstractmethod


class BaseCampaign(ABC):

    campaign_ids_collection = set()

    def __init__(self, campaign_id: int, brand: str, budget: float, required_engagement: float):
        self.campaign_id = campaign_id
        self.brand = brand
        self.budget = budget
        self.required_engagement = required_engagement
        self.approved_influencers: list = []

# TO DO add object Influencers

    @property
    def campaign_id(self):
        return self.__campaign_id
    
    @campaign_id.setter
    def campaign_id(self, value):
        if value <= 0:
            raise Exception("Campaign ID must be a positive integer greater than zero.")
        if value in self.campaign_ids_collection:
            raise Exception("Campaign with ID {campaign_id} already exists. Campaign IDs must be unique.")
        self.campaign_ids_collection.add(value)
        self.__campaign_id = value

    @abstractmethod
    def check_eligibility(self, engagement_rate: float):
        pass
