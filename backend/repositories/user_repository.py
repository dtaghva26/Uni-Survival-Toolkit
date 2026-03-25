from models.user import User
from schemas.user import UserCreate, UserResponse
from typing import Optional, List


def to_user_response(user: User) -> UserResponse:
    return UserResponse(
        id=str(user.id),
        name=user.name,
        email=user.email,
        household_id=user.household_id,
        created_at=user.created_at
    )


class UserRepository:

    @staticmethod
    async def create_user(user_data: UserCreate) -> UserResponse:
        user = User(**user_data.model_dump())
        await user.insert()
        return to_user_response(user)

    @staticmethod
    async def get_user_by_id(user_id: str) -> Optional[UserResponse]:
        user = await User.get(user_id)
        if not user:
            return None
        return to_user_response(user)

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[UserResponse]:
        user = await User.find_one(User.email == email)
        if not user:
            return None
        return to_user_response(user)

    @staticmethod
    async def get_all_users() -> List[UserResponse]:
        users = await User.find_all().to_list()
        return [to_user_response(user) for user in users]

    @staticmethod
    async def delete_user(user_id: str) -> bool:
        user = await User.get(user_id)
        if not user:
            return False
        await user.delete()
        return True