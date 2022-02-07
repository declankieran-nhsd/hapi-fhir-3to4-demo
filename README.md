# hapi-fhir-3to4-demo

## Overview  

The purpose of this repo is to demo the transform capabilities of the StructureMap transform functionality of the core [HAPI libraries](https://github.com/hapifhir/org.hl7.fhir.core.git)

A [script](./scripts/generate_comparison.py) to check the results of the transform based on the defined elements has been written and the results are available at the root of the input files folder.  A description of the set alegbra used in the script can be found in the [README](./scripts/README.md) in the [scripts](./scripts) folder.

> **NOTE:** Only JSON is currently supported in the script, so the xml examples are not examined.

The latest Cross-Version package [hl7.fhir.xver.r4#1.2.0](http://fhir.org/packages/hl7.fhir.xver.r4/) uses unversioned URL's for the targets in the individual StructureMaps of the resources.  This currently causes the validator_cli to retrieve the wrong StructureDefinition of the resource for the following invocation of the validator_cli 

```shell
java -jar validator_cli.jar ./source.json -version 3.0 -to-version 4.0 -output output.json
```
The core libraries loads the StructureDefinitions included in the STU3 package (hl7.fhir.r3.core#3.0.2) as well as the StructureDeinitions in the xver package (hl7.fhir.xver.r4#1.2.0). The StructureDefinitions in the STU3 package have unversioned URL's

```shell
for f in ~/.fhir/packages/hl7.fhir.r3.core#3.0.2/package/StructureDefinition*; do jq '.url' $f; done
```

In the xver package, they are all versioned

```shell
for f in ~/.fhir/packages/hl7.fhir.xver.r4#1.2.0/package/StructureDefinition*; do jq '.url' $f; done
```
The targets in all StructureMap's in the xver are unversioned

```shell
for f in ~/.fhir/packages/hl7.fhir.xver.r4#1.2.0/package/StructureMap-*3to4*.json; do fhirpath --expression "structure.where(mode='target')" --resourceFile $f; done
```
Therefore if an R4 version of a resource has a new element, and this needs to be handled, then it will fail with an error similar to this

```
 ...Failure: Exception executing transform tgt.encounter = create() as vvv on Rule "context": Attempt to get types for an invalid property 'encounter' on type MedicationRequest
org.hl7.fhir.exceptions.FHIRException: Exception executing transform tgt.encounter = create() as vvv on Rule "context": Attempt to get types for an invalid property 'encounter' on type MedicationRequest
        at org.hl7.fhir.r5.utils.structuremap.StructureMapUtilities.runTransform(StructureMapUtilities.java:1755)
        at org.hl7.fhir.r5.utils.structuremap.StructureMapUtilities.processTarget(StructureMapUtilities.java:1626)
        at org.hl7.fhir.r5.utils.structuremap.StructureMapUtilities.executeRule(StructureMapUtilities.java:1215)
        at org.hl7.fhir.r5.utils.structuremap.StructureMapUtilities.executeGroup(StructureMapUtilities.java:1202)
        at org.hl7.fhir.r5.utils.structuremap.StructureMapUtilities.transform(StructureMapUtilities.java:1164)
        at org.hl7.fhir.validation.ValidationEngine.transformVersion(ValidationEngine.java:667)
        at org.hl7.fhir.validation.cli.services.ValidationService.transformVersion(ValidationService.java:270)
        at org.hl7.fhir.validation.ValidatorCli.doValidation(ValidatorCli.java:260)
        at org.hl7.fhir.validation.ValidatorCli.main(ValidatorCli.java:164)
Caused by: org.hl7.fhir.exceptions.FHIRException: Attempt to get types for an invalid property 'encounter' on type MedicationRequest
        at org.hl7.fhir.r5.model.Base.getTypesForProperty(Base.java:313)
        at org.hl7.fhir.r5.elementmodel.Element.getTypesForProperty(Element.java:750)
        at org.hl7.fhir.r5.utils.structuremap.StructureMapUtilities.runTransform(StructureMapUtilities.java:1651)
        ... 8 more
```

Below is a minimal snippet to repeat

```json
{
  "resourceType": "MedicationRequest",
  "context": {
    "reference": "Encounter/f001",
    "display": "encounter that leads to this prescription"
  }
}
```

Changing the xver StructureMap targets to versioned (4.0) urls, this makes the validator_cli retrieve the corrects version of the StructureDefinitions.

A pytest script has been written to iterate over a set of examples taken from https://github.com/rbren/fhir-swagger/tree/master/schemas/dstu3/examples. There is a pipeline in github actions to run the transforms.  The expected data is currently just the data returned from a successful transform of the data, further analysis would be need to detemine how correct the output is.  Depending on the resource, it varies how much data is successfully transformed over to the version 4.0 resource, but it appears that most data is transferred over with serveral placing data in extensions where there is nowhere to move to in the new version.  

If updates are made to the validator_cli or the StructureDefinitions to improve the maps or functionality, this pipeline should highlight this as a failure.  This is intentional, so that updates are noticed.  This currently means that expected data will then need to be updated.  

## Running and testing locally

The modified package must be loaded into your local package cache for this to work if doing it locally.  See the ./github/workflow yml for an example of how to do it on Linux, or refer to the HL7 guidance on [NPM packaging](https://confluence.hl7.org/display/FHIR/NPM+Package+Specification) for further details on using NPM for FHIR packages.  The modified package is included in the repo ./hl7.fhir.xver.r4#1.2.0-mod

The output of the transforms should match exactly what is in the expected folder.  Therefore to examine the transforms, a comparision of examples/input and examples/expected is possible.  The following can be used to examine the difference in terms of top level keys.

TODO Maybe look at intergrating this into the tests in the pipeline, and examine each object in total.

To get the a diff of the top level keys

```shell
cd examples
mkdir diffs
for f in input/*; do diff <(jq -S 'keys' $f) <(jq -S 'keys' expected/$(basename $f)) > diffs/$(basename $f); done
```
## Test data sets

### JSON

A subset of the STU3 examples available at https://github.com/rbren/fhir-swagger/tree/master/schemas/dstu3/examples were used for these tests.  Only 794 out of 2,496 (as of 14/01/22) are used here, as the validator fails on resources for things like a bundles of resources or resources that have contained resources.  The 794 that did succeed are single resources, comprised of 74 unique types

```shell
jq '.resourceType' input/* | sort -u | wc -l
```

The "id" element has also been removed from all resources as this is not currently handled by the validator_cli.jar.  However, for migration purposes having the "id" transfer over to the new resource is probably not a desirable outcome anyway.

### XML

A set of examples is has also been tested (not validated really yet).  Only 368 succeed without error when running the transform.  There are a total of 914 examples in set.   Again, probably likely to things not yet supported...  TOOD see TODO...

The set of files can be found here in the fhir github https://github.com/HL7/fhir/blob/64bcf4567853b8a6e8a836a173a6fad7ba3dd880/source/release3/examples.zip.  The reason these were chosen, is there were unit tests that were working before for the transforms and this seems to be the set they used.

## HL7 Community Documentation on FML

Additional information can be found at

* [Using the FHIR Mapping Language](https://confluence.hl7.org/display/FHIR/Using+the+FHIR+Mapping+Language)
* [FHIR Mapping Language - Tutorial](https://www.hl7.org/fhir/mapping-tutorial.html)
  * [Tutorial implementation](https://github.com/ahdis/fhir-mapping-tutorial.git)

## Related NHSDigital Work

NHSDigital are in the process of constructing [UK versions of FHIR](https://digital.nhs.uk/services/fhir-apis).  Part of this work is looking at transforming between versions both ins terms of the based resources and the custom extensions that have been designed for the different profiles.

### UK FHIR Profiles

More details on the different API projects NHSDigital have undertaken can be found on [Simplifier](https://simplifier.net/organization/nhsdigital/~projects)

### NHSDigital FHIR Conversion API

https://github.com/NHSDigital/fhir-converter.git

### NHSDIgital FML Maps for FHIR Transforms

https://github.com/NHSDigital/fhir-transforms.git

## TODO

* Extend this to all combinations of version transforms backwards and forwards
* Validate in more detail...  Use a validation service?
* Extend comparison script to XML and TTL
