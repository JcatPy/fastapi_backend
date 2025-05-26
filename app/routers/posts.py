from fastapi import APIRouter, Depends, HTTPException, FastAPI, status, Response
from sqlmodel import Session, select
from ..database import get_session
from ..Schemas import PostCreate, PostUpdate
from ..model import Post
from ..oauth2 import get_current_user

router = APIRouter()

@router.get("/posts", response_model=list[Post])
def read_posts(session: Session = Depends(get_session)):
    posts = session.exec(select(Post)).all()
    print("Fetched posts:", posts)
    return posts

@router.post("/posts", response_model=Post)
def create_post(post: PostCreate, session: Session = Depends(get_session), get_current_user: int = Depends(get_current_user)):
    print(get_current_user)
    new_post = Post(**post.dict())
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post


@router.get("/posts/{post_id}", response_model=Post)
def read_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/posts/{post_id}", response_model=Post)
def delete_post(post_id: int, session: Session = Depends(get_session), get_current_user: int = Depends(get_current_user)):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    session.delete(post)
    session.commit()
    return post

@router.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post_update: PostUpdate, session: Session = Depends(get_session),
                get_current_user: int = Depends(get_current_user)):
    db_post = session.get(Post, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Only update fields that were actually provided
    post_data = post_update.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_post, key, value)

    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post



@router.get("/")
def root():
    return {"status": "API is running"}




# The below code is crud operations for posts using psycopg2(or raw sql queries)
'''
# Define a Pydantic model for the request body
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

# Database connection
while True:
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(host='localhost', port = 3453, database='fastapi', user='postgres', password='Student@eacc18')
        # Create a cursor to execute SQL queries
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        print("Database connection successful")
        break
    except Exception as error:
        print("Connection to database failed")
        print(error)
        time.sleep(2)


@app.get("/posts")
def root():
    # Fetch all posts from the database
    cursor.execute("SELECT * FROM posts")
    # Fetch all rows from the result set
    posts = cursor.fetchall()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts found")
    return {"message": posts}


@app.post("/posts")
def create_post(post: Post):
    if not post.title or not post.content:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Title and content are required")
    cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", (post.title, post.content, post.published))
    # Fetch the newly created post
    new_post = cursor.fetchone()
    # Commit the transaction
    conn.commit()
    return {"message": new_post}

@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("select * from posts where id = %s", (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return {"message": post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (id,))
    deleted_post = cursor.fetchone()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int , post: Post):
    cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, id))
    post_dict = cursor.fetchone()
    if not post_dict:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    # Commit the transaction
    conn.commit()
    return {"message": post_dict}
'''