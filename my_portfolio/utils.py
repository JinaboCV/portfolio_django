import math
from django.utils.html import strip_tags

""" Utility functions """
def calculate_read_time(content):
    text = strip_tags(content)  # Remove HTML tags
    word_count = len(text.split())
    read_time_min = math.ceil(word_count / 200)  # average reading speed
    return read_time_min