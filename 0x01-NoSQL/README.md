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

---

### [10. Change school topics](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/10-update_topics.py)
Write a Python function that changes all topics of a school document based on the name:

Prototype: `def update_topics(mongo_collection, name, topics)`:
`mongo_collection` will be the `pymongo` collection object
`name` (string) will be the school name to update
`topics` (list of strings) will be the list of topics approached in the school

---

### [11. Where can I learn Python?](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/11-schools_by_topic.py)
Write a Python function that returns the list of school having a specific topic:

Prototype: `def schools_by_topic(mongo_collection, topic):`
`mongo_collection` will be the `pymongo` collection object
`topic` (string) will be topic searched

---

### [12. Log stats](https://github.com/ehabsmh/alx-backend-storage/blob/main/0x01-NoSQL/12-log_stats.py)
Write a Python script that provides some stats about Nginx logs stored in MongoDB:

- Database: `logs`
- Collection: `nginx`
- Display (same as the example):
  - first line: `x logs` where `x` is the number of documents in this collection
  - second line: `Methods:`
  - 5 lines with the number of documents with the `method` = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
  - one line with the number of documents with:
    - `method=GET`
    - `path=/status`

You can use the dump in the current directory as data sample.

The output of your script must be exactly the same as the example.
