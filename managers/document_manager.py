"""
Brief summary of the class's purpose.

Detailed explanation of the class's behavior, its role within the larger application, and how it interacts with other classes or data.

Parameters
----------
param1 : type
    Description of param1, including any constraints or required formats.
param2 : type
    Description of param2, including any constraints or required formats.
...

Attributes
----------
attr1 : type
    Description of attr1, including any default values.
attr2 : type
    Description of attr2, including any default values.
...

Methods
-------
method1
    Brief description of method1.
method2
    Brief description of method2.
...

Example
-------
>>> ClassName(param1, param2)
Expected result

Notes
-----
Any additional notes on the class's usage within the broader application.
"""

import pickle

class DocumentManager:
    def __init__(self):
        self.documents = {}

    def add_document(self, document_id: str, document) -> None:
        pass

    def mount_document(self, document_id):
        pass

    def unmount_document(self, document_id):
        pass

    def remove_document(self, document_id):
        pass

    def get_loaded_documents(self):
        return self.documents.keys()