from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "posts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "publication_date" TIMESTAMP NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "content" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "comments" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "publication_date" TIMESTAMP NOT NULL,
    "content" TEXT NOT NULL,
    "post_id" INT NOT NULL REFERENCES "posts" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
