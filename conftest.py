import pytest

def pytest_addoption(parser):
    parser.addoption("--config_url", action="store", default="https://jsonplaceholder.typicode.com")

def pytest_configure(config):
    pytest.config_url = config.getoption('config_url')

def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test classes run in a given order. Controls sequential execution if needed."""
    CLASS_ORDER = [
                "TestUserCanGetUsers", 
                "TestUserCanGetAllPosts",
                "TestUserCanGetSinglePostById",
                "TestUserCanCreatePost",
                "TestUserCanUpdatePosts"
    ]

    class_mapping = {item: item.cls.__name__ for item in items}
    print (class_mapping)

    sorted_items = items.copy() # Take a copy of the list

    # Iteratively move tests of each class to the end of the test queue
    for class_ in CLASS_ORDER:
        sorted_items = [it for it in sorted_items if class_mapping[it] != class_] + [
            it for it in sorted_items if class_mapping[it] == class_
        ]

    items[:] = sorted_items
