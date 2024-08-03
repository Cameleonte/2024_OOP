from typing import List

from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_CAMPAIGNS = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float) -> str:
        try:
            influencer = self.VALID_INFLUENCERS[influencer_type](username, followers, engagement_rate)
        except KeyError:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            # if influencer.check_eligibility():
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float) -> str:
        if campaign_type not in self.VALID_CAMPAIGNS:
            return f"{campaign_type} is not a valid campaign type."
        try:
            next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:
            curr_campaign = self.VALID_CAMPAIGNS[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(curr_campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int) -> str:
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the "
                    f"eligibility criteria for the campaign with ID {campaign_id}.")

        payment_current_influencer = influencer.calculate_payment(campaign)
        if payment_current_influencer > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment_current_influencer
            influencer.campaigns_participated.append(campaign)
            return (f"Influencer '{influencer_username}' has successfully "
                    f"participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self) -> dict:
        campaigns_dictionary = {}
        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                followers_count = influencer.reached_followers(campaign.__class__.__name__)
                campaigns_dictionary[campaign] = campaigns_dictionary.get(campaign, 0) + followers_count

        return campaigns_dictionary

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda i: i.username == username, self.influencers))
        if influencer:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda camp: (len(camp.approved_influencers), -camp.budget))
        to_print = [
            f"  * Brand: {camp.brand}, "
            f"Total influencers: {len(camp.approved_influencers)}, "
            f"Total budget: ${camp.budget:.2f}, "
            f"Total reached followers: {self.calculate_total_reached_followers().get(camp, 0)}"
            for camp in sorted_campaigns
        ]

        return f"$$ Campaign Statistics $$\n" + '\n'.join(to_print)
