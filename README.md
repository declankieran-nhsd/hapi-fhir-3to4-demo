# hapi-fhir-3to4-demo

## Oevrview  

Using a modified version of the package [hl7.fhir.xver.r4#1.2.0](http://fhir.org/packages/hl7.fhir.xver.r4/), where the target URL's are versioned to 4.0, this repo contains a set of STU3 FHIR resource examples that are transformed using the HAPI validator_cli.  

A python script is used along with github actions to run the transforms.  The modified package must be loaded into your local package cache for this to work if doing it locally.  See the ./github/workflow yml for an example of how to do it on Linux, or refer to the HL7 guidance on [NPM packaging](https://confluence.hl7.org/display/FHIR/NPM+Package+Specification) for further details on FHIR packages.    

The set of STU3 examples used are copied from https://github.com/rbren/fhir-swagger/tree/master/schemas/dstu3/examples.  Only 794 out of 2,496 (as of 14/01/22) are being used here as the validator_cli does not currently appear to support more complex resources like bundles and resources with contained resources.  The "id" element has also been removed from all resources as this is not currently handled by the validator_cli.jar.  However, for migration purposes having the "id" transfer over to the new resource is probably not a desirable outcome anyway.

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


