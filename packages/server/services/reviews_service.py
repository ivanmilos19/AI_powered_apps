from datetime import datetime, timezone
from fastapi import HTTPException
from pathlib import Path
from repositories.reviews_repository import reviewsRepository
from llm.client import generate_text


script_dir = Path(__file__).parent
summarize_reviews_txt_path = (script_dir / "../prompts/summarize-reviews.txt").resolve()
summarize_reviews = summarize_reviews_txt_path.read_text()


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
        existing_summary = await reviewsRepository.get_review_summary(product_id)
        if existing_summary and existing_summary.expires_at > datetime.now(timezone.utc):
            return existing_summary.content

        reviews = await reviewsRepository.get_reviews_by_product(product_id, 10)
        reviews_text = "".join([r.content for r in reviews])
        prompt = summarize_reviews.replace("{{reviews}}", reviews_text)

        response = generate_text(
            model="gpt-4o-mini",
            input=prompt,
            temperature=0.2,
            max_output_tokens=500,
        )

        summary = response["text"]
        await reviewsRepository.store_review_summary(product_id, summary)

        return summary
