from models.households import Household
from schemas.household import HouseholdCreate, HouseholdResponse
from typing import Optional, List


def to_household_response(household: Household) -> HouseholdResponse:
    return HouseholdResponse(
        id=str(household.id),
        name=household.name,
        members=household.members,
        created_at=household.created_at
    )


class HouseholdRepository:

    @staticmethod
    async def create_household(data: HouseholdCreate) -> HouseholdResponse:
        household = Household(
            name=data.name,
            members=data.members or []
        )
        await household.insert()
        return to_household_response(household)

    @staticmethod
    async def get_household_by_id(household_id: str) -> Optional[HouseholdResponse]:
        household = await Household.get(household_id)
        if not household:
            return None
        return to_household_response(household)

    @staticmethod
    async def get_all_households() -> List[HouseholdResponse]:
        households = await Household.find_all().to_list()
        return [to_household_response(h) for h in households]

    @staticmethod
    async def delete_household(household_id: str) -> bool:
        household = await Household.get(household_id)
        if not household:
            return False
        await household.delete()
        return True

    @staticmethod
    async def add_member(household_id: str, user_id: str) -> Optional[HouseholdResponse]:
        household = await Household.get(household_id)
        if not household:
            return None

        if user_id not in household.members:
            household.members.append(user_id)
            await household.save()

        return to_household_response(household)

    @staticmethod
    async def remove_member(household_id: str, user_id: str) -> Optional[HouseholdResponse]:
        household = await Household.get(household_id)
        if not household:
            return None

        if user_id in household.members:
            household.members.remove(user_id)
            await household.save()

        return to_household_response(household)