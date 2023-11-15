
# Django Redis Caching Example

This project demonstrates implementing caching using Redis in a Django blog application.

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   https://github.com/DmitriyChebruchan/hillel-13
   cd blog
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows (using Command Prompt):
     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

1. Start the Redis server with Docker:
   ```bash
   docker run -p 6379:6379 redis
   ```

2. Run Django migrations:
   ```bash
   python manage.py migrate
   ```

3. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

4. Access the application at [http://localhost:8000](http://localhost:8000)

## Usage

- Visit `/blog/{post_id}/` to view a blog post by its ID.
- Edit a blog post at `/edit/{post_id}/`.
