# from document_management_3.project.category import Category
# from document_management_3.project.topic import Topic
# from document_management_3.project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        categ = [cat for cat in self.categories if cat.id == category_id][0]
        categ.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        doc = [d for d in self.documents if d.id == document_id][0]
        doc.file_name = new_file_name

    def delete_category(self, category_id):
        cat = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(cat)

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        dok = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(dok)

    def get_document(self, document_id):
        g_d = [d for d in self.documents if d.id == document_id][0]
        return g_d

    def __repr__(self):
        return "\n".join([d.__repr__() for d in self.documents])

# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
