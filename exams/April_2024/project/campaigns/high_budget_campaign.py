from campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):

    HIGHBUDGET = 5000

    def __init__(self, campaign_id: int, brand: str, required_engagement: float, budget):
        super().__init__(campaign_id, brand, budget, required_engagement)
        self.budget = self.HIGHBUDGET
