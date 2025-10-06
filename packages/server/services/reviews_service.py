from repositories.reviews_repository import reviewsRepository
from fastapi import HTTPException


class ReviewService:
    @staticmethod
    async def get_reviews_for_product(product_id: int):
        if product_id <= 0:
            raise HTTPException(
                status_code=400, detail="Product ID must be a positive integer"
            )

        reviews = await reviewsRepository.get_reviews_by_product(product_id)
        if not reviews:
            raise HTTPException(
                status_code=404, detail="No reviews found for this product"
            )

        return [
            {
                "author": r.author,
                "rating": r.rating,
                "content": r.content,
                "created_at": r.created_at,
            }
            for r in reviews
        ]
