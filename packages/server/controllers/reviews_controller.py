from services.reviews_service import ReviewService
from fastapi import HTTPException


class ReviewController:
    @staticmethod
    async def getReviews(id: int):
        try:
            return await ReviewService.get_reviews_for_product(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")
