from django.db import models
from django_extensions.db.fields import json

import markdown, re


def parse_comment(text):
    return markdown.markdown(text, safe_mode='remove')

class Post(models.Model):
    submission = json.JSONField()
    parent = json.JSONField()
    comment = json.JSONField()
    created = models.IntegerField()

    def comment_to_html(self):
        return parse_comment(self.comment.get('body'), display_images=True)

    def comment_img_src(self):
        match = re.search('http://.*\.jpg', self.comment.get('body'))
        if match:
            return match.group()

    def parent_as_title(self):
        if self.parent.get('body') != self.comment.get('body'):
            return parse_comment(self.parent.get('body'))
        else:
            return self.submission.get('title')

    def is_simple_image_post(self):
        return self.comment_img_src() is not None

    def get_context_url(self):
        link = self.submission.get('permalink')
        comment_id = self.comment.get('id')#.split('_')[1]
        return "http://reddit.com/{}/{}/?context=2".format(link,comment_id)


    def __str__(self):
        return "%s -> %s" % (self.parent.get('body'), self.comment.get('body'))

    class Meta:
        ordering = ('-created',)
