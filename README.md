**API of a twitter-like application using FastAPI.
**
Users can log into the application and create a post and like other users' posts. 
Users can also delete their posts. 
User data is stored in a postgres database using SQLAlchemy as the Object Relational Mapper.

**There are four routes in this API:
**
1. The post route: for creating, updating and deleting posts.
2. The users route: For creating the users and searching for users by username.
3. The auth route: For authenticating each user using JWT token.
4. The vote route: For liking a post and cancelling it.

**How to Run locally**
1. You can run this project by cloning the repository and installing fastapi using "pip install fastapi[all]". Of course, you should have python >= 3.10 installed.
2. Then, you can run the application using uvicorn main:app --reload
3. Routes can be manually tested using the interactive api documentation provided by OpenAPI using Swagger UI or by using Postman by going to the link: http://127.0.0.1:8000/docs.

You can run a local postgres database by using your local environment and connecting it to Postgres using your environment variables.
