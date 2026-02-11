SCHEMA_USER_CREATE_INPUT = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "password": {
      "type": "string"
    },
    "role": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "email",
    "password",
    "role"
  ]
}

SCHEMA_USER_CREATE_OUTPUT ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "item": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "createdAt": {
          "type": "string"
        },
        "updatedAt": {},
        "email": {
          "type": "string"
        },
        "role": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "username": {},
        "phone": {},
        "organization": {},
        "isSsoUser": {
          "type": "boolean"
        },
        "isDeactivated": {
          "type": "boolean"
        },
        "avatar": {},
        "isDefaultAdmin": {
          "type": "boolean"
        },
        "lockedFieldNames": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "id",
        "createdAt",
        "updatedAt",
        "email",
        "role",
        "name",
        "username",
        "phone",
        "organization",
        "isSsoUser",
        "isDeactivated",
        "avatar",
        "isDefaultAdmin",
        "lockedFieldNames"
      ]
    }
  }
}