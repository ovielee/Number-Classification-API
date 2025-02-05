
# Number Classification API

## Overview
The **Number Classification API** is a Flask-based web service that takes a number as input and returns interesting mathematical properties about it, along with a fun fact. The API is designed to be simple, fast, and easy to use.

## Endpoints

### URL Parameter Endpoint
- **Endpoint**: `/api/classify-number?number=<number>`
- **Method**: `GET`
- **Description**: Classifies a number and returns its mathematical properties and a fun fact.

### Query Parameter Endpoint
- **Example Request**:
  ```
  GET /api/classify-number?number=371
  ```

- **Example Response**:
  ```json
  {
      "number": 371,
      "is_prime": false,
      "is_perfect": false,
      "properties": ["armstrong", "odd"],
      "class_sum": 11,
      "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
  }
  ```

### Response Structure
The API returns a JSON object with the following fields:
- `number`: The input number.
- `is_prime`: `true` if the number is prime, otherwise `false`.
- `is_perfect`: `true` if the number is perfect, otherwise `false`.
- `properties`: A list of properties of the number (e.g., "prime", "perfect", "armstrong", "even", "odd").
- `class_sum`: The sum of the digits of the number.
- `fun_fact`: A fun fact about the number fetched from the [Numbers API](http://numbersapi.com/).

## Number Properties
The API checks for the following properties of a number:
- **Prime**: A number greater than 1 that has no divisors other than 1 and itself.
- **Perfect**: A number that is equal to the sum of its proper divisors (e.g., 6 = 1 + 2 + 3).
- **Armstrong**: A number that is equal to the sum of its own digits each raised to the power of the number of digits (e.g., 371 = 3^3 + 7^3 + 1^3).
- **Even/Odd**: A number is even if it is divisible by 2, otherwise it is odd.

## Tools
- **Programming Language**: Python
- **Framework**: Flask
- **API Documentation**: Swagger (optional)
- **Version Control**: Git
- **Deployment Platform**: Vercel

## Dependencies
The project relies on the following Python libraries:
- `Flask`: For building the web API.
- `requests`: For fetching fun facts from the Numbers API.

You can install the dependencies using:
```bash
pip install -r requirements.txt
```

## Deployment
The API is deployed on **Vercel** for public access. Follow these steps to deploy your own instance:

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Log in to Vercel:
   ```bash
   vercel login
   ```

3. Deploy the project:
   ```bash
   vercel
   ```

4. Test the deployed API:
   ```
   https://<your-vercel-app>.vercel.app/api/classify-number?number=371
   ```

## Error Handling
The API handles errors gracefully and returns appropriate HTTP status codes:
- **400 Bad Request**: If the input is not a valid number.
  ```json
  {
      "number": "abc",
      "error": true
  }
  ```
- **404 Not Found**: If the requested endpoint does not exist.
- **500 Internal Server Error**: If an unexpected error occurs on the server.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by submitting issues or pull requests on [GitHub](https://github.com/your-username/number-classification-api).
```

---

### **How to Use This README**
1. Replace `<your-vercel-app>` with your actual Vercel app name.
2. Replace `your-username` with your GitHub username in the repository link.
3. Add a `LICENSE` file if you want to include licensing information.

This `README.md` provides a comprehensive overview of your project, making it easy for users and contributors to understand and use your API. Let me know if you need further assistance! 😊
