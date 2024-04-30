#!/usr/bin/env python3
import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs

    get_count = db.nginx.count_documents({"method": "GET"})
    post_count = db.nginx.count_documents({"method": "POST"})
    put_count = db.nginx.count_documents({"method": "PUT"})
    patch_count = db.nginx.count_documents({"method": "PATCH"})
    delete_count = db.nginx.count_documents({"method": "DELETE"})
    status_count = db.nginx.count_documents({"method": "GET",
                                             "path": "/status"})

    print(db.nginx.count_documents({}), "logs")
    print("Methods:")
    print(f"\t method GET: {get_count}")
    print(f"\t method POST: {post_count}")
    print(f"\t method PUT: {put_count}")
    print(f"\t method PATCH: {patch_count}")
    print(f"\t method DELETE: {delete_count}")
    print(f"{status_count} status check")
