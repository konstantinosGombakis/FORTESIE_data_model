
# Fortesie Data model demo


The tutorial uses [cUrl](https://ec.haxx.se/) commands throughout, but is also available as
[Postman documentation](https://www.postman.com/glompos21/workspace/fortesie-data-model/collection/9192452-51008a35-c2e2-4a3f-b72a-175e210e24b6?action=share&creator=9192452)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/glompos21/workspace/fortesie-data-model/collection/9192452-51008a35-c2e2-4a3f-b72a-175e210e24b6?action=share&creator=9192452)

Additional several docker images are needed.

**Start needed docker components**
```console
docker-compose up -d 
```


## Tutorial with cURL

Please install from your package manager the utility **jq**

### Checking the service health

You can check if the Orion Context Broker is running by making an HTTP request to the exposed port:

#### Request:

```console
curl -X GET 'http://localhost:1026/version'
```
#### Response:

The response will look similar to the following:

```json
{
  "orionld version": "1.4.0",
  "orion version":   "1.15.0-next",
  "uptime":          "0 d, 0 h, 35 m, 56 s",
  "git_hash":        "746e13b343987d846b3451fe1f943600c4b2abe9",
  "compile_time":    "Sat Aug 26 06:19:10 UTC 2023",
  "compiled_by":     "root",
  "compiled_in":     "",
  "release_date":    "Sat Aug 26 06:19:10 UTC 2023",
  "doc":             "https://fiware-orion.readthedocs.org/en/master/"
}
```
### Provition device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001 
```console
./importJSON.sh sample-data_model_for_partners.json
```

### Request data for device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001  without providing @context

#### Request:
```console
curl -X GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001' | jq
```

### Request data for device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001 providing @context
#### Request:
```console
curl -X GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001' \
 -H 'Link: <http://forteseie-ld-context/fortesie-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
 -H 'Accept: application/ld+json' |jq
```


### Provition device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002
```console
./importJSON.sh sample-data_model_for_partners_2.json 
```

### Request data for device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001  without providing @context

#### Request:
```console
curl -X GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002'  | jq
```

### Request data for device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001 providing @context
#### Request:
```console
curl -X GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002' \
 -H 'Link: <http://forteseie-ld-context/fortesie-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
 -H 'Accept: application/ld+json' |jq
```