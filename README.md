# Financial-Management-System-Backend

This platform is used to track financial savings for individuals that signup and their savings on the platform.

## The Tech Stack

### FrameWork

The backend framework used in this project is FastAPI, a modern, high-performance Python framework for building APIs. You can learn more about FastAPI by checking out their [documentation](https://fastapi.tiangolo.com/)

### ORM

This project uses SQLAlchemy as the ORM (Object-Relational Mapping) tool for database interactions.

### Getting your Project to run

After you have clone this repo you can `cd` into the directory `Financial-Management-System-Backend` and create your virtual enviroment
to do this you can run

```bash
python3 -m venv venv
```

To run your virtual enviroment

if you're on

- Linux

```bash
source venv/bin/activate
```

- Windows

```bash
source venv\Scripts\activate
```

After this you can install the project requirements by installing the requirements.txt

```bash
pip install -r requirements.txt
```

## Setting up your Database

Firstly install Postgres 17

you can follow this [documentation](https://www.postgresql.org/download/) to install

leave the username as default while setting up postgres
`postgres` password `password123`

Next Create a database in postgres called `finance.db`

You will need to manually create super user in the user table of your database

- 1 Set the email

- 2 set the password: To set the password you have to vist [bcrypt Generator online](https://bcrypt.online) to generate the password hash

![Doc Image](https://github.com/sir-george2500/custome_images/blob/main/images/doc_pic.png)

Provide a plain text input set the `cost` to 12 as shown in the image
then press the generate button to generate the password hash. Then copy the hash
and paste it in the password field of the table.

- 3 set the username, firstname and lastname field then set the role to Admin
  also set both the `created_at` and `update_at` to the `now()` function

- 4 Save the record and ensure that the information is in the database by runing

```bash
SELECT * FROM users;
```

To run your project you can run the below command

```bash
uvicorn main:app --reload
```
