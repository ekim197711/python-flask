import unittest
from pymongo import MongoClient
from bson.objectid import ObjectId

class MyTestCase(unittest.TestCase):
    def dummyspaceships(self):
        return [
            {'name':'Falcon', 'crew': 100},
            {'name':'Eagle', 'crew': 2500},
            {'name':'Black bird', 'crew': 42},
            {'name':'Stork', 'crew': 12},
            {'name':'Flamingo', 'crew': 5}
        ]

    def test_createSpaceship(self):
        client = MongoClient(host="localhost", port=27017)
        db = client.space
        spaceships = db.spaceships
        spaceships.delete_many({})
        spaceships.insert_many(self.dummyspaceships())

        allspaceships = spaceships.find({'crew': {'$gt': 10}})
        for ship in allspaceships:
            print(f'Ship { str(ship) }')

        # onespaceship = spaceships.find_one({'_id': ObjectId('5db8a4cf2728d1296aa37158')})
        # print('One Ship {}'.format(str(onespaceship)))


if __name__ == '__main__':
    unittest.main()
