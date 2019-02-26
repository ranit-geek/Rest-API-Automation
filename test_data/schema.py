my_details_schema = {

  "type": "object",
  "required": [
    "birthdate",
    "country",
    "display_name",
    "email",
    "external_urls",
    "followers",
    "href",
    "id",
    "images",
    "product",
    "type",
    "uri"
  ],
  "properties":
      {
          "birthdate":
              {
                  "type": "string"
              },
          "country":

              {
                  "type": "string"
              },
          "display_name":
              {
                  "type": "string"
              },
          "email":
              {
                  "type": "string"
              },
          "external_urls":
              {
                  "type": "object",
                  "required":
                      [
                          "spotify"
                      ],
                  "properties":
                      {
                          "spotify":
                              {
                                  "type": "string"
                              }
                      }
              },
          "followers":
              {
                  "type": "object",
                  "required":
                      [
                          "href",
                          "total"
                      ],
                  "properties":
                      {
                          "href":
                              {
                                  "type": "null"
                              },
                          "total":
                              {
                                  "type": "integer",
                              }
                      }
              },
          "href":
              {
                  "type": "string"
              },
          "id":
              {
                  "type": "string"
              },
          "images":
              {
                  "type": "array",
              },
          "product":
              {
                  "type": "string"
              },
          "type":
              {
                  "type": "string"
              },
          "uri":
              {
                  "type": "string"
              }
      }
}
