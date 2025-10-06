from fastapi import HTTPException
from repositories.reviews_repository import reviewsRepository
from llm.client import generate_text


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

    @staticmethod
    async def summarize_reviews(product_id: int):

        reviews = await reviewsRepository.get_reviews_by_product(product_id, 10)
        reviews_text = "".join([r.content for r in reviews])
        prompt = f"Summarize the following customer reviews into a short paragraph hilighting key themes, both positive and negative: {reviews_text}"

        response = generate_text(
            model="gpt-4o-mini",
            input=prompt,
            temperature=0.2,
            max_output_tokens=500,
        )

        return response["text"]
