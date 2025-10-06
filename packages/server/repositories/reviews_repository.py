from datetime import datetime, timedelta, timezone
from database.models import Review, Summary


class reviewsRepository:
    @staticmethod
    async def get_reviews_by_product(product_id: int, limit=None):
        return await Review.filter(product_id=product_id).order_by("created_at")[:limit]

    @staticmethod
    async def store_review_summary(product_id: int, summary: str):
        now = datetime.now()
        expires_at = now + timedelta(days=7)

        data = {
            "content": summary,
            "expires_at": expires_at,
            "generated_at": now,
            "product_id": product_id,
        }

        summary_obj = await Summary.get_or_none(product_id=product_id)
        if summary_obj:
            for key, value in data.items():
                setattr(summary_obj, key, value)
            await summary_obj.save()
        else:
            summary_obj = await Summary.create(**data)

        return summary_obj

    @staticmethod
    async def get_review_summary(product_id: int):
        now_utc = datetime.now(timezone.utc)
        summary_obj = await Summary.filter(
            product_id=product_id, expires_at__gt=now_utc
        ).first()
        return summary_obj.content if summary_obj else None
