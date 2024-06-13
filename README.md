### WebGame Project with Docker Integration

#### Overview
The WebGame project is a web-based platform that allows users to register, log in, and access a variety of online games. The project uses Flask for the backend, MongoDB for data storage, and includes a Docker setup to simplify deployment and ensure consistent environments across development and production.

#### Features
1. **User Registration**: Allows new users to sign up by providing a username, email, and password.
2. **User Login**: Enables registered users to log in using their username and password.
3. **Game Dashboard**: Provides access to a variety of online games after logging in.
4. **Password Visibility Toggle**: Users can toggle the visibility of passwords during registration and login.
5. **Responsive Design**: Ensures usability across different devices.
6. **Docker Integration**: Utilizes Docker to create a containerized environment for easy deployment and consistency.

#### File Structure
- **app.py**: The main Flask application file containing routes and database interactions.
- **Dockerfile**: Defines the Docker image for the Flask application.
- **docker-compose.yml**: Configures the Docker services for the application and MongoDB.
- **requirements.txt**: Lists the dependencies for the Flask application.
- **templates/**: Directory containing HTML templates for different pages.
  - `login.html`: Template for the login page.
  - `register.html`: Template for the registration page.
  - `index.html`: Template for the game dashboard page.
- **static/**: Directory containing static files such as images and CSS.
  - `favicon.ico`: The website's favicon.
  - `webgamelogin.jpg`: Background image for the login page.
  - `background.jpg`: Background image for the landing page.
  - `logo.jpg`: Logo used in the navbar and other sections.
  - `mario.jpg`, `pacman.jpg`, `2048.jpg`, `contra.jpg`: Images for featured games.
  - `webgameimage.webp`: Background image for the account features section.
- **style.css**: CSS file for styling the web pages.

#### Installation and Setup

##### Prerequisites
- Docker and Docker Compose installed on your machine.

##### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sandeshpp17/WebGames
   cd webgame
   ```

2. **Build and Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```
   This command builds the Docker image and starts the Flask application along with MongoDB in separate containers.

3. **Access the Application**:
   The application will be accessible at `http://127.0.0.1:5000/`.

#### Docker Configuration

- **Dockerfile**:
  ```dockerfile
  FROM python:3.9-slim

  WORKDIR /app

  COPY requirements.txt requirements.txt
  RUN pip install -r requirements.txt

  COPY . .

  CMD ["python", "app.py"]
  ```

- **docker-compose.yml**:
  ```yaml
  version: '3.8'

  services:
    web:
      build: .
      ports:
        - "5000:5000"
      depends_on:
        - mongo

    mongo:
      image: mongo
      ports:
        - "27017:27017"
  ```

#### Usage
- **Register**: Navigate to `/register`, fill in the registration form, and submit.
- **Login**: Navigate to `/`, enter your credentials, and log in.
- **Dashboard**: After logging in, you will be redirected to `/index` where you can view and play featured games.

#### Routes and Endpoints
- **GET /**: Renders the login page.
- **GET /register**: Renders the registration page.
- **POST /register**: Handles user registration.
- **POST /login**: Handles user login.
- **GET /index**: Renders the game dashboard after successful login.
- **GET /images/<filename>**: Serves static image files.

#### Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

This summary provides an overview of the WebGame project, detailing its features, file structure, setup instructions, and usage with Docker integration. It is intended to help users and contributors understand the project and get started quickly.
