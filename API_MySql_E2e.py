import requests

from API_DataDriven_MYSQL.Utilities.requirements import *

book_creation_endpoint=create_book_url()
book_creation_payload=createbook_payload()
book_creation_response=requests.post(book_creation_endpoint,json=book_creation_payload)
print(book_creation_response.status_code)
response_dic=book_creation_response.json()
unique_id=response_dic['ID']
book_deletion_endpoint=delete_book_url()
book_deletion_payload=deletebook_payload(unique_id)
book_deletion_response=requests.post(book_deletion_endpoint,json=book_deletion_payload)
print(book_deletion_response.status_code)
response_dic=book_deletion_response.json()
print(response_dic)
