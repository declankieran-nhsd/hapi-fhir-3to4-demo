# hapi-fhir-3to4-demo

## Oevrview  

The purpose of this repo is to demo the transform capabilities of the StructureMap transform functionality of the core [HAPI libraries](https://github.com/hapifhir/org.hl7.fhir.core.git)

The latest Cross-Version package [hl7.fhir.xver.r4#1.2.0](http://fhir.org/packages/hl7.fhir.xver.r4/) uses unversioned URL's for the targets in the individual StructureMaps of the resources.  This currently causes the validator_cli to retrieve the wrong StructureDefinition of the resource for the following invocation of the validator_cli 

```shell
java -jar validator_cli.jar ./medicationrequest-stu3-apim.json -version 3.0 -to-version 4.0 -output output.json
```

As the -version is 3.0, the StructureDefinitions in the STU3 package are searched, and with the unversioned URL it finds the latest, i.e. the STU3 version of the StructureMap.  The STU3 package that is loaded does have 4.0 versions of the StructureDefinitions, therefore changing the xver StructureMap targets to versioned (4.0) urls, the correct version of the StructureDefinition is retrieve.

A python script is used along with github actions to run the transforms.  The expected data is currently just the data returned from a successful transform of the data.  Depending on the resource, it varies how much data is successfully transformed over to the version 4.0 resource.  If updates are made to the validator_cli or the StructureDefinitions to fix any issues, this pipeline will pick it up.  This currently means that expected data will then need to be updated.  

TODO An indicator of a successful transform would be good, as well as a percentage of how much was successfully transformed.  Need a script to detect lost content in the transformed resource, tricky given the element might have different names..

The modified package must be loaded into your local package cache for this to work if doing it locally.  See the ./github/workflow yml for an example of how to do it on Linux, or refer to the HL7 guidance on [NPM packaging](https://confluence.hl7.org/display/FHIR/NPM+Package+Specification) for further details on using NPM for FHIR packages.    

## Limitations

The StructureMap's in the current xver package currently does not fully transform resources.  This repository will hopefully be useful in keeping up to date with current development on using FML for FHIR transformations

TODO: Extend this to all combinations of version transforms backwards and forwards

A subset of the STU3 examples available at https://github.com/rbren/fhir-swagger/tree/master/schemas/dstu3/examples were used for these tests.  Only 794 out of 2,496 (as of 14/01/22) are used here, as the validator fails on resources for things like a bundles of resources or resources that have contained resources.  The 794 that did succeed are single resources, but this should be a sufficient set to test with. Also, probably very much on the edge of what won't time out in github actions!

The "id" element has also been removed from all resources as this is not currently handled by the validator_cli.jar.  However, for migration purposes having the "id" transfer over to the new resource is probably not a desirable outcome anyway.

A useful command for comparing the results is

diff --color <(jq -S < expected/medicationexample4.json) <(jq -S < input/medicationexample4.json)

to give an indication of what and how much was transformed.

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


