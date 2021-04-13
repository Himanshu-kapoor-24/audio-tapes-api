# Filed - Audio Tapes API
Provide Endpoints to perform CRUD operation(s) on audio tape(Song, Podcast, Audiobook)

Requirements:-
1. PostgreSQL - version 12
2. Django - version 3.2

Song Model Fields:-
  - id = primary key, integer, unique, mandatory
  - audio_file_type = charfield, mandatory, max length=100
  - song_name = charfield, mandatory, max length=100
  - duration = integerfield, mandatory
  - uploaded_date = datetimefield, mandatory, validator:date cannot be in the past

Podcast Model Fields:-
  - id = primary key, integer, unique, mandatory
  - audio_file_type = charfield, mandatory, max length=100
  - podcast_name = charfield, mandatory, max length=100
  - duration = integerfield, mandatory
  - uploaded_date = datetimefield, mandatory, validator:date cannot be in the past
  - host = charfield, mandatory, max length=100
  - participants = array of charfields with max length=100, optional, size=10

Audiobook Model Fields:-
  - id = primary key, integer, unique, mandatory
  - audio_file_type = charfield, mandatory, max length=100
  - title = charfield, mandatory, max length=100
  - author = charfield, mandatory, max length=100
  - narrator = charfield, mandatory, max length=100
  - duration = integerfield, mandatory
  - uploaded_date = datetimefield, mandatory, validator:date cannot be in the past
  
Query Paramters:-
* audioFileType- 
    - allowed values= Song | Podcast | Audiobook 
    - must be string
* audioFileID- 
    - must be integer
    
Endpoints:-
1. Endpoint to CREATE an audio file of a specific type - localhost:8000/filed/<audioFileType>
  - Method - POST
  
2. Endpoint to READ all audio files of a specific type - localhost:8000/filed/<audioFileType>
  - Method - GET

3. Endpoint to READ a specific audio file of a specific type - localhost:8000/filed/<audioFileType>/<audioFileID>
  - Method - GET

4. Endpoint to UPDATE an audio file of a specific type - localhost:8000/filed/<audioFileType>/<audioFileID>
  - Method - PUT

5. Endpoint to DELETE an audio file of a specific type - localhost:8000/filed/<audioFileType>/<audioFileID>
  - Method - DELETE

Response of these endpoints:
* Action is successful: 200 OK
* The request is invalid: 400 bad request
* Any error: 500 internal server error

# note:-
* PostgreSQL database name, host, username, and password details are in a settings.py file. In case you have to need to change these details please must change in settings.py file.

