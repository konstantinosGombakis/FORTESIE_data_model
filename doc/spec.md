<!-- 10-Header -->
  
Entity: fortesie_data_model  
===========================
<!-- /10-Header -->
  
<!-- 15-License -->
  

[Open License](https://github.com/smart-data-models//fortesie_data_model/blob/master/fortesie_data_model/LICENSE.md)  

[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->
  
<!-- 20-Description -->
  

Global description: **Data model for Horizon Europe FORTESIES project**  

version: 2.0.0  
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
- `agreedSavings[number]`: Percentage of savings agreed by the contract. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `alternateName[string]`: An alternative name for this item  
- `apparentPower[object]`: Apparent power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the apparent power    
	- `L2[number]`: Property. Value for phase 2 of the apparent power    
	- `L3[number]`: Property. Value for phase 3 of the apparent power    
- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)
- `challengeRewardValue[number]`: The green euros the user won from the challenge (if applicable).  . Model: [https://schema.org/Number](https://schema.org/Number)
- `co2[number]`: Carbon Dioxide detected  
- `constantTerm[number]`: Real consumption of energy in the period to be evaluated for the calculation of the EPC.   . Model: [https://schema.org/Number](https://schema.org/Number)
- `consumerBonusPercentage[number]`: Percentage of the bonus which is given to the Consumer. This percentage can be for the whole contract or different for each year. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `consumerMalusPercentage[number]`: Percentage of the malus which is given to the Consumer. This percentage can be for the whole contract or different for each year. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `contactStatus[boolean]`: The contact indication, true = broken (open), false = in place (closed)  
- `coolingDegreeDays[number]`: Cooling degree days are calculated based on the number of degrees that the average outdoor temperature rises above a specified baseline temperature over a given period of a day.  . Model: [https://schema.org/Number](https://schema.org/Number)
- `current[object]`: Electrical current. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the current    
	- `L2[number]`: Property. Value for phase 2 of the current    
	- `L3[number]`: Property. Value for phase 3 of the current    
	- `N[number]`: Property. Value for phase neutral of the current    
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  
- `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  
- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  
- `description[string]`: A description of this item  
- `energyPrice[number]`: Energy price for each month, needed for the calculation of the savings and billed price.  . Model: [https://schema.org/Number](https://schema.org/Number)
- `escoBonusPercentage[number]`: Percentage of the bonus which is given to the ESCO. This percentage can be for the whole contract or different for each year. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `escoMalusPercentage[number]`: Percentage of the malus which is given to the ESCO. This percentage can be for the whole contract or different for each year. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `excludedConsumption[number]`: Consumptions that are excluded from the EPC due to various reasons. For example sanitary water consumption is excluded from savings calculations in most EPCs because renovations doesn’t affect them. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `excludedSavings[number]`: Savings that are excluded from the EPC due to various reasons. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `fixedPrice[number]`: Fixed price of the contract charged to the consumer each month.  . Model: [https://schema.org/Number](https://schema.org/Number)
- `frequency[number]`: The frequency of the circuit. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `gasConsumption[number]`: Gas consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20).'  . Model: [https://schema.org/Number](https://schema.org/Number)
- `greenEuroBalance[number]`:   . Model: [https://schema.org/Number.](https://schema.org/Number.)
- `heatingDegreeDays[number]`:   . Model: [https://schema.org/Number.Heating degree days are calculated based on the number of degrees that the average outdoor temperature falls below a specified baseline temperature over a given period of a day](https://schema.org/Number.Heating degree days are calculated based on the number of degrees that the average outdoor temperature falls below a specified baseline temperature over a given period of a day)
- `id[*]`: Unique identifier of the entity  
- `illuminance[number]`:   . Model: [https://schema.org/Number](https://schema.org/Number)
- `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  
- `name[string]`: The name of this item  
- `nominalReturnWaterTemperatureHeating[number]`: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement  
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
- `precipitation[number]`: Amount of water rain registered  . Model: [https://schema.org/Number](https://schema.org/Number)
- `reactivePower[object]`: Fundamental frequency reactive power. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
	- `L1[number]`: Property. Value for phase 1 of the reactive power    
	- `L2[number]`: Property. Value for phase 2 of the reactive power    
	- `L3[number]`: Property. Value for phase 3 of the reactive power    
- `recommendationEngineChallengeStatus[string]`: The status of the challenge WON, FAILED  . Model: [https://schema.org/TEXT](https://schema.org/TEXT)
- `recommendationEngineMessageAppartmentId[string]`: Check Google sheet fortesie-demo-endpoint.  . Model: [https://schema.org/TEXT.Apartment ID for the specific apartment](https://schema.org/TEXT.Apartment ID for the specific apartment)
- `recommendationEngineMessageCorrectResponse[string]`: Correct answer for a recommendationEngineMessageResponse entity.  . Model: [https://schema.org/TEXT](https://schema.org/TEXT)
- `recommendationEngineMessageId[string]`: The unique id of the recommendation for reference.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
- `recommendationEngineMessagePeriod[string]`: Period of time the challenge is covering (note. same challenge cannot be realised twice within the same period).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
- `recommendationEngineMessageResponse[string]`: Question or other response text that require user input.  . Model: [https://schema.org/TEXT](https://schema.org/TEXT)
- `recommendationEngineMessageText[string]`: recommendation_message  . Model: [https://schema.org/TEXT](https://schema.org/TEXT)
- `recommendationEngineMessageTimeToShow[date]`: The time in ISO 8601 UTC mobile app will show the recommendation_engine_message_text entity   . Model: [https://schema.org/Number](https://schema.org/Number)
- `recommendationEngineMessageType[string]`:   . Model: [https://schema.org/StructuredValue.Recommendation type](https://schema.org/StructuredValue.Recommendation type)
- `referenceCoolingDegreeDays[number]`: Reference heating degree days are calculated based on the number of degrees that the average outdoor temperature falls below a specified baseline temperature over a given period of a day used for the definition of the contact ESCO and customer.  . Model: [https://schema.org/Number](https://schema.org/Number)
- `referenceElectricalConsumption[number]`: Reference electrical  energy consumption used for the calculation of the baseline consumption. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `referenceHeatingDegreeDays[number]`:   . Model: [https://schema.org/Number.Reference heating degree days are calculated based on the number of degrees that the average outdoor temperature falls below a specified baseline temperature over a given period of a day used for the definition of the contact ESCO and customer.](https://schema.org/Number.Reference heating degree days are calculated based on the number of degrees that the average outdoor temperature falls below a specified baseline temperature over a given period of a day used for the definition of the contact ESCO and customer.)
- `referenceThermalConsumption[number]`: The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number.Reference thermal energy consumption used for the calculation of the baseline consumption](https://schema.org/Number.Reference thermal energy consumption used for the calculation of the baseline consumption)
- `relativeHumidity[number]`: Relative Humidity of the air (a number between 0 and 1 representing the range of 0% to 100%)  
- `seeAlso[*]`: list of uri pointing to additional resources about the item  
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  
- `temperature[number]`: Temperature of the item  
- `thermalEnergyExport[number]`: Thermal energy exported i.e. generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `thermalEnergyImport[number]`: Thermal energy imported i.e. consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `thresholdSavings[number]`: Percentage of savings that determines the interval in which the EPC bonus or malus is applied. For example a +-5% range, in which neither a bonus or malus is applied. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalActiveEnergyExport[number]`: Total energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalActiveEnergyImport[number]`: Total energy imported i.e. consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalActivePowerExport[number]`: Total Active Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalActivePowerImport[number]`: Total Active Power generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalApparentEnergyExport[number]`: Total energy exported (with regards to apparent power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
- `totalApparentEnergyImport[number]`: Total energy imported i.e. consumed (with regards to apparent power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalApparentPowerExport[number]`: Total Apparent Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalApparentPowerImport[number]`: Total Apparent Power generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalReactiveEnergyExport[number]`: Total fundamental frequency reactive energy exported. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
- `totalReactiveEnergyImport[number]`: Total energy imported i.e. consumed (with regards to fundamental frequency reactive power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalReactivePowerExport[number]`: Total Reactive Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `totalReactivePowerImport[number]`: Total Reactive Power generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)  . Model: [https://schema.org/Number](https://schema.org/Number)
- `type[string]`: NGSI Entity type. It has to be fortesie  
- `userEmail[string]`: The email of the user of the mobile & green euro apps.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)
- `variableTerm[number]`: Variable term of the equation (varaibleTerm*X+constantTerm) for the calculation of the baseline consumption.  . Model: [https://schema.org/Number](https://schema.org/Number)
- `verifiedEnergySavings[number]`: output of the M&V components after the correction with the dependent variables (ie temperature)  . Model: [https://schema.org/Number](https://schema.org/Number)
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
fortesie_data_model:    
  description: Data model for Horizon Europe FORTESIES project    
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
    agreedSavings:    
      description: Percentage of savings agreed by the contract. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: '%'    
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
    challengeRewardValue:    
      description: The green euros the user won from the challenge (if applicable).    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    co2:    
      description: Carbon Dioxide detected    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    constantTerm:    
      description: 'Real consumption of energy in the period to be evaluated for the calculation of the EPC. '    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    consumerBonusPercentage:    
      description: Percentage of the bonus which is given to the Consumer. This percentage can be for the whole contract or different for each year. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: '%'    
    consumerMalusPercentage:    
      description: Percentage of the malus which is given to the Consumer. This percentage can be for the whole contract or different for each year. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: '%'    
    contactStatus:    
      description: The contact indication, true = broken (open), false = in place (closed)    
      readOnly: yes    
      type: boolean    
      x-ngsi:    
        type: Property    
    coolingDegreeDays:    
      description: Cooling degree days are calculated based on the number of degrees that the average outdoor temperature rises above a specified baseline temperature over a given period of a day.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    energyPrice:    
      description: Energy price for each month, needed for the calculation of the savings and billed price.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    escoBonusPercentage:    
      description: Percentage of the bonus which is given to the ESCO. This percentage can be for the whole contract or different for each year. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: '%'    
    escoMalusPercentage:    
      description: Percentage of the malus which is given to the ESCO. This percentage can be for the whole contract or different for each year. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: '%'    
    excludedConsumption:    
      description: Consumptions that are excluded from the EPC due to various reasons. For example sanitary water consumption is excluded from savings calculations in most EPCs because renovations doesn’t affect them. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour    
    excludedSavings:    
      description: Savings that are excluded from the EPC due to various reasons. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour    
    fixedPrice:    
      description: Fixed price of the contract charged to the consumer each month.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    greenEuroBalance:    
      description: ''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    heatingDegreeDays:    
      description: ''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.Heating degree days are calculated based on the number of degrees that the average outdoor temperature falls below a specified baseline temperature over a given period of a day    
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
        type: Relationship    
    illuminance:    
      description: ''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Measured illuminance LUX.    
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
    nominalReturnWaterTemperatureHeating:    
      description: Represents the measured value made over a property. It is also linked to the unit of measure in which the value is expressed and the timestamp of the measurement    
      type: number    
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
        description: Relationship. Unique identifier of the entity    
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
      description: Amount of water rain registered    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Liters per square meter.    
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
    recommendationEngineChallengeStatus:    
      description: The status of the challenge WON, FAILED    
      enum:    
        - WON    
        - FAILED    
      type: string    
      x-ngsi:    
        model: https://schema.org/TEXT    
        type: Property    
    recommendationEngineMessageAppartmentId:    
      description: Check Google sheet fortesie-demo-endpoint.    
      type: string    
      x-ngsi:    
        model: https://schema.org/TEXT.Apartment ID for the specific apartment    
        type: Property    
    recommendationEngineMessageCorrectResponse:    
      description: Correct answer for a recommendationEngineMessageResponse entity.    
      type: string    
      x-ngsi:    
        model: https://schema.org/TEXT    
        type: Property    
    recommendationEngineMessageId:    
      description: The unique id of the recommendation for reference.    
      type: string    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    recommendationEngineMessagePeriod:    
      description: Period of time the challenge is covering (note. same challenge cannot be realised twice within the same period).    
      enum:    
        - DAY    
        - MONTH    
        - WEEK    
        - YEAR    
        - ALL    
      type: string    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    recommendationEngineMessageResponse:    
      description: Question or other response text that require user input.    
      type: string    
      x-ngsi:    
        model: https://schema.org/TEXT    
        type: Property    
    recommendationEngineMessageText:    
      description: recommendation_message    
      type: string    
      x-ngsi:    
        model: https://schema.org/TEXT    
        type: Property    
    recommendationEngineMessageTimeToShow:    
      description: 'The time in ISO 8601 UTC mobile app will show the recommendation_engine_message_text entity '    
      minimum: 0    
      type: date    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    recommendationEngineMessageType:    
      description: ''    
      enum:    
        - MONTHLY_CHALLENGE    
        - QUIZ    
        - ENERGY_SAVING_RECOMMENDATION    
        - RENOVATION_RECOMMENDATION    
        - WARNING    
      type: string    
      x-ngsi:    
        model: https://schema.org/StructuredValue.Recommendation type    
        type: Property    
    referenceCoolingDegreeDays:    
      description: Reference heating degree days are calculated based on the number of degrees that the average outdoor temperature falls below a specified baseline temperature over a given period of a day used for the definition of the contact ESCO and customer.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    referenceElectricalConsumption:    
      description: Reference electrical  energy consumption used for the calculation of the baseline consumption. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour    
    referenceHeatingDegreeDays:    
      description: ''    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.Reference heating degree days are calculated based on the number of degrees that the average outdoor temperature falls below a specified baseline temperature over a given period of a day used for the definition of the contact ESCO and customer.    
        type: Property    
    referenceThermalConsumption:    
      description: The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.Reference thermal energy consumption used for the calculation of the baseline consumption    
        type: Property    
        units: kilovolt-ampere-hour    
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
        units: kilovolt-ampere-hour    
    thermalEnergyImport:    
      description: Thermal energy imported i.e. consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour    
    thresholdSavings:    
      description: Percentage of savings that determines the interval in which the EPC bonus or malus is applied. For example a +-5% range, in which neither a bonus or malus is applied. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: '%'    
    totalActiveEnergyExport:    
      description: Total energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilowatt hour    
    totalActiveEnergyImport:    
      description: Total energy imported i.e. consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilowatt hour    
    totalActivePowerExport:    
      description: Total Active Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt    
    totalActivePowerImport:    
      description: Total Active Power generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt    
    totalApparentEnergyExport:    
      description: Total energy exported (with regards to apparent power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-hour    
    totalApparentEnergyImport:    
      description: Total energy imported i.e. consumed (with regards to apparent power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour.    
    totalApparentPowerExport:    
      description: Total Apparent Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volt-ampere    
    totalApparentPowerImport:    
      description: Total Apparent Power generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volt-ampere    
    totalReactiveEnergyExport:    
      description: Total fundamental frequency reactive energy exported. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-reactive-hour    
    totalReactiveEnergyImport:    
      description: Total energy imported i.e. consumed (with regards to fundamental frequency reactive power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-reactive-hour.    
    totalReactivePowerExport:    
      description: Total Reactive Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: volt-ampere-reactive    
    totalReactivePowerImport:    
      description: Total Reactive Power generated. The unit code (text) is given using the [UN/CEFACT Common Codes](https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20)    
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
    userEmail:    
      description: The email of the user of the mobile & green euro apps.    
      type: string    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    variableTerm:    
      description: Variable term of the equation (varaibleTerm*X+constantTerm) for the calculation of the baseline consumption.    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    verifiedEnergySavings:    
      description: output of the M&V components after the correction with the dependent variables (ie temperature)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    volatileOrganicCompoundsTotal:    
      description: Alkanes <C10, ketones <C6, aldehydes <C10, carboxylic acids <C5, aspirits<C7, Alkenes <C8, Aromatics    
      minimum: 0    
      type: number    
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
  x-license-url: https://github.com/smart-data-models/fortesie_data_model/blob/master/fortesie_data_model/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/konstantinosGombakis/fortesie_data_model/main/FORTESIES_data_model/schema.json    
  x-model-tags: ''    
  x-version: 2.0.0    
```  
</details>    
<!-- /60-ModelYaml -->
  
<!-- 70-MiddleNotes -->
  
<!-- /70-MiddleNotes -->
  
<!-- 80-Examples -->
  

## Example payloads    

Not available the example of a fortesie_data_model in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  

#### fortesie_data_model NGSI-LD normalized Example    

Here is an example of a fortesie_data_model in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
  "frequency": {  
    "type": "Property",  
    "value": 658.2,  
    "unitCode": "HTZ",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "nominalWaterFlowHeating": {  
    "type": "Property",  
    "value": 54.1,  
    "unitCode": "MQS",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "thermalEnergyImport": {  
    "type": "Property",  
    "value": 619.8,  
    "unitCode": "3B",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "thermalEnergyExport": {  
    "type": "Property",  
    "value": 553.8,  
    "unitCode": "3B",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "nominalSupplyWaterTemperatureHeating": {  
    "type": "Property",  
    "value": 23.8,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "nominalWaterFlowCooling": {  
    "type": "Property",  
    "value": 936.1,  
    "unitCode": "MQS",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "nominalReturnWaterTemeratureHeating": {  
    "type": "Propertyp",  
    "value": 10.3,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "gasConsumption": {  
    "type": "Property",  
    "value": 727.0,  
    "unitCode": "3B",  
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
  },  
  "contactStatus": {  
    "type": "Property",  
    "value": true  
  },  
  "illuminance": {  
    "type": "Property",  
    "value": 194.9,  
    "unitCode": "KLX",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "heatingDegreeDays": {  
    "type": "Property",  
    "value": 676.9,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "coolingDegreeDays": {  
    "type": "Property",  
    "value": 904.6,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "referenceHeatingDegreeDays": {  
    "type": "Property",  
    "value": 340.5,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "referenceCoolingDegreeDays": {  
    "type": "Property",  
    "value": 359.5,  
    "unitCode": "CEL",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "referenceElectricalConsumption": {  
    "type": "Property",  
    "value": 282.1,  
    "unitCode": "KWH",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "referenceThermalConsumption": {  
    "type": "Property",  
    "value": 651.4,  
    "unitCode": "3B",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "variableTerm": {  
    "type": "Property",  
    "value": 974.6,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "constantTerm": {  
    "type": "Property",  
    "value": 887.1,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "excludedConsumption": {  
    "type": "Property",  
    "value": 896.8,  
    "unitCode": "KWH",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "excludedSavings": {  
    "type": "Property",  
    "value": 116.6,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "agreedSavings": {  
    "type": "Property",  
    "value": 407.5,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "thresholdSavings": {  
    "type": "Property",  
    "value": 886.6,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "escoBonusPercentage": {  
    "type": "Property",  
    "value": 477.8,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "consumerBonusPercentage": {  
    "type": "Property",  
    "value": 241.0,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "escoMalusPercentage": {  
    "type": "Property",  
    "value": 573.2,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "consumerMalusPercentage": {  
    "type": "Property",  
    "value": 245.9,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "fixedPrice": {  
    "type": "Property",  
    "value": 337.2,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "energyPrice": {  
    "type": "Property",  
    "value": 116.4,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "verifiedEnergySavings": {  
    "type": "Property",  
    "value": 34.6,  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "greenEuroBalance": {  
    "type": "Property",  
    "value": 343.6,  
    "observedAt": "2023-09-15T16:04:49Z",  
    "unitCode": "€G"  
  },  
  "userEmail": {  
    "type": "Property",  
    "value": "fortesie@europeandynamics.eu",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineMessageId": {  
    "type": "Property",  
    "value": "adfd2123123t0",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineMessageType": {  
    "type": "Property",  
    "value": "WARNING",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineMessageText": {  
    "type": "Property",  
    "value": "Writer nor type throughout analysis. Every rest between personal bit.",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineMessageResponse": {  
    "type": "Property",  
    "value": {  
      "1": "To ensure proper functioning of electronic devices",  
      "2": "To prevent discomfort due to extreme temperatures",  
      "3": "To adjust indoor activities accordingly for comfort and health"  
    },  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineMessageCorrectResponse": {  
    "type": "Property",  
    "value": "3",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineMessageTimeToShow": {  
    "type": "Property",  
    "value": "2023-09-15T16:04:49Z",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineChallengeStatus": {  
    "type": "Property",  
    "value": "WON",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineMessagePeriod": {  
    "type": "Property",  
    "value": "MONTH",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "recommendationEngineMessageAppartmentId": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:fortesie:demo-4:building_286:room_bn2",  
    "observedAt": "2023-09-15T16:04:49Z"  
  },  
  "challengeRewardValue": {  
    "type": "Property",  
    "value": 4,  
    "observedAt": "2023-09-15T16:04:49Z",  
    "unitCode": "€G"  
  }  
}  
```  
</details><!-- /80-Examples -->
  
