## Tasks

### [0. List all databases](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/0-list_databases)
Lists all databases in MongoDB.

---

### [1. Create a database](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/1-use_or_create_database)
Creates or uses the database `my_db`.

---

### [2. Insert document](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/2-insert)
Inserts a document in the collection `school`:

- The document must have one attribute name with value “`Holberton school`”.
- The database name will be passed as option of mongo command.

---

### [3. All documents](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/3-all)
Write a script that lists all documents in the collection `school`:

- The database name will be passed as option of `mongo` command

---

### [4. All matches](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/4-match)
Write a script that lists all documents with `name="Holberton school"` in the collection `school`:

 - The database name will be passed as option of `mongo` command.

---

### [5. Count](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/5-count)
Write a script that displays the number of documents in the collection school:

 - The database name will be passed as option of mongo command

---

### [6. Update](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/6-update)
Write a script that adds a new attribute to a document in the collection `school`:

 - The script should update only document with `name="Holberton school"` (all of them).
 - The update should add the attribute `address` with the value “972 Mission street”.
 - The database name will be passed as option of `mongo` command.

---

### [7. Delete by match](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/7-delete)
Deletes all documents with `name="Holberton school"` in the collection `school`:

 - The database name will be passed as option of `mongo` command

---

### [8. List all documents in Python](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/8-all.py)
Write a Python function that lists all documents in a collection:

 - Prototype: def list_all(mongo_collection):
 - Return an empty list if no document in the collection
 - mongo_collection will be the pymongo collection object

---

### [9. Insert a document in Python](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/9-insert_school.py)
Write a Python function that inserts a new document in a collection based on `kwargs`:

Prototype: `def insert_school(mongo_collection, **kwargs)`:
`mongo_collection` will be the `pymongo` collection object
Returns the new `_id`
