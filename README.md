# Cemetery-Website

## Rigby Pioneer Cemetery Website

### Getting Started

1. Clone the repository: `git clone https://github.com/daxtonwirth/Cemetery-Website`
2. Change directories into the repository: `cd .\Cemetery-Website\`
3. Run the website: `python manage.py runserver`
4. Visit the website by clicking the link: `http://127.0.0.1:8000/`

### Managing website

- Admin page: http://127.0.0.1:8000/admin/
- Creating a superuser: `python3 manage.py createsuperuser`
- After Applying any changes: 
`python manage.py makemigrations website`
`python manage.py migrate`


### Creating SQLite database

1. Convert excel file to csv
2. Download DB browser for SQLite `https://sqlitebrowser.org/dl/`
3. Import existing db.sqlite3 database from Django
![image](https://user-images.githubusercontent.com/66894542/228933640-aabda19e-9256-4088-81d5-c4c70e0a09e9.png)
4. Import csv file as table

### Recreating database: 

1. Delete all the migration files in your app's migrations folder, except for the __init__.py file.
2. Delete the database file (usually db.sqlite3 in the project root directory).
3. Run python manage.py makemigrations command to create new migration files.
4. Run python manage.py migrate command to apply the migrations and create the new database file.
5. Create a superuser account using the createsuperuser command (python manage.py createsuperuser) to access the Django admin panel and add some data.
