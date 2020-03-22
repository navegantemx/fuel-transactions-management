
# 1. Real MongoDB --> "Mocked" (faked)
# 2. Test Views, e.g. /get_receipts endpoint, /edit_receipt/<OBJECTID>
# .    - assert that either something changed in the database
#     - or an exception was raised and you were redirected
# 3. Test Functionality, test all functions which don't have to do with views, e.g. find_object

import unittest
import mongomock
from unittest import mock  # TODO: research mocking


class AppTests(unittest.TestCase):
    # These two will run at the beginning and end of all these tests (only once)
    @classmethod
    def setUpClass(cls) -> None:
        # flask_pymongo.PyMongo will be replaced by a fake client
        cls.patcher = mock.patch(
            'flask_pymongo.PyMongo', lambda app: mongomock.MongoClient())
        cls.patcher.start()
        # This will instantiate Mongo, so mongomock is required before
        from app import app
        cls.app = app.test_client()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.patcher.stop()

    # These two will run at the beginning and end of EACH test scenario
    # def tearDown(self):
    #     db['users'].remove()

    # def setUp(self):
    #     db['users'].save({...})

    # ------------------------------

    def test_get_receipts(self):
        # mongo.db.receipts.insert_one({....}})
        response = self.app.get('/get_receipts')
        self.assertEqual(response.status_code, 200)
        self.assertIn('a href="/get_sites">Manage Sites</a>', str(response.data))