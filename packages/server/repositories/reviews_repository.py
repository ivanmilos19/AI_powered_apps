from database.models import Review


class reviewsRepository:
    @staticmethod
    async def get_reviews_by_product(product_id: int):
        return await Review.filter(product_id=product_id).order_by("created_at")
