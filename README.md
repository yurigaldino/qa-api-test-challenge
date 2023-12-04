# qa-web-test-challenge (an API Testing Project)

This project is an API testing framework using Newman and Postman for testing the "reqres.in" API.

## Setup

### Prerequisites

- Node.js and npm installed on your machine.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yurigaldino/qa-api-test-challenge.git
```
2. Navigate to the project directory:

```bash
cd api-testing-project
```
3. Install Newman and the "htmlextra" reporter:

```bash
npm install -g newman newman-reporter-htmlextra
```
## Running Tests
Run the API tests using Newman:

```bash
newman run qa-api-test-challenge-collection.json -r htmlextra
```
This will execute the tests and generate an HTML test report.

Or run the following command to execute the tests:

```bash
python qa-api-test-challenge.py
```

## Project Structure
qa-api-test-challenge-collection.json: Postman collection file with API test cases.

Contributing
yurifgdesouza@gmail.com
