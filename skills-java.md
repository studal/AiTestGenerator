# Java Rest Assured API Testing Framework

## Overview

This framework is designed for automated API testing using **Java**, **Rest Assured**, and **TestNG/JUnit**. It helps QA engineers create scalable, maintainable, and reusable API tests.

---

## Tech Stack

* **Java** – Core programming language
* **Rest Assured** – HTTP client for API testing
* **TestNG / JUnit** – Test runner and assertions
* **Maven / Gradle** – Dependency management
* **Jackson / Gson** – JSON parsing
* **Allure / Extent Reports** – Reporting
* **JSON Schema Validator** – Response schema validation
* **Log4j / SLF4J** – Logging

---

## Typical Folder Structure

```text
project/
│
├── src/test/java/
│   ├── tests/
│   │   ├── LoginTest.java
│   │   ├── UserTest.java
│   │
│   ├── endpoints/
│   │   ├── LoginAPI.java
│   │   ├── UserAPI.java
│   │
│   ├── models/
│   │   ├── LoginRequest.java
│   │   ├── UserResponse.java
│   │
│   ├── utils/
│   │   ├── BaseTest.java
│   │   ├── ConfigReader.java
│
├── src/test/resources/
│   ├── config.properties
│   ├── schemas/
│
├── pom.xml
└── testng.xml
```

---

## Core Concepts

### 1. API Object Layer

Encapsulates HTTP methods for reusability.

```java
public Response getUsers(int page) {
    return given()
            .queryParam("page", page)
            .when()
            .get("/api/users");
}
```

---

### 2. Base Test Setup

Used for setup like base URI or auth.

```java
@BeforeClass
public void setup() {
    RestAssured.baseURI = "https://reqres.in";
}
```

---

### 3. Writing Tests

```java
@Test
public void testGetUsers() {
    Response response = userAPI.getUsers(2);
    Assert.assertEquals(response.statusCode(), 200);
}
```

---

### 4. Data Driven Testing

Run same test with multiple inputs.

```java
@DataProvider(name = "loginData")
public Object[][] loginData() {
    return new Object[][]{{"user@test.com", "pass"}};
}
```

---

### 5. Schema Validation

Validate API response structure.

```java
response.then().body(matchesJsonSchemaInClasspath("schemas/user-schema.json"));
```

---

## Best Practices

* Keep test logic separate from request logic.
* Use reusable API object classes.
* Store configs externally.
* Validate status code, body, headers, and schema.
* Use groups like smoke, regression, sanity.
* Generate reports after execution.

---

## Common Commands

```bash
mvn test
mvn clean test
mvn allure:serve
```

---

## Use Cases

* REST API functional testing
* Regression testing
* Smoke/Sanity checks
* Contract/schema validation
* Authentication/authorization testing
* Data-driven API testing
