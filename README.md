# Twitter Dashboard

Twitter Dashboard is project that integrates twitter API, to fetch user's timeline tweets and what is trending globally. For now, It is using only the timeline api and trend api. 
The application has a django-celery beat that schedules periodic celery workers to make an api call after 10 minutes. Twitter api has rate limiting therefore to avoid exceeding the limit. api call is scheduled after 10 minutes of subsequent calls.

## Usage
```bash
   python -m pip install -r requirements.txt
```
This will install all the dependacy of the project from requirements.txt in the project folder

You need to have setup developer account from twitter developers inorder to get the API credentials and use it for your authentiacation and authorization when making an api call.

With the credentials acquired use it in the settings.py 

```python
#settings.py
API_KEY = *****
API_SECRET_KEY = *****
CONSUMER_KEY = ******
CONSUMER_KEY_SECRET = ********
```
NB:- Do not push your credentials on github, they will be exposed to the public. Put them in an environmet variable


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Roadmap
The following is will features will be added in future.
   - Fetching data from another user's timeline
   - Creating listeners to fetch tweets with specific words
   - Video and image downloaders. to fetch videos on user's timeline.

## Project status
This project is still on development