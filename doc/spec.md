
  

Global description: **Data model for H2020 FORTESIES project**  

version: 0.0.1  
<!-- /20-Description -->
  
<!-- 30-PropertiesList -->
  


## List of properties  


<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `activePower[object]`: Active power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the active power    
	- `L2[number]`: Property. Value for phase 2 of the active power    
	- `L3[number]`: Property. Value for phase 3 of the active power    
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressCountry[string]`: Property. The country. For example, Spain. Model:'https://schema.org/addressCountry'    
	- `addressLocality[string]`: Property. The locality in which the street address is, and which is in the region. Model:'https://schema.org/addressLocality'    
	- `addressRegion[string]`: Property. The region in which the locality is, and which is in the country. Model:'https://schema.org/addressRegion'    
	- `district[string]`: Property. A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: Property. The post office box number for PO box addresses. For example, 03578. Model:'https://schema.org/postOfficeBoxNumber'    
	- `postalCode[string]`: Property. The postal code. For example, 24004. Model:'https://schema.org/https://schema.org/postalCode'    
	- `streetAddress[string]`: Property. The street address. Model:'https://schema.org/streetAddress'    
	- `streetNr[string]`: Property. Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  
- `apparentPower[object]`: Apparent power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the apparent power    
	- `L2[number]`: Property. Value for phase 2 of the apparent power    
	- `L3[number]`: Property. Value for phase 3 of the apparent power    
- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)
- `co2[number]`: Carbon Dioxide detected  
- `contactStatus[boolean]`: The contact indication, true = broken (open), false = in place (closed)  
- `current[object]`: Electrical current. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the current    
	- `L2[number]`: Property. Value for phase 2 of the current    
	- `L3[number]`: Property. Value for phase 3 of the current    
	- `N[number]`: Property. Value for phase neutral of the current    
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  
- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  
- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  
- `description[string]`: A description of this item  
- `frequency[number]`: The frequency of the circuit. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `gasConsumption[number]`: Gas consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20).'  . Model: [https://schema.org/Number](https://schema.org/Number)
- `id[*]`: Unique identifier of the entity  
- `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name[string]`: The name of this item  
- `nominalSupplyWaterTemperatureHeating[number]`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement  
- `nominalWaterFlowCooling[number]`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement  
- `nominalWaterFlowHeating[number]`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement  
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  
- `phaseToPhaseVoltage[object]`: Voltage between phases. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L12[number]`: Property. Value for phase 1 to phase 2 voltage    
	- `L23[number]`: Property. Value for phase 2 to phase 3 voltage    
	- `L31[number]`: Property. Value for phase 3 to phase 1 voltage    
- `phaseVoltage[object]`: The voltage between each phase and neutral conductor. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the voltage    
	- `L2[number]`: Property. Value for phase 2 of the voltage    
	- `L3[number]`: Property. Value for phase 3 of the voltage    
- `pm25[number]`: Particulate matter 2.5 micrometers or less in diameter  
- `volatileOrganicCompoundsTotal[number]`: Alkanes <C10, ketones <C6, aldehydes <C10, carboxylic acids <C5, aspirits<C7, Alkenes <C8, Aromatics  

- `powerFactor[object]`: Power factor for each phase  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the power factor    
	- `L2[number]`: Property. Value for phase 2 of the power factor    
	- `L3[number]`: Property. Value for phase 3 of the power factor    
- `precipitation[number]`: Amount of water rain registered.   . Model: [https://schema.org/Number](https://schema.org/Number)
- `reactivePower[object]`: Fundamental frequency reactive power. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the reactive power    
	- `L2[number]`: Property. Value for phase 2 of the reactive power    
	- `L3[number]`: Property. Value for phase 3 of the reactive power    
- `relativeHumidity[number]`: Relative Humidity of the air (a number between 0 and 1 representing the range of 0% to 100%)  
- `seeAlso[*]`: list of uri pointing to additional resources about the item  
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  
- `temperature[number]`: Temperature of the item  
- `thermalEnergyExport[number]`: Thermal energy exported i.e. generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `thermalEnergyImport[number]`: Thermal energy imported i.e. consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalActivePower[number]`: Total Active Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalActiveEnergyExport[number]`: Total active energy exported . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
- `totalActiveEnergyImport[number]`: Total active energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalReactiveEnergyExport[number]`: Total reactive energy exported . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
- `totalReactiveEnergyImport[number]`: Total reactive energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalApparentEnergyExport[number]`: Total energy exported . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
- `totalApparentEnergyImport[number]`: Total energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalApparentPower[number]`: Total Apparent Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalReactivePower[number]`: Total Reactive Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `type[string]`: NGSI Entity type. It has to be fortesie  
- `windDirection[number]`: Direction of the wind bet  . Model: [http://schema.org/Number](http://schema.org/Number)
- `windSpeed[number]`: Intensity of the wind  . Model: [http//schema.org/Number](http//schema.org/Number)
<!-- /30-PropertiesList -->
  
<!-- 35-RequiredProperties -->
  

Required properties  
- `id`  
- `type`  
<!-- /35-RequiredProperties -->
  
<!-- 40-RequiredProperties -->
  
<!-- /40-RequiredProperties -->
  
<!-- 50-DataModelHeader -->
  

## Data Model description of properties  

Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->
  
<!-- 60-ModelYaml -->
  
<details><summary><strong>full yaml details</strong></summary>    

```yaml  
custom_data_model:    
  description: Data model for H2020 FORTESIES project    
  properties:    
    activePower:    
      description: Active power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      properties:    
        L1:    
          description: Property. Value for phase 1 of the active power    
          minimum: 0    
          type: number    
        L2:    
          description: Property. Value for phase 2 of the active power    
          minimum: 0    
          type: number    
        L3:    
          description: Property. Value for phase 3 of the active power    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: Watt    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: Property. The country. For example, Spain. Model:'https://schema.org/addressCountry'    
          type: string    
        addressLocality:    
          description: Property. The locality in which the street address is, and which is in the region. Model:'https://schema.org/addressLocality'    
          type: string    
        addressRegion:    
          description: Property. The region in which the locality is, and which is in the country. Model:'https://schema.org/addressRegion'    
          type: string    
        district:    
          description: Property. A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
        postOfficeBoxNumber:    
          description: Property. The post office box number for PO box addresses. For example, 03578. Model:'https://schema.org/postOfficeBoxNumber'    
          type: string    
        postalCode:    
          description: Property. The postal code. For example, 24004. Model:'https://schema.org/https://schema.org/postalCode'    
          type: string    
        streetAddress:    
          description: Property. The street address. Model:'https://schema.org/streetAddress'    
          type: string    
        streetNr:    
          description: Property. Number identifying a specific property on a public street    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    apparentPower:    
      description: Apparent power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      properties:    
        L1:    
          description: Property. Value for phase 1 of the apparent power    
          minimum: 0    
          type: number    
        L2:    
          description: Property. Value for phase 2 of the apparent power    
          minimum: 0    
          type: number    
        L3:    
          description: Property. Value for phase 3 of the apparent power    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: Watt    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    co2:    
      description: Carbon Dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    contactStatus:    
      description: The contact indication, true = broken (open), false = in place (closed)    
      readOnly: yes    
      type: boolean    
      x-ngsi:    
        type: Property    
    current:    
      description: Electrical current. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      properties:    
        L1:    
          description: Property. Value for phase 1 of the current    
          type: number    
        L2:    
          description: Property. Value for phase 2 of the current    
          type: number    
        L3:    
          description: Property. Value for phase 3 of the current    
          type: number    
        N:    
          description: Property. Value for phase neutral of the current    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: Ampere    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    frequency:    
      description: The frequency of the circuit. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Hertz    
    gasConsumption:    
      description: Gas consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20).'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nominalSupplyWaterTemperatureHeating:    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement    
      type: number    
      x-ngsi:    
        type: Property    
    nominalWaterFlowCooling:    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement    
      type: number    
      x-ngsi:    
        type: Property    
    nominalWaterFlowHeating:    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement    
      type: number    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Property. Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: Property. Identifier format of any NGSI entity    
            format: uri    
            type: string    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    phaseToPhaseVoltage:    
      description: Voltage between phases. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      properties:    
        L12:    
          description: Property. Value for phase 1 to phase 2 voltage    
          minimum: 0    
          type: number    
        L23:    
          description: Property. Value for phase 2 to phase 3 voltage    
          minimum: 0    
          type: number    
        L31:    
          description: Property. Value for phase 3 to phase 1 voltage    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: Volts    
    phaseVoltage:    
      description: The voltage between each phase and neutral conductor. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      properties:    
        L1:    
          description: Property. Value for phase 1 of the voltage    
          minimum: 0    
          type: number    
        L2:    
          description: Property. Value for phase 2 of the voltage    
          minimum: 0    
          type: number    
        L3:    
          description: Property. Value for phase 3 of the voltage    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: Volts    
    pm25:    
      description: Particulate matter 2.5 micrometers or less in diameter    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    powerFactor:    
      description: Power factor for each phase    
      properties:    
        L1:    
          description: Property. Value for phase 1 of the power factor    
          maximum: 1    
          minimum: -1    
          type: number    
        L2:    
          description: Property. Value for phase 2 of the power factor    
          maximum: 1    
          minimum: -1    
          type: number    
        L3:    
          description: Property. Value for phase 3 of the power factor    
          maximum: 1    
          minimum: -1    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    precipitation:    
      description: 'Amount of water rain registered. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Liters per square meter    
    reactivePower:    
      description: Fundamental frequency reactive power. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      properties:    
        L1:    
          description: Property. Value for phase 1 of the reactive power    
          type: number    
        L2:    
          description: Property. Value for phase 2 of the reactive power    
          type: number    
        L3:    
          description: Property. Value for phase 3 of the reactive power    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: volts-ampere-reactive    
    relativeHumidity:    
      description: Relative Humidity of the air (a number between 0 and 1 representing the range of 0% to 100%)    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    temperature:    
      description: Temperature of the item    
      type: number    
      x-ngsi:    
        type: Property    
    thermalEnergyExport:    
      description: Thermal energy exported i.e. generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour.    
    thermalEnergyImport:    
      description: Thermal energy imported i.e. consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour.    
    totalActivePower:    
      description: Total Active Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt    
    totalActiveEnergyExport:    
      description: Total active energy exported . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-hour    
    totalActiveEnergyImport:    
      description: Total active energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour.    
    totalReactiveEnergyExport:    
      description: Total reactive energy exported . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-hour    
    totalReactiveEnergyImport:    
      description: Total reactive energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour.    
    totalApparentEnergyExport:    
      description: Total energy exported . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-hour    
    totalApparentEnergyImport:    
      description: Total energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour.    
    totalApparentPower:    
      description: Total Apparent Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volt-ampere    
    totalReactivePower:    
      description: Total Reactive Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volt-ampere-reactive    
    type:    
      description: NGSI Entity type. It has to be fortesie    
      enum:    
        - fortesie    
      type: string    
      x-ngsi:    
        type: Property    
    windDirection:    
      description: Direction of the wind bet    
      maximum: 360    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    windSpeed:    
      description: Intensity of the wind    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http//schema.org/Number    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/fortesie_data_model/blob/master/custom_data_model/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/konstantinosGombakis/fortesie_data_model/main/FORTESIES_data_model/schema.json    
  x-model-tags: ''    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Example payloads    

#### custom_data_model NGSI-LD key-values Example    

Here is an example of a custom_data_model in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001",  
  "type": "fortesie",  
  "@context": [  
    "http://forteseie-ld-context/fortesie-context.jsonld"  
  ],  
  "phaseVoltage": 223.6,  
  "phaseToPhaseVoltage": [  
    252.2,  
    223,  
    224.3  
  ],  
  "current": 2.7,  
  "totalActivePower": 344.8,  
  "totalReactivePower": 54.7,  
  "totalApparentPower": 45.7,  
  "powerFactor": 98.2,  
  "activePower": 56.2,  
  "reactivePower": 32.3,  
  "apparentPower": 45.8,  
  "totalApparentEnergyImport": 34.2,  
  "totalApparentEnergyExport": 4.2,  
  "frequency": 49.8,  
  "nominalWaterFlowHeating": 54.1,  
  "nominalSupplyWaterTemperatureHeating": 23.8,  
  "nominalReturnWaterTemperatureHeating": 10.3,  
  "thermalEnergyImport": 12.3,  
  "thermalEnergyExport": 1.3,  
  "gasConsumption ": 1.3,  
  "temperature": 18.4,  
  "relativeHumidity": 39.0,  
  "pm25": 36.0,  
  "co2": 690.5,  
  "windSpeed": 2.5,  
  "windDirection": 231,  
  "precipitation": 34,  
  "contactStatus": 1  
}  
```  
</details>  

#### custom_data_model NGSI-LD normalized Example    

Here is an example of a custom_data_model in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    

```json  

{  
  "id": "urn:ngsi-ld:FORTESIE:DEMO-1:device-id-001",  
  "type": "fortesie",  
  "@context": [  
    "http://forteseie-ld-context/fortesie-context.jsonld"  
  ],  
  "phaseVoltage": {  
    "type": "Property",  
    "value": 223.6,  
    "unitCode": "2G",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "phaseToPhaseVoltage": {  
    "type": "Property",  
    "value": [  
      252.2,  
      223,  
      224.3  
    ],  
    "unitCode": "2G",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "current": {  
    "type": "Property",  
    "value": 2.7,  
    "unitCode": "AMP",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "totalActivePower": {  
    "type": "Property",  
    "value": 344.8,  
    "unitCode": "K1",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "totalReactivePower": {  
    "type": "Property",  
    "value": 54.7,  
    "unitCode": "K2",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "totalApparentPower": {  
    "type": "Property",  
    "value": 45.7,  
    "unitCode": "K1",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "powerFactor": {  
    "type": "Property",  
    "value": 98.2,  
    "unitCode": "P1",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "activePower": {  
    "type": "Property",  
    "value": 56.2,  
    "unitCode": "K1",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "reactivePower": {  
    "type": "Property",  
    "value": 32.3,  
    "unitCode": "K2",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "apparentPower": {  
    "type": "Property",  
    "value": 45.8,  
    "unitCode": "P1",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
    "totalActiveEnergyImport": {
    "type": "Property",
    "value": 32.2,
    "unitCode": "KWH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "totalActiveEnergyExport": {
    "type": "Property",
    "value": 1.2,
    "unitCode": "KWH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
    "totalReactiveEnergyImport": {
    "type": "Property",
    "value": 6.2,
    "unitCode": "KWH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "totalReactiveEnergyExport": {
    "type": "Property",
    "value": 1.2,
    "unitCode": "KWH",
    "observedAt": "2023-09-15T16:04:49.000Z"
  },
  "totalApparentEnergyImport": {  
    "type": "Property",  
    "value": 34.2,  
    "unitCode": "KWH",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "totalApparentEnergyExport": {  
    "type": "Property",  
    "value": 4.2,  
    "unitCode": "KWH",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Property",  
    "value": 54.1,  
    "unitCode": "MQS",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Property",  
    "value": 23.8,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "nominalReturnWaterTemperatureHeating": {  
    "type": "Property",  
    "value": 10.3,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "temperature": {  
    "type": "Property",  
    "value": 18.4,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "relativeHumidity": {  
    "type": "Property",  
    "value": 39.0,  
    "unitCode": "P1",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "pm25": {  
    "type": "Property",  
    "value": 36.0,  
    "unitCode": "GQ",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "co2": {  
    "type": "Property",  
    "value": 690.5,  
    "unitCode": "59",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "windSpeed": {  
    "type": "Property",  
    "value": 2.5,  
    "unitCode": "KMH",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "windDirection": {  
    "type": "Property",  
    "value": 231,  
    "unitCode": "DD",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "precipitation": {  
    "type": "Property",  
    "value": 34,  
    "unitCode": "MMT",  
    "observedAt": "2023-09-15T16:04:49Z"  
  }  
}  
```  
</details><!-- /80-Examples -->
  

