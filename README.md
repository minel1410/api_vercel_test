# [Car Price Predictor API](https://price-predictor-model-api.onrender.com/)

## Overview

The Car Price Predictor API is a backend service developed using FastAPI. It serves as the backend for the Car Price Predictor application, allowing users to submit data about their vehicles and receive price predictions. The API is hosted on Render, which may cause responses to be delayed by a few minutes if the server is in sleep mode due to inactivity.

## Endpoints

### `/models`

- **Method**: `GET`
- **Description**: Retrieves a list of car brands and their associated models.
- **Response Model**: `List[BrandModel]`
- **Response Example**:
  ```json
  [
    {
      "brand_id": 1,
      "models": [
        {
          "model_id": 101,
          "model_name": "Model A",
          "brand_name": "Brand X"
        },
        ...
      ]
    },
    ...
  ]

## Endpoints

### `/fuel_types`

- **Method**: `GET`
- **Description**: Returns a dictionary of fuel types with their corresponding encoding values.
- **Response Example**:
  ```json
  {
    "Benzin": 0,
    "Dizel": 1,
    "Elektro": 2,
    "Hibrid": 3,
    "Plin": 4
  }

  ### `/body_types`

- **Method**: `GET`
- **Description**: Provides a dictionary of body types with their corresponding encoding values.
- **Response Example**:
  ```json
  {
    "Caddy": 0,
    "Kabriolet": 1,
    "Karavan": 2,
    "Kombi": 3,
    "Limuzina": 4,
    "Malo auto": 5,
    "Monovolumen": 6,
    "Off Road": 7,
    "Ostalo": 8,
    "Pick up": 9,
    "SUV": 10,
    "Sportski/kupe": 11,
    "Terenac": 12
  }
  ### `/post_car`

- **Method**: `POST`
- **Description**: Submits car data to receive a price prediction.
- **Request Model**: `ModelRequest`
- **Request Example**:
  ```json
  {
    "Mileage": 120000,
    "Engine_volume": 2.0,
    "Engine_power": 150,
    "Registered": true,
    "Year": 2018,
    "brand_enc": 1,
    "body_enc": 3,
    "fuel_type_enc": 1,
    "model_enc": 101
  }
 
