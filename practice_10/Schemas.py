get_full_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "userId": {
        "type": "number"
      },
      "id": {
        "type": "number"
      },
      "title": {
        "type": "string"
      },

      "body": {
        "type": "string"
      }
    },
    "required": [
      "userId",
      "id",
      "title",
      "body"
    ]
  }
}

get_list_item_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "body": {
      "type": "string"
    },
    "userId": {
      "type": "number"
    },
    "id": {
      "type": "number"
    }
  },
  "required": [
    "title",
    "body",
    "userId",
    "id"
  ]
}

empty_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {},
  "required": []
}

create_response_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "body": {
      "type": "string"
    },
    "userId": {
      "type": "number"
    },
    "id": {
      "type": "number"
    }
  },
  "required": [
    "title",
    "body",
    "userId",
    "id"
  ]
}