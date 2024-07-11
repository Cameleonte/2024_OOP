from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:

    def __init__(self) -> None:
        self.categories: list[Category] = []
        self.topics: list[Topic] = []
        self.documents: list[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __find_obj(obj_id: int, obj_collection: list):
        return next((o for o in obj_collection if o.id == obj_id), None)

    def edit_obj(self, obj_id: int, obj_collection: list, *new_values):
        curr_obj = self.__find_obj(obj_id, obj_collection)
        if curr_obj:
            curr_obj.edit(*new_values)

    def delete_obj(self, obj_id: int, obj_collection: list):
        curr_obj = self.__find_obj(obj_id, obj_collection)
        if curr_obj and curr_obj in obj_collection:
            obj_collection.remove(curr_obj)

    def edit_category(self, category_id: int, new_name: str):
        self.edit_obj(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.edit_obj(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.edit_obj(document_id, self.documents, new_file_name)

    def delete_category(self, category_id: int):
        self.delete_obj(category_id, self.categories)

    def delete_topic(self, topic_id: int):
        self.delete_obj(topic_id, self.topics)

    def delete_document(self, document_id: int):
        self.delete_obj(document_id, self.documents)

    def get_document(self, document_id: int):
        return self.__find_obj(document_id, self.documents)

    def __repr__(self):
        return '\n'.join([d.__repr__() for d in self.documents])
