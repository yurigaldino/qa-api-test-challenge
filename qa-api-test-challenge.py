import requests
import json
import unittest
import os
from sys import platform

class ReqresApiTest(unittest.TestCase):
    def test_1_retrieve_user_information(self):
        # Test Case 1: Retrieve a User (Positive Scenario)
        user_id = 1
        response = requests.get(f'https://reqres.in/api/users/{user_id}')

        # Validation
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('data', data)
        user_data = data['data']
        self.assertEqual(user_data['id'], user_id)
        self.assertEqual(response.reason, 'OK')

    def test_2_retrieve_invalid_user_information(self):
        # Test Case 2: Retrieve a User (Negative Scenario)
        invalid_user_id = 99999999
        response = requests.get(f'https://reqres.in/api/users/{invalid_user_id}')

        # Validation
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.reason, 'Not Found')

    def test_3_create_new_user(self):
        # Test Case 3: Create a New User
        user_data = {
            'name': 'Yuri Galdino',
            'job': '"QA Software Engineer"'
        }
        response = requests.post('https://reqres.in/api/users', json=user_data)

        # Validation
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertIn('id', data)
        self.assertEqual(data['name'], user_data['name'])
        self.assertEqual(data['job'], user_data['job'])
        self.assertEqual(response.reason, 'Created')

        # Report generation
        if platform == "linux" or platform == "linux2":
            os.system("newman run qa-api-test-challenge-collection.json -r htmlextra")
        elif platform == "win32":
            os.system("newman run qa-api-test-challenge-collection.json -r htmlextra")
        elif platform == "darwin":
            os.system("newman run qa-api-test-challenge-collection.json -r htmlextra")

if __name__ == '__main__':
    unittest.main()
    