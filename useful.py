"""
This file has functions that can be used on the daily basis.
"""


def delete_duplicates(model_name):
    """This function deletes duplicates from a model on the database.
        It takes a ModelName as argument.
    """
    deleted = 0
    for row in model_name.objects.all():
        if model_name.objects.filter(isbn_13=row.isbn_13).count() > 1:
            model_name.delete()
            deleted += 1
    print(f"deleted: {deleted}")