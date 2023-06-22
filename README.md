# Weblab Backend Task

## Requirements

The requirements for this project are listed in the `requirements.txt` file. You can install all the necessary packages by running the following command:

```
pip install -r requirements.txt
```

## Starting the App

To start the app, run the following command: `python app.py`

This will start the Flask server on `localhost:5000`. You can access the website by opening a web browser and navigating to `http://localhost:5000`.

**Admin username is "admin", password is "skylab".**

## Routes

### /auth/login (POST)

Authenticates a user and generates an access token.

**Request Body:**

- **username (str)**: The username of the account.
- **password (str)**: The password of the account.

### /auth/create (POST)

Creates a new panel account.
**Requires a valid JWT token with admin privileges.**

**Request Body:**

- **username (str)**: The username of the account.
- **password (str)**: The password of the account.
- **is_admin (bool)**: Indicates whether the account has admin privileges.

### /applications/apply (POST)

Submits a application form.

**Request Body:**

- **email (str)**: The email of the applicant.
- **phone_number (str)**: The phone number of the applicant.
- **form_data (dict)**: The data submitted in the form.#/form/get-applications

### /applications/get (POST)

Retrieves all application forms.
**Requires a valid JWT token for authentication.**

### /applications/edit (POST)

Edits a application form.
**Requires a valid JWT token with admin privileges.**

**Request Body**:

- **id (int)**: The ID of the application form.
- **email (str)**: **(Optional)** The updated email of the applicant.
- **phone_number (str)**: **(Optional)** The updated phone number of the applicant.
- **form_data (dict)**: **(Optional)** The updated form data.

### /applications/delete (POST)

Deletes a application form.
**Requires a valid JWT token with admin privileges.**

**Request Body**:

- **id (int)**: The ID of the application form to delete.

### /inputs/get (POST)

Retrieves all inputs.

### /inputs/add (POST)

Adds a new input field to the form.
**Requires a valid JWT token for authentication.**

**Request Body**:

- **name (str)**: The name of the input field.
- **placeholder (str)**: The placeholder text for the input field.

### /inputs/update (POST)

Updates an existing input field in the form.
**Requires a valid JWT token for authentication.**

**Request Body**:

- **id (int)**: The ID of the input field to update.
- **name (str)**: **(Optional)** The updated name of the input field.
- **placeholder (str)**: **(Optional)** The updated placeholder text for the input field.

### /inputs/delete (POST)

Deletes an input field from the form.
**Requires a valid JWT token with admin privileges.**

**Request Body**:

- **id (int)**: The ID of the input field to delete.
