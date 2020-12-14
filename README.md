# Watson NLP

Car purchase recommendation engine that uses *Natural Language Processing* and *Speech-to-Text* in text and audio files to recognize a customer comment and recommend a car based on the perceived sentiment.

## Getting Started

Clone the repository:

```bash
git clone git@github.com:Trowsing/watson-nlp.git
cd watson-nlp
```

Create the environment:

```bash
pipenv install
pipenv shell
```

*API keys, URIs and Watson models must be provided as env vars.*

|   Variable    |
| :-----------: |
| `NLU_API_KEY` |
|   `NLU_URL`   |
|  `NLU_MODEL`  |
| `STT_API_KEY` |
|   `STT_URL`   |


Run the application:

```export FLASK_APP=fiat_nlp/app.py && flask run```

Or run the `gunicorn` server:

```gunicorn --chdir fiat_nlp/ app:app```

---

## Text and audio processing

`POST` *http://localhost:5000/nlp*

The `/nlp` endpoint receives a request containing either an audio file or text.

**Params** (*multipart/form-data*):

|  Param  |        Type         |         Description         |
| :-----: | :-----------------: | :-------------------------: |
| `text`  |         str         |    Customer comment text    |
| `audio` | audio binary (flac) | Customer comment audio file |
|  `car`  |         str         |   Current customer's car    |

**Response** (*application/json*):

|      Value       | Type  |           Description            |
| :--------------: | :---: | :------------------------------: |
|    `entities`    | array | Entities detected in the comment |
| `recommendation` |  str  |    Car recommendation output     |
