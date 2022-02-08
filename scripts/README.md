# Comparison of JSON transforms
## Overview
This README provides details on how the transform comparison results are generated for the input and expected folders in the [examples](../examples) folder.  See the [README](../examples/README.md) for the result output.

Input and transformed files are in folders named input and expected at the base file path of:
    `../examples`
The StructureDefinitions for the [source](../packages/hl7.fhir.r3.core%233.0.2/package.tar) (input) and [target](../packages/hl7.fhir.r4.core%234.0.1/package.tar) (transformation) are what determines whether data was lost or is invalid and shouldn't be in the input.  

### Use of StructureDefinitions in Comparison

The results are sectioned in terms of the IDs of the elements in the snapshot (FHIRPath snapshot.element.id) in a StructureDefinition (example using Encounter below).  The script creates a dictionary to hold the definition of each resource. Each level within the (JSON) resource structure will be examined in terms of sub elements. 

For example:
```  
    "Encounter"
    "Encounter.id"
    "Encounter.meta"
    "Encounter.language"
    "etc ..."
```  
Will provide an element with the key ('Encounter') with the sub elements, i.e.
```python  
{('Encounter'): ['id', 'meta', 'language', ...]}
```  
For a deeper level, for example:
```
    "Encounter.classHistory"
    "Encounter.classHistory.id"
    "Encounter.classHistory.extension"
    "Encounter.classHistory.modifierExtension"
    "etc ..."
```  
Will provide an element with the key ('Encounter', 'classHistory') with the sub elements, i.e.
```python  
{('Encounter', 'classHistory'): ['id', 'extension', 'modifierExtension', ...]}
```  
The root of the dictionary provides the name of the resource
```python  
{(): ['Encounter'])
```  

### Choice of types

Choice of types (i.e. choice[x]), when defined within a StructureDefintion may contain many valid keys.  These keys are a concatenation of the last part of the snapshot.element.id within the StructureDefinition, and the values within snapshot.element.type.code.  Below is an example within the Communication resource:

```json  
{
  "id": "Communication.payload.content[x]",
  "path": "Communication.payload.content[x]",
  "short": "Message part content",
  "definition": "A communicated content (or for multi-part communications, one portion of the communication).",
  "min": 1,
  "max": "1",
  "type": [
    {
      "code": "string"
    },
    {
      "code": "Attachment"
    },
    {
      "code": "Reference",
      "targetProfile": "http://hl7.org/fhir/StructureDefinition/Resource"
    }
  ]
}
```  

The above element will be considered to have three valid keys based on the entries in the type array, i.e.

```  
Communication.payload.contentString
Communication.payload.contentAttachment
Communication.payload.contentReference
```  

The script would therefore generate the following entry in the dictionary (including the key names of the other elements for Communication.payload)

```python  
  {('Communication', 'payload'): ['id', 
                                  'extension', 
                                  'contentString', 
                                  'contentAttachment', 
                                  'contentReference']}
```

### Example of full StructureDefinition dictionary

Below shows how the STU3 snapshot of patient is packaged in a dictionary
```python  
{(): ['Patient'],
 ('Patient',): ['id',
                'meta',
                'implicitRules',
                'language',
                'text',
                'contained',
                'extension',
                'modifierExtension',
                'identifier',
                'active',
                'name',
                'telecom',
                'gender',
                'birthDate',
                'deceased',
                'address',
                'maritalStatus',
                'multipleBirth',
                'photo',
                'contact',
                'animal',
                'communication',
                'generalPractitioner',
                'managingOrganization',
                'link'],
 ('Patient', 'animal'): ['id',
                         'extension',
                         'modifierExtension',
                         'species',
                         'breed',
                         'genderStatus'],
 ('Patient', 'communication'): ['id',
                                'extension',
                                'modifierExtension',
                                'language',
                                'preferred'],
 ('Patient', 'contact'): ['id',
                          'extension',
                          'modifierExtension',
                          'relationship',
                          'name',
                          'telecom',
                          'address',
                          'gender',
                          'organization',
                          'period'],
 ('Patient', 'link'): ['id', 'extension', 'modifierExtension', 'other', 'type']}
```  

### Format of comparison results

The format of the results are sectioned based on each element definition, i.e

**Filename:** **_[Input file name]_**  

*Encounter:*  
**<sub>[Details]</sub>**  

*Encounter --> classHistory:*  
**<sub>[Details]</sub>**  

etc ...

where the **[Details]** will include the following possible sections  
**<sub>a. Keys lost during transform</sub>**  
**<sub>b. Input keys possibly lost or renamed</sub>**  
**<sub>c. Transform output keys possibly lost or renamed</sub>**  
**<sub>d. Invalid keys in inputs not defined in source definition</sub>**  

Each section may have a list containing the keys that have been flagged, e.g.
```python
{'contentReference', 'contentString'}
```  
The different results sections can be described using set algebra, where  
<sub>**- input** = the input data at a given level, as maps to the superset defined in the StructureDefinition</sub>  
<sub>**- transformed** = the output data of the transform at a given level, as maps to the superset defined in the StructureDefinition</sub>  
<sub>**- source_superset** = The StructureDefinition at a given level (as described above) of the source input</sub>  
<sub>**- target_superset** = The StructureDefinition at a given level (as described above) of the transformed output data</sub>  

### Calculation of results within details sections

#### a. Keys lost during transform
This is defined using the following formula:

<sub>**_( (input ∩ source_superset) ∩ target_superset ) - transformed_**</sub>

> **NOTE:** Only the keys (i.e. the key of the key value pairs of elements) are contained within the following sets.  Also each set relates to single level within the data as defined in the StructureDefinition.  See the dictionary structure in the patient example above.

The following sections will detail, with a worked example, how the set alegbra defined in the formula above provides the lost keys at a given level within the data.

The individual set operations are detailed in terms of the data sets they provide in the next sections.

<ins>**_input ∩ source_superset_**</ins>

Elements (keys) defined in the snapshot of the source StructureDefinition are used to determine if the data in the input is valid.  The data is examined from the top level of the JSON and then down through the levels of each object.  

See the patient StructureDefinition above for how the definition data is structured in a tuple indexed python dictionary.

![Valid keys](./images/valid_keys.svg?raw=true "Data in input considered valid. SET( input ∩ source_superset )")

##### Worked example:
**Input -> SET( input )**
```json  
{
  "NotInSourceDefinition": "data",
  "InSourceDefinition": {},
  "LostData": 123,
  "SuccessfullyTransformed": "data"
}
```  
**Source Superset -> SET( source_superset )**
```python  
{
  {'Resource'): ['LostData',
                 'InSourceDefinition',
                 'SuccessfullyTransformed',
                 'AnotherDef',
                 'NotInTarget']
}
```  
**Valid Keys -> SET( input ∩ source_superset )**
```python  
{
  ['InSourceDefinition', 'LostData', 'SuccessfullyTransformed']
}
```  
<br></br>
<ins>**_(input ∩ source_superset) ∩ target_superset_**</ins>

Elements (keys) defined in the source definition will not necessarily exist in the target definition.  The keys that are defined in both the source definition and the target definition, MUST exist in the transform at the same level.  Therefore as part of the detection of lost keys, the intersection between the set of valid input keys and the target definition for a given level of an object is calculated here.

> **NOTE:** It would be possible for a key of the same name to be mapped to a different part of the resource hierarchy, and for another of the same name to be mapped back to the same level/object examined.  This would be a swap of data with the same name.  This is not considered in this check, and is possibly one of things that could be considered as an extension to this script.  The data (values) are not checked at all in these tests, only the keys for simplicity.

![Must transform](./images/must_transform.svg?raw=true "Data that should be in transformed output. SET( (input ∩ source_superset) ∩ target_superset )")

##### Worked example:
**Valid Keys -> SET( input ∩ source_superset )**
```python  
{
  ['InSourceDefinition', 'LostData', 'SuccessfullyTransformed']
}
```  

**Target Superset -> SET( target_superset )**
```python  
{
  {'Resource'): ['LostData',
                 'AnotherDef',
                 'SuccessfullyTransformed',
                 'NotInSource']
}
```  

**Must Transform -> SET ( ( input ∩ source_superset ) ∩ target_superset )**
```python  
{
  {'Resource'): ['LostData', 'SuccessfullyTransformed']
}
```  
<br></br>
<ins>**_( (input ∩ source_superset) ∩ target_superset ) - transformed_**</ins>

The keys that have been identified in the previous steps as being data that should be in the same level in the transform, now has the transformed data subtracted from it, i.e. asymmetric difference of the sets must_transform and transformed.

![Lost keys](./images/lost_keys.svg?raw=true "Data that has been lost during transform. SET( ((input ∩ source_superset) ∩ target_superset) - transformed")

##### Worked example:
**Must Transform -> SET( (input ∩ source_superset) ∩ target_superset )**
```python  
{
  {'Resource'): ['LostData', 'SuccessfullyTransformed']
}
```  
**Transformed -> SET( transformed )**
```json  
{
  "SuccessfullyTransformed": "data"
}
```  
**Lost Keys ->  SET( ( (input ∩ source_superset) ∩ target_superset ) - transformed )**
```python  
{
  ['LostData']
}
```  

#### b. Input keys possibly lost or renamed
This is defined using the following formula:

<sub>**_( (input ∩ source_superset) - transformed) ∩ (source_superset Δ target_superset)_**</sub>

> **NOTE:** Only the keys (i.e. the key of the key value pairs of elements) are contained within the following sets.  Also each set relates to single level within the data as defined in the StructureDefinition.  See the dictionary structure in the patient example above.

The individual set operations are detailed in terms of the data sets they provide in the next sections.

<ins>**_(input ∩ source_superset) - transformed_**</ins>

The asymmetric difference of the valid keys (input ∩ source_superset, as defined in the previous section **a.**) and the transformed data is taken to get the input keys that are not in the transform.  The valid keys of the input and not just the input keys must be used, as it would be possible an invalid key coule be defined in the target definition but not the source definition, thus something that shouldn't be transformed would be included in possibly lost.  

Subtracting the transformed gives the keys that are defined within a definition but could be lost within the input data.  The next sections uses much the same operations to indicate possibly lost data in the transformed.

![Input keys possibly lost](./images/possibly_lost.svg?raw=true "Valid keys, as per source definition, that are not contained in the transformed data. SET( (input ∩ source_superset) - transformed )")

##### Worked example:
**Input -> SET( input )**
```json  
{
  "PossiblyLostData": 456,
  "SuccessfullyTransformed": "data",
  "InvalidData": 123
}
```  

**Source Superset -> SET( source_superset )**
```python  
{
  {'Resource'): ['PossiblyLostData',
                 'SuccessfullyTransformed',
                 'AnotherDef']
}
```  

**Transformed -> SET( transformed )**
```json  
{
  "SuccessfullyTransformed": "data"
}
```  

**Possibly lost -> SET( (input ∩ source_superset) - transformed )**
```python  
{
  ['PossiblyLostData']
}
```  
<br></br>
<ins>**_source_superset Δ target_superset_**</ins>

The symmetric difference of the source and the target definition is taken to get the set of keys that have either been renamed or deprecated.

![Symmetric difference of the source and the target definition](./images/symmetric_diff_def.svg?raw=true "Keys that have either been renamed or deprecated. SET( source_superset Δ target_superset )")

##### Worked example:
**Source Superset -> SET( source_superset )**
```python  
{
  {'Resource'): ['PossiblyLostData',
                 'SuccessfullyTransformed',
                 'AnotherDef']
}
```  

**Target Superset -> SET( target_superset )**
```python  
{
  {'Resource'): ['AnotherDef',
                 'SuccessfullyTransformed',
                 'NotInSource']
}
```  

**Symmetric Definition Diff -> SET( source_superset Δ target_superset )**
```python  
{
  ['PossiblyLostData', 'NotInSource']
}
```  
<br></br>
<ins>**_( (input ∩ source_superset) - transformed) ∩ (source_superset Δ target_superset)_**</ins>

The intersection of the possibly lost keys in the input and those that are either deprecated or renamed, provides the keys that are possibly lost in the input and are worth a more detailed look at.  

> **NOTE:** This is a limitation of the scripts that checks for differences and is noted in the limitations section below.  For a fully accurate report, a mapping would need to be referenced, such as one of the defined StructureMaps, however this strategy should be useful as a test bed for fully completing the StructureMaps.

![Possibly lost keys in input](./images/possibly_lost_input.svg?raw=true "Keys in the input data that have either been renamed or deprecated. SET( (input ∩ source_superset) - transformed) ∩ (source_superset Δ target_superset) )")

##### Worked example:

**Possibly lost -> SET( (input ∩ source_superset) - transformed )**
```python  
{
  ['PossiblyLostData']
}
```  

**Symmetric Definition Diff -> SET( source_superset Δ target_superset )**
```python  
{
  ['PossiblyLostData', 'NotInSource']
}
```  

**Possibly lost in input -> SET( (input ∩ source_superset) - transformed) ∩ (source_superset Δ target_superset) )**
```python  
{
  ['PossiblyLostData']
}
```  

#### c. Transform output keys possibly lost or renamed
This is defined using the following formula:

<sub>**_(transformed - input) ∩ (source_superset Δ target_superset)_**</sub>

See section **b.** above.  This is the same as the possibly lost keys for the input, except the asymmetric difference of the input and transformed is reversed.  The indicates keys that are possibly deprecated or renamed in transformed data, as opposed to the input data.

#### d. Invalid keys in inputs not defined in source definition
This is defined using the following formula:

<sub>**_input - source_superset_**</sub>

Anything that is not defined in the source definition is considered to be invalid input, which may include misspelled element keys as well as other unexpected data.

![Invalid keys in input](./images/invalid_keys.svg?raw=true "Keys in the input data that are undefined. SET( input - source_superset )")

##### Worked example:
**Input -> SET( input )**
```json  
{
  "NotInSourceDefinition": "data",
  "InSourceDefinition": {},
  "LostData": 123,
  "SuccessfullyTransformed": "data"
}
```  
**Source Superset -> SET( source_superset )**
```python  
{
  {'Resource'): ['LostData',
                 'InSourceDefinition',
                 'SuccessfullyTransformed',
                 'AnotherDef',
                 'NotInTarget']
}
```  
**Invalid Keys -> SET( input ∩ source_superset )**
```python  
{
  ['NotInSourceDefinition']
}
```  

## Limitations / Scope for extension

* This only supports JSON, but the comparison code has been structured using a strategy pattern, so if following the same dictionary output for an XML or turtle comparator, it should be possible to use the same logic to generate the results template by just extending the documentcompare library.

* It would clearly be preferable to just indicate lost or invalid data, as opposed to possible lost in the input and transformed.  The current mappings defined in the StructureMaps or the FML could be used for this.  The script and set logic could be extended to facilitate this.  However, the mappings seem to possibly be missing a few edge cases and this script could be used as a test harness for updating the StructureMaps/FML.

* If the key is a valid key and appears to be lost in the transform, it might be that the data in the object was actually invalid.  The comparison code does not currently look at the data, so won't detect whether the data in that element is valid or not.  An element with invalid data will be shown as lost, whereas it should be included in the invalid list.  Probably not too difficult to extend the code to do this...

* There is no support for testing transforms where the resource name has changed.

* No doubt many others :-/