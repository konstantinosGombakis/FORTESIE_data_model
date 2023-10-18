
# Fortesie Data model demo


The tutorial uses [cUrl](https://ec.haxx.se/) commands throughout, but is also available as
[Postman documentation](https://www.postman.com/konstantinosgombakis/workspace/fortesie-data-model/collection/9192452-51008a35-c2e2-4a3f-b72a-175e210e24b6?action=share&creator=9192452)

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.postman.com/konstantinosgombakis/workspace/fortesie-data-model/collection/9192452-51008a35-c2e2-4a3f-b72a-175e210e24b6?action=share&creator=9192452)

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

<details><summary><strong>show/hide output</strong></summary>    

```json  
{
  "id": "urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001",
  "type": "fortesie",
  "https://smartdatamodels.org/dataModel.Energy/phaseVoltage": {
    "type": "Property",
    "value": 223.6,
    "unitCode": "2G",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/phaseToPhaseVoltage": {
    "type": "Property",
    "value": [
      252.2,
      223,
      224.3
    ],
    "unitCode": "2G",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/current": {
    "type": "Property",
    "value": 2.7,
    "unitCode": "AMP",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/totalActivePower": {
    "type": "Property",
    "value": 344.8,
    "unitCode": "K1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/totalReactivePower": {
    "type": "Property",
    "value": 54.7,
    "unitCode": "K2",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/totalApparentPower": {
    "type": "Property",
    "value": 45.7,
    "unitCode": "K1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/powerFactor": {
    "type": "Property",
    "value": 98.2,
    "unitCode": "P1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/activePower": {
    "type": "Property",
    "value": 56.2,
    "unitCode": "K1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/reactivePower": {
    "type": "Property",
    "value": 32.3,
    "unitCode": "K2",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/apparentPower": {
    "type": "Property",
    "value": 45.8,
    "unitCode": "P1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/totalApparentEnergyImport": {
    "type": "Property",
    "value": 34.2,
    "unitCode": "KWH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Energy/totalApparentEnergyExport": {
    "type": "Property",
    "value": 4.2,
    "unitCode": "KWH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.S4BLDG/nominalWaterFlowHeating": {
    "type": "Property",
    "value": 54.1,
    "unitCode": "MQS",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.S4BLDG/nominalSupplyWaterTemperatureHeating": {
    "type": "Property",
    "value": 23.8,
    "unitCode": "CEL",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "nominalReturnWaterTemperatureHeating": {
    "type": "Property",
    "value": 10.3,
    "unitCode": "CEL",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Environment/temperature": {
    "type": "Property",
    "value": 18.4,
    "unitCode": "CEL",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Environment/relativeHumidity": {
    "type": "Property",
    "value": 39,
    "unitCode": "P1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Environment/pm25": {
    "type": "Property",
    "value": 36,
    "unitCode": "GQ",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Environment/co2": {
    "type": "Property",
    "value": 690.5,
    "unitCode": "59",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Weather/windSpeed": {
    "type": "Property",
    "value": 2.5,
    "unitCode": "KMH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Weather/windDirection": {
    "type": "Property",
    "value": 231,
    "unitCode": "DD",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "https://smartdatamodels.org/dataModel.Weather/precipitation": {
    "type": "Property",
    "value": 34,
    "unitCode": "MMT",
    "observedAt": "2023-09-15T16:04:49.000Z"
  }
}  
```  
</details>  

### Request data for device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001 providing @context
#### Request:
```console
curl -X GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001' \
 -H 'Link: <http://forteseie-ld-context/fortesie-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
 -H 'Accept: application/ld+json' |jq
```

<details><summary><strong>show/hide output</strong></summary>    

```json 
{
  "@context": "http://forteseie-ld-context/fortesie-context.jsonld",
  "id": "urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001",
  "type": "fortesie",
  "phaseVoltage": {
    "type": "Property",
    "value": 223.6,
    "unitCode": "2G",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "phaseToPhaseVoltage": {
    "type": "Property",
    "value": [
      252.2,
      223,
      224.3
    ],
    "unitCode": "2G",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "current": {
    "type": "Property",
    "value": 2.7,
    "unitCode": "AMP",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "totalActivePower": {
    "type": "Property",
    "value": 344.8,
    "unitCode": "K1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "totalReactivePower": {
    "type": "Property",
    "value": 54.7,
    "unitCode": "K2",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "totalApparentPower": {
    "type": "Property",
    "value": 45.7,
    "unitCode": "K1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "powerFactor": {
    "type": "Property",
    "value": 98.2,
    "unitCode": "P1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "activePower": {
    "type": "Property",
    "value": 56.2,
    "unitCode": "K1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "reactivePower": {
    "type": "Property",
    "value": 32.3,
    "unitCode": "K2",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "apparentPower": {
    "type": "Property",
    "value": 45.8,
    "unitCode": "P1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "totalApparentEnergyImport": {
    "type": "Property",
    "value": 34.2,
    "unitCode": "KWH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "totalApparentEnergyExport": {
    "type": "Property",
    "value": 4.2,
    "unitCode": "KWH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "nominalWaterFlowHeating": {
    "type": "Property",
    "value": 54.1,
    "unitCode": "MQS",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "nominalSupplyWaterTemperatureHeating": {
    "type": "Property",
    "value": 23.8,
    "unitCode": "CEL",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "nominalReturnWaterTemperatureHeating": {
    "type": "Property",
    "value": 10.3,
    "unitCode": "CEL",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "temperature": {
    "type": "Property",
    "value": 18.4,
    "unitCode": "CEL",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "relativeHumidity": {
    "type": "Property",
    "value": 39,
    "unitCode": "P1",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "pm25": {
    "type": "Property",
    "value": 36,
    "unitCode": "GQ",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "co2": {
    "type": "Property",
    "value": 690.5,
    "unitCode": "59",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "windSpeed": {
    "type": "Property",
    "value": 2.5,
    "unitCode": "KMH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "windDirection": {
    "type": "Property",
    "value": 231,
    "unitCode": "DD",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "precipitation": {
    "type": "Property",
    "value": 34,
    "unitCode": "MMT",
    "observedAt": "2023-09-15T16:04:49.000Z"
  }
}
```
</details>    

### Provition device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002
```console
./importJSON.sh sample-data_model_for_partners_2.json 
```

### Request data for device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002  without providing @context

#### Request:
```console
curl -X GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002'  | jq
```

<details><summary><strong>show/hide output</strong></summary>    

```json 
{
  "id": "urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002",
  "type": "fortesie",
  "https://smartdatamodels.org/dataModel.Energy/phaseVoltage": {
    "type": "Property",
    "value": 223.6,
    "unitCode": "2G",
    "observedAt": "2023-09-15T16:04:49.000Z"
  }
}
```
</details> 

### Request data for device urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002 providing @context
#### Request:
```console
curl -X GET 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002' \
 -H 'Link: <http://forteseie-ld-context/fortesie-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
 -H 'Accept: application/ld+json' |jq
```

<details><summary><strong>show/hide output</strong></summary>  
  
```json 
{
  "@context": "http://forteseie-ld-context/fortesie-context.jsonld",
  "id": "urn:ngsi-ld:FORTESIE:DEMO-1:device-id-002",
  "type": "fortesie",
  "phaseVoltage": {
    "type": "Property",
    "value": 223.6,
    "unitCode": "2G",
    "observedAt": "2023-09-15T16:04:49.000Z"
  }
```  
</details> 