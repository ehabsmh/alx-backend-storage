#!/usr/bin/env python3
import pymongo


client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client.logs

print(db.nginx.count_documents({}), "logs")
print("Methods:")
count_get_methods = db.nginx.count_documents({"method": "GET"})
count_post_methods = db.nginx.count_documents({"method": "POST"})
count_put_methods = db.nginx.count_documents({"method": "PUT"})
count_patch_methods = db.nginx.count_documents({"method": "PATCH"})
count_delete_methods = db.nginx.count_documents({"method": "DELETE"})
print("\t method GET:", count_get_methods)
print("\t method POST:", count_post_methods)
print("\t method PUT:", count_put_methods)
print("\t method PATCH:", count_patch_methods)
print("\t method DELETE:", count_delete_methods)
print(db.nginx.count_documents({
    "method": "GET",
    "path": "/status"
    }), "status check")
