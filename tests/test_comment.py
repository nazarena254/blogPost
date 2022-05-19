import unittest
from app.models import Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        
        self.new_comment = Comment(comment = "so inspiring",
                                    post_id = self.new_post.id,
                                    user_id = self.user_naz.id)

    def test_instance(self):
        
        self.assertTrue(isinstance(self.new_comment, Comment))