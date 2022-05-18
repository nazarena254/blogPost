import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_naz = User(first_name = "Nazarena",
                                last_name = "Wambura",
                                username = "nazarena",
                                password = "naz123",
                                email = "mnazwambura@mail.com")
        self.new_post = Post(post_title = "Tech",
                            post_content = "practice for mastery",
                            user_id = self.user_Collins.id)
        self.new_comment = Comment(comment = "great one",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Collins.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_naz, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))