"""
this provides the post class which is used to store the data for a scraped post
"""


class Post:
    __doc__ = """
    Post class

    Attributes
    ----------
    id : str
        the id of the post
    reddit_id : str
        the reddit id of the post
    permalink_url : str
        the permalink url of the post
    title : str
        the title of the post
    is_nsfw : bool
        whether or not the post is nsfw
    access_date : datetime
        the date and time the post was accessed
    post_type : str
        the type of post, either submission or comment
    post_content_type : str
        the type of content in the post, either text, image, video, gif, link, or embed
    post_content : str
        the content of the post
    tags : list
        a list of strings containing the tags for the post
    """

    reddit_id = ''
    permalink_url = ''
    title = ''
    is_nsfw = False
    access_date = ''
    post_type = ''
    post_content_type = ''
    post_content = ''
    tags = []

    # functions

    def __init__(self, reddit_id, permalink_url, title, is_nsfw, access_date, post_type, post_content_type, post_content, tags):
        # initialize the class attributes
        self.reddit_id = reddit_id
        self.permalink_url = permalink_url
        self.title = title
        self.is_nsfw = is_nsfw
        self.access_date = access_date
        self.post_type = post_type
        self.post_content_type = post_content_type
        self.post_content = post_content
        self.tags = tags

    def __str__(self):
        # return a string representation of the class
        return f"""
        Post(
            reddit_id={self.reddit_id},
            permalink_url={self.permalink_url},
            title={self.title},
            is_nsfw={self.is_nsfw},
            access_date={self.access_date},
            post_type={self.post_type},
            post_content_type={self.post_content_type},
            post_content={self.post_content},
            tags={self.tags},
        )
        """

    def get_tags(self):
        """return the tags for the post

        Returns:
            list: a list of strings containing the tags for the post
        """
        return self.tags

    def set_tags(self, tags):
        """set the tags for the post

        Args:
            tags (list): a list of strings containing the tags for the post
        """
        self.tags = tags
