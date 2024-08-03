from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    HIGHBUDGET = 5000.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.HIGHBUDGET, required_engagement)

    @property
    def engagement_rate_coefficient(self):
        return 1.2
