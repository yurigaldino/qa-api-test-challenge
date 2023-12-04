# qa-api-test-challenge (an API Testing Project)

This project is an API testing framework using Newman and Postman for testing the "reqres.in" API.

## Setup

### Prerequisites

- Node.js and npm installed on your machine.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yurigaldino/qa-api-test-challenge.git
```

2. Install Newman and the "htmlextra" reporter:

```bash
npm install -g newman newman-reporter-htmlextra
```
## Running Tests
Run the API tests using Newman (only .json Postman collection file with API test cases needed):

```bash
newman run qa-api-test-challenge-collection.json -r htmlextra
```
_This will only generate an HTML test report._


Or run the following command to execute the tests:

```bash
python qa-api-test-challenge.py
```
_This will execute the tests and generate an HTML test report._

## Project Structure
qa-api-test-challenge-collection.json: Postman collection file with API test cases.

Contributing
yurifgdesouza@gmail.com
