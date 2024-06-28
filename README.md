---
title: FastAPI
description: A FastAPI server
tags:
  - fastapi
  - uvicorn
  - python
  - postgresql
---

# FastAPI FullStack Example

This example starts up a [FastAPI](https://fastapi.tiangolo.com/) server with [PostgreSQL](https://www.postgresql.org/) as backend.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/IhHgYS?referralCode=jk_FgY)

## ✨ Features

- FastAPI
- [uvicorn](https://www.uvicorn.org/)
- Python 3

## 💁‍♀️ How to use

- Clone locally and install packages with pip using `pip install -r requirements.txt`
- Run locally using `python -m backend.app.main`

## 📝 Notes

- To learn about how to use FastAPI with most of its features, you can visit the [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/)
- To learn about Uvicorn and how to configure it, read their [Documentation](https://www.uvicorn.org/)

## 📋 API Endpoints

### Create Item
```sh
curl -X POST "https://fullstack-fastapi-production.up.railway.app/api/v1/items/" -H "Content-Type: application/json" -d '{"name": "Test Item", "description": "A test item", "price": 100, "quantity_in_stock": 10}'
```

### Get Item
```sh
curl -X GET "https://fullstack-fastapi-production.up.railway.app/api/v1/items/{item_id}"
```

### Update Item
```sh
curl -X PUT "https://fullstack-fastapi-production.up.railway.app/api/v1/items/{item_id}" -H "Content-Type: application/json" -d '{"name": "Updated Test Item", "description": "An updated test item", "price": 150, "quantity_in_stock": 5}'
```

### Delete Item
```sh
curl -X DELETE "https://fullstack-fastapi-production.up.railway.app/api/v1/items/{item_id}"
```
