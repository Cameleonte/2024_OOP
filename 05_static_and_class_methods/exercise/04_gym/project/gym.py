from project import exercise_plan
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan


class Gym:

    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    @staticmethod
    def add_obj(obj, obj_collection: list):
        if obj not in obj_collection:
            obj_collection.append(obj)

    def add_customer(self, customer: Customer):
        return self.add_obj(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        return self.add_obj(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        return self.add_obj(equipment, self.equipment)

    def add_plan(self, plans: ExercisePlan):
        return self.add_obj(plans, self.plans)

    def add_subscription(self, subscription: Subscription):
        return self.add_obj(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer_repr = [c.__repr__() for c in self.customers if c.id == subscription.customer_id][0]
        trainer_repr = [t.__repr__() for t in self.trainers if t.id == subscription.trainer_id][0]
        equipment_repr = [eq.__repr__() for eq in self.equipment if eq.id == subscription.exercise_id][0]
        exercise_repr = [ex.__repr__() for ex in self.plans if ex.id == subscription.exercise_id][0]
        result = '\n'.join([subscription.__repr__(), customer_repr, trainer_repr, equipment_repr, exercise_repr])

        return result
