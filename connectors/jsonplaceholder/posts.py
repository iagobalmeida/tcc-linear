from .req import get

def publicize_post(post):
    return {
        "id": post["id"],
        "title": post["title"],
        "body": post["body"]
    }

def get_posts_from_user(user_id):
    all_posts = get('posts')
    return [post for post in all_posts if post['user_id'] == user_id]

def get_post_details(post_id):
    all_posts = get('posts')
    post_comments = get(f'posts/{post_id}/coments')
    if post_id not in all_posts: return None
    post = publicize_post(all_posts[post_id])
    post['comments'] = post_comments
    return post