# Rest API with JWT Authorization and Custom Asynchronous Middleware

## **Overview**
This project demonstrates the implementation of a **REST API** that uses **JSON Web Tokens (JWT)** for secure authorization. It also includes a **custom asynchronous middleware** to handle external API connections and data processing efficiently.

---

## **Features**
- **JWT Authorization:** Secure and scalable token-based authentication system.
- **Custom Asynchronous Middleware:** Enhances performance by handling external API calls asynchronously.
- **External API Integration:** Demonstrates how to fetch and use data from third-party APIs seamlessly.
- **Error Handling:** Provides robust error handling for API requests and middleware operations.
- **PostgreSQL Database:** Robust and scalable database used for storing API data and user information.

---

## **Technologies Used**
- **Python** (v3.x)
- **Django REST Framework** (DRF)
- **PostgreSQL** (Database)
- **JWT Authentication** (via `djangorestframework-simplejwt`)
- **Asynchronous Programming** (via `asyncio` and `aiohttp`)
- **Git for Version Control**

---

## **Setup and Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/shubham-patil-98/Rest-Api-with-JWT-and-Custom-Asynchronous-Middleware.git
   cd Rest-Api-with-JWT-and-Custom-Asynchronous-Middleware

2. **Create and Activate a Virtual Environment:**
    python3 -m venv rest_api_env
    source rest_api_env/bin/activate

3. **Install Dependencies:**
    pip install -r requirements.txt

4. **Run Migrations:**
    python manage.py makemigrations
    python manage.py migrate

5. **Start the Server:**
    python manage.py runserver

## **How It Works**

### **JWT Authentication**
- Users must authenticate using their credentials to obtain a JWT token.
- Include the JWT token in the Authorization header (`Authorization: Bearer <token>`) for secured API access.

### **Custom Asynchronous Middleware**
- The middleware intercepts incoming requests to make external API calls asynchronously.
- Middleware attaches the fetched external API data to the request object, making it accessible in the views.

---

## **Endpoints**

| Method | Endpoint             | Description                              | Authorization Required |
|--------|-----------------------|------------------------------------------|------------------------|
| POST   | `/api/token/`         | Obtain JWT token                         | No                     |
| POST   | `/api/token/refresh/` | Refresh JWT token                        | No                     |
| GET    | `/api/tasks/`         | Fetch a list of tasks                    | Yes                    |
| GET    | `/api/external-data/` | Fetch external API data using middleware | Yes                    |

---

## **Example Usage**

### **1. Obtain JWT Token**
Use the following endpoint to obtain a JWT token:
```bash
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=<your_username>&password=<your_password>"
```
### **2. Access Protected Endpoints**
Pass the JWT token in the Authorization header:
```bash
curl -H "Authorization: Bearer <your_jwt_token>" http://127.0.0.1:8000/api/tasks/
```