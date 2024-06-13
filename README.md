### WebGame Project

#### Overview
The WebGame project is a web-based platform that provides users with the ability to register, log in, and access a variety of online games. The project uses Flask as the web framework and MongoDB for data storage. The user interface is designed with HTML, CSS, and JavaScript to create an engaging and user-friendly experience.

#### Features
1. **User Registration**: Allows new users to register by providing a username, email, and password.
2. **User Login**: Enables registered users to log in using their username and password.
3. **Game Dashboard**: Once logged in, users can access a dashboard with featured games.
4. **Password Visibility Toggle**: Users can toggle the visibility of passwords during registration and login.
5. **Responsive Design**: The website layout is designed to be responsive, ensuring usability across various devices.

#### File Structure
- **app.py**: The main Flask application file containing routes and database interactions.
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
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/webgame.git
   cd webgame
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`.

#### MongoDB Setup
Ensure MongoDB is installed and running. The connection string in `app.py` should be updated to match your MongoDB server settings:
```python
client = MongoClient('mongodb://your_mongo_host:your_mongo_port/webgamelogin')
```

#### Routes and Endpoints
- **GET /**: Renders the login page.
- **GET /register**: Renders the registration page.
- **POST /register**: Handles user registration.
- **POST /login**: Handles user login.
- **GET /index**: Renders the game dashboard after successful login.
- **GET /images/<filename>**: Serves static image files.

#### Usage
- **Register**: Navigate to `/register`, fill in the registration form, and submit.
- **Login**: Navigate to `/`, enter your credentials, and log in.
- **Dashboard**: After logging in, you will be redirected to `/index` where you can view and play featured games.

#### Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.


---

This summary provides an overview of the WebGame project, detailing its features, file structure, setup instructions, and usage. It is intended to help users and contributors understand the project and get started quickly.
