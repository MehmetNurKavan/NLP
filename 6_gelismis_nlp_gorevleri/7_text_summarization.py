#%% Import the summarization pipeline from the Hugging Face transformers library

from transformers import pipeline

#%% ozetleme pipline yukle

summarizer = pipeline("summarization")

text = """
Peter Pan was a magical boy who lived in Neverland, a place where children never grow up and adventures never end. Unlike other children, Peter could fly, fight pirates, and talk to magical creatures. One evening, while flying over London, he met a curious girl named Wendy and invited her and her brothers to Neverland.
In Neverland, Peter introduced Wendy to his loyal companion, a tiny fairy named Tinker Bell. Tinker Bell was brave, clever, and a little jealous, especially when Peter gave Wendy too much attention. Despite this, Tinker Bell always helped Peter and protected their home from danger.
Together, Peter, Tinker Bell, and the Lost Boys battled the evil Captain Hook and his crew of pirates. Tinker Bell once risked her life to save Peter from a deadly trap, proving her deep loyalty. With courage, teamwork, and a bit of fairy dust, they defeated the pirates and kept Neverland safe.
As time passed, Wendy missed her family and chose to return home, but Peter and Tinker Bell stayed behind. Peter still refused to grow up, and Tinker Bell remained his closest friend, flying beside him through the skies of Neverland. Their magical adventures continued, reminding everyone that with imagination, friendship, and a little bit of faith, anything is possible.
"""

#%% metin ozetle

summary = summarizer(
    text,
    max_length = 100, 
    min_length = 30, 
    do_sample = False,
    )
print(summary[0]["summary_text"])



"""
do_sample = False 

Peter Pan was a magical boy who lived in Neverland, 
a place where children never grow up and adventures never end .
Peter, Tinker Bell, and the Lost Boys battled the evil 
Captain Hook and his crew of pirates . 
Together, they defeated the pirates and kept Neverland safe .
"""

"""
do_sample = True

Peter Pan was a magical boy who lived in Neverland, 
a place where children never grow up and adventures never end .
Peter, Tinker Bell, and the Lost Boys battled the evil 
Captain Hook and his crew of pirates . 
With courage, teamwork, and a bit of fairy dust, 
they defeated the pirates 

"""
