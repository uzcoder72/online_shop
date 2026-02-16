# Project Setup Instructions

## 1. Fix Python Environment
It seems your virtual environment might be broken or moved. To avoid the "Fatal error in launcher" issue, use `python -m pip` instead of just `pip`.

## 2. Install Dependencies
Run the following command in your terminal to install all necessary packages:

```powershell
python -m pip install -r requirements.txt
```

If you want to install them manually as you asked:
1. `python -m pip install Django==5.0.6`
2. `python -m pip install django-environ`
3. `python -m pip install psycopg2-binary`
4. `python -m pip install Pillow`

## 3. Configure Environment Variables
The project uses `django-environ` to manage settings.
1. Copy the file `env_doc` and rename it to `.env`.
2. Open `.env` and fill in your database details and secret key.

Example `.env` content (based on `env_doc`):
```
DEBUG=True
SECRET_KEY=your_secret_key_here
NAME=your_db_name
USER=your_db_user
PASSWORD=your_db_password
HOST=localhost
PORT=5432
```

## 4. Run the Server
Once dependencies are installed and `.env` is configured:

```powershell

## 5. Project Structure Overview
- **shop**: Contains the main e-commerce logic (Products, Categories, Orders).
- **customer**: Handles User authentication and profiles.
  - Unlike standard Django, this project uses a **Custom User Model** defined here.
  - This is why the `customer` app is critical for the entire site (login/register), even if other apps don't mistakenly import from it directly.

