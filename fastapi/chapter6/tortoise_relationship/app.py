from typing import List, Tuple

from fastapi import Depends, FastAPI, HTTPException, Query, status
from tortoise.contrib.fastapi import register_tortoise
from tortoise.exceptions import DoesNotExist

from models import (
    CommentBase,
    CommentTortoise,
    PostDB,
    PostCreate,
    PostPartialUpdate,
    PostTortoise,
    CommentDB
)

app = FastAPI()


async def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_post_or_404(id: int) -> PostTortoise:
    try:
        return await PostTortoise.get(id=id).prefetch_related("comments")
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/posts")
async def list_posts(pagination: Tuple[int, int] = Depends(pagination)) -> List[PostDB]:
    skip, limit = pagination
    posts = await PostTortoise.all().offset(skip).limit(limit)

    results = [PostDB.model_validate(post) for post in posts]

    return results


@app.get("/posts/{id}", response_model=PostDB)
async def get_post(post: PostTortoise = Depends(get_post_or_404)) -> PostDB:
    return PostDB.model_validate(post)


@app.post("/posts", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate) -> PostDB:
    post_tortoise = await PostTortoise.create(**post.model_dump())

    return PostDB.model_validate(post_tortoise)


@app.patch("/posts/{id}", response_model=PostDB)
async def update_post(
    post_update: PostPartialUpdate, post: PostTortoise = Depends(get_post_or_404)
) -> PostDB:
    post.update_from_dict(post_update.model_dump(exclude_unset=True))
    await post.save()

    return PostDB.model_validate(post)


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post: PostTortoise = Depends(get_post_or_404)):
    await post.delete()

@app.post("/comments", response_model=CommentDB, status_code=status.HTTP_201_CREATED)
async def create_comment(comment: CommentBase) -> CommentDB:
    try:
        await PostTortoise.get(id=comment.post_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Post {id} does not exist"
        )
    comment_tortoise = await CommentTortoise.create(**comment.model_dump())
    return CommentDB.model_dump(comment_tortoise)


TORTOISE_ORM = {
    "connections": {"default": "sqlite://chapter6_tortoise_relationship.db"},
    "apps": {
            "models": {
                "models": ["models", "aerich.models"],
                "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)