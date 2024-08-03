from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45
    HIGH_MULTIPLIER = 1.2
    LOW_MULTIPLIER = 0.9

    @property
    def payment_percentage(self):
        return self.INITIAL_PAYMENT_PERCENTAGE

    @property
    def high_engagement_rate_multiplier(self):
        return self.HIGH_MULTIPLIER

    @property
    def low_engagement_rate_multiplier(self):
        return self.LOW_MULTIPLIER
