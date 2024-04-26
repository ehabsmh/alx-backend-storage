## Tasks
### [0. We are all unique!](https://github.com/ehabsmh/alx-backend-storage/0x00-MySQL_Advanced/0-uniq_users.sql)
Write a SQL script that creates a table users following these requirements:

With these attributes:
- id, integer, never null, auto increment and primary key.
- email, string (255 characters), never null and unique.
- name, string (255 characters).
- If the table already exists, your script should not fail
- Your script can be executed on any database.

Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application.

---

### [1. In and not out](https://github.com/ehabsmh/alx-backend-storage/0x00-MySQL_Advanced/1-country_users.sql)
Write a SQL script that creates a table users following these requirements:

With these attributes:
- id, integer, never null, auto increment and primary key
- email, string (255 characters), never null and unique
- name, string (255 characters)
- country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
- If the table already exists, your script should not fail

Your script can be executed on any database

---

### [2. Best band ever!](https://github.com/ehabsmh/alx-backend-storage/0x00-MySQL_Advanced/2-fans.sql)
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:

- Import this table dump: metal_bands.sql.zip
- Column names must be: origin and nb_fans
- Your script can be executed on any database

Context: Calculate/compute something is always power intensive… better to distribute the load!
---
### [3. Old school band](https://github.com/ehabsmh/alx-backend-storage/0x00-MySQL_Advanced/3-glam_rock.sql)

Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

Requirements:

- Import this table dump: [metal_bands.sql.zip](https://intranet.alxswe.com/rltoken/uPn947gnZLaa0FJrrAFTGQ)
- Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE())).
- You should use attributes formed and split for computing the lifespan.
- Your script can be executed on any database.

---

### [4. Buy buy buy](https://github.com/ehabsmh/alx-backend-storage/0x00-MySQL_Advanced/4-store.sql)
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table items can be negative.

Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

---

### [5. Email validation to sent](https://github.com/ehabsmh/alx-backend-storage/0x00-MySQL_Advanced/5-valid_email.sql)
Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

---

### [6. Add bonus](https://github.com/ehabsmh/alx-backend-storage/0x00-MySQL_Advanced/6-bonus.sql)
Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:

- Procedure AddBonus is taking 3 inputs (in this order):
    - user_id, a users.id value (you can assume user_id is linked to an existing users).
    - project_name, a new or already exists projects - if no projects.name found in the table, you should create it.
    - score, the score value for the correction.

Context: Write code in SQL is a nice level up!
