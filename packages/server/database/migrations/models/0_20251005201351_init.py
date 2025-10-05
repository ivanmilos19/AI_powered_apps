from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `products` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `description` LONGTEXT,
    `price` DOUBLE NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `reviews` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `author` VARCHAR(255) NOT NULL,
    `rating` INT NOT NULL,
    `content` LONGTEXT NOT NULL,
    `created_at` DATETIME(6) NOT NULL,
    `product_id` INT NOT NULL,
    CONSTRAINT `fk_reviews_products_9251a0c3` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `summaries` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `content` LONGTEXT NOT NULL,
    `generated_at` DATETIME(6) NOT NULL,
    `expires_at` DATETIME(6) NOT NULL,
    `product_id` INT NOT NULL UNIQUE,
    CONSTRAINT `fk_summarie_products_805804a4` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
