# Comparison of JSON transforms
## Overview
A walk-through of how these results are generated is given in the [directory](../scripts) of the [script](../scripts/generate_comparison.py) that generates these results.  The [input folder](./input) contains the data to be transformed, and the [expected folder](./expected) contains the transformed data.

Examples that are not fully transformed are included in the expected folder to provide expected output in the validate transforms tests that run as part a [CI pipeline](../.github/workflows/validate-transforms.yml) testing the latest version of the validator_cli.

Most issues are from either invalid data or renamed data not being handled.

## Results
### Summary
|<sub>Total transforms examined:</sub>                 |<sub>788</sub>|
|----------------------------------------|---------------|
|<sub>Number of transforms with issues to review:</sub> |<sub>215</sub>    |
|<sub>Transforms with no issue detected:</sub>|<sub>573</sub>  |
---
### [composition-example.json](./input/composition-example.json)
*Composition:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'class'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'category'}
```

---
### [patient-example-xds.json](./input/patient-example-xds.json) ✔
---
### [valueset-vision-eye-codes.json](./input/valueset-vision-eye-codes.json) ✔
---
### [slot-example.json](./input/slot-example.json) ✔
---
### [valueset-care-plan-activity-status.json](./input/valueset-care-plan-activity-status.json) ✔
---
### [communication-example.json](./input/communication-example.json)
*Communication:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

---
### [binary-f006.json](./input/binary-f006.json)
*Binary:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'content'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'data'}
```

---
### [expansionprofile-questionnaire.json](./input/expansionprofile-questionnaire.json) ✔
---
### [operation-conceptmap-closure.json](./input/operation-conceptmap-closure.json) ✔
---
### [questionnaire-extensions-Questionnaire-deReference.json](./input/questionnaire-extensions-Questionnaire-deReference.json) ✔
---
### [observation-genetics-Observation-amino-acid-change.json](./input/observation-genetics-Observation-amino-acid-change.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [valueset-task-performer-type.json](./input/valueset-task-performer-type.json) ✔
---
### [valueset-data-types.json](./input/valueset-data-types.json) ✔
---
### [valueset-c80-doc-classcodes.json](./input/valueset-c80-doc-classcodes.json) ✔
---
### [valueset-message-conformance-event-mode.json](./input/valueset-message-conformance-event-mode.json) ✔
---
### [valueset-flag-category.json](./input/valueset-flag-category.json) ✔
---
### [valueset-appointmentstatus.json](./input/valueset-appointmentstatus.json) ✔
---
### [valueset-map-context-type.json](./input/valueset-map-context-type.json) ✔
---
### [valueset-name-use.json](./input/valueset-name-use.json) ✔
---
### [valueset-actionlist.json](./input/valueset-actionlist.json) ✔
---
### [valueset-module-metadata-type.json](./input/valueset-module-metadata-type.json) ✔
---
### [valueset-measure-type.json](./input/valueset-measure-type.json) ✔
---
### [valueset-process-priority.json](./input/valueset-process-priority.json) ✔
---
### [valueset-template-status-code.json](./input/valueset-template-status-code.json) ✔
---
### [medicationexample13.json](./input/medicationexample13.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [valueset-LOINC-48019-4-answerlist.json](./input/valueset-LOINC-48019-4-answerlist.json) ✔
---
### [medicationstatementexample1.json](./input/medicationstatementexample1.json)
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime', 'patient', 'reasonForUseCodeableConcept', 'wasNotTaken'}
```

---
### [valueset-module-metadata-focus-type.json](./input/valueset-module-metadata-focus-type.json) ✔
---
### [valueset-immunization-route.json](./input/valueset-immunization-route.json) ✔
---
### [valueset-claim-modifiers.json](./input/valueset-claim-modifiers.json) ✔
---
### [organization-example-insurer.json](./input/organization-example-insurer.json) ✔
---
### [medicationexample1.json](./input/medicationexample1.json) ✔
---
### [linkage-example.json](./input/linkage-example.json) ✔
---
### [condition-example-f205-infection.json](./input/condition-example-f205-infection.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'dateRecorded', 'patient'}
```

---
### [valueset-participantrequired.json](./input/valueset-participantrequired.json) ✔
---
### [valueset-manifestation-codes.json](./input/valueset-manifestation-codes.json) ✔
---
### [valueset-map-transform.json](./input/valueset-map-transform.json) ✔
---
### [condition-example-f204-renal.json](./input/condition-example-f204-renal.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'encounter', 'dateRecorded', 'patient', 'abatementDateTime'}
```

*Condition --> stage:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-search-modifier-code.json](./input/valueset-search-modifier-code.json) ✔
---
### [relatedperson-example-f002-ariadne.json](./input/relatedperson-example-f002-ariadne.json) ✔
---
### [valueset-allergy-intolerance-status.json](./input/valueset-allergy-intolerance-status.json) ✔
---
### [valueset-order-set-item-type.json](./input/valueset-order-set-item-type.json) ✔
---
### [observation-example-sample-data.json](./input/observation-example-sample-data.json)
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

*Observation --> component:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueSampledData', 'fhir_comments'}
```

---
### [valueset-organization-type.json](./input/valueset-organization-type.json) ✔
---
### [operation-task-release.json](./input/operation-task-release.json) ✔
---
### [valueset-condition-ver-status.json](./input/valueset-condition-ver-status.json) ✔
---
### [valueset-units-of-time.json](./input/valueset-units-of-time.json) ✔
---
### [valueset-testscript-operation-codes.json](./input/valueset-testscript-operation-codes.json) ✔
---
### [valueset-goal-category.json](./input/valueset-goal-category.json) ✔
---
### [practitioner-example-f204-ce.json](./input/practitioner-example-f204-ce.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [condition-example.json](./input/condition-example.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'patient'}
```

---
### [valueset-subscription-channel-type.json](./input/valueset-subscription-channel-type.json) ✔
---
### [valueset-binding-strength.json](./input/valueset-binding-strength.json) ✔
---
### [valueset-basic-resource-type.json](./input/valueset-basic-resource-type.json) ✔
---
### [valueset-care-plan-activity-category.json](./input/valueset-care-plan-activity-category.json) ✔
---
### [valueset-specimen-collection-method.json](./input/valueset-specimen-collection-method.json) ✔
---
### [organization-example-f203-bumc.json](./input/organization-example-f203-bumc.json)
*Organization:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_active'}
```

---
### [visionprescription-example-1.json](./input/visionprescription-example-1.json)
*VisionPrescription:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'dispense'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'lensSpecification'}
```

---
### [device-extensions-Device-din.json](./input/device-extensions-Device-din.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [valueset-LOINC-53037-8-answerlist.json](./input/valueset-LOINC-53037-8-answerlist.json) ✔
---
### [medicationexample4.json](./input/medicationexample4.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [valueset-procedure-request-priority.json](./input/valueset-procedure-request-priority.json) ✔
---
### [valueset-specimen-container-type.json](./input/valueset-specimen-container-type.json) ✔
---
### [familymemberhistory-example-mother.json](./input/familymemberhistory-example-mother.json)
*FamilyMemberHistory --> condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetQuantity'}
```

---
### [valueset-device-kind.json](./input/valueset-device-kind.json) ✔
---
### [valueset-provenance-agent-role.json](./input/valueset-provenance-agent-role.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### [us-core-Patient-ethnicity.json](./input/us-core-Patient-ethnicity.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [valueset-payment-type.json](./input/valueset-payment-type.json) ✔
---
### [practitioner-example-xcda-author.json](./input/practitioner-example-xcda-author.json) ✔
---
### [valueset-condition-code.json](./input/valueset-condition-code.json) ✔
---
### [valueset-device-action.json](./input/valueset-device-action.json) ✔
---
### [operation-task-resume.json](./input/operation-task-resume.json) ✔
---
### [valueset-condition-state.json](./input/valueset-condition-state.json) ✔
---
### [valueset-security-labels.json](./input/valueset-security-labels.json)
*ValueSet:*

**<sub>Keys lost during transform:</sub>**
```python
{'compose'}
```

*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### [valueset-extensions-ValueSet-effective.json](./input/valueset-extensions-ValueSet-effective.json) ✔
---
### [valueset-list-order.json](./input/valueset-list-order.json) ✔
---
### [valueset-procedure-not-performed-reason.json](./input/valueset-procedure-not-performed-reason.json) ✔
---
### [operation-patient-everything.json](./input/operation-patient-everything.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [organization-example-f003-burgers-ENT.json](./input/organization-example-f003-burgers-ENT.json) ✔
---
### [detectedissue-example-dup.json](./input/detectedissue-example-dup.json)
*DetectedIssue:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'date', 'category'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'code'}
```

---
### [valueset-bundle-type.json](./input/valueset-bundle-type.json) ✔
---
### [group-example-member.json](./input/group-example-member.json) ✔
---
### [episodeofcare-questionnaire.json](./input/episodeofcare-questionnaire.json) ✔
---
### [valueset-encounter-special-courtesy.json](./input/valueset-encounter-special-courtesy.json) ✔
---
### [valueset-cds-rule-action-type.json](./input/valueset-cds-rule-action-type.json) ✔
---
### [namingsystem-example-replaced.json](./input/namingsystem-example-replaced.json)
*NamingSystem:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'replacedBy'}
```

---
### [valueset-investigation-sets.json](./input/valueset-investigation-sets.json) ✔
---
### [valueset-observation-methods.json](./input/valueset-observation-methods.json) ✔
---
### [audit-event-example-media.json](./input/audit-event-example-media.json)
*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_name'}
```

*AuditEvent --> entity:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier', 'reference'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'what'}
```

*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

---
### [valueset-parent-relationship-codes.json](./input/valueset-parent-relationship-codes.json) ✔
---
### [valueset-map-input-mode.json](./input/valueset-map-input-mode.json) ✔
---
### [element.profile.json](./input/element.profile.json) ✔
---
### [condition-example2.json](./input/condition-example2.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'patient'}
```

---
### [operation-task-reserve.json](./input/operation-task-reserve.json) ✔
---
### [valueset-message-significance-category.json](./input/valueset-message-significance-category.json) ✔
---
### [detectedissue-example-allergy.json](./input/detectedissue-example-allergy.json)
*DetectedIssue:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [substance-example-f201-dust.json](./input/substance-example-f201-dust.json) ✔
---
### [observation-example-f005-hemoglobin.json](./input/observation-example-f005-hemoglobin.json) ✔
---
### [valueset-specimen-status.json](./input/valueset-specimen-status.json) ✔
---
### [operationoutcome-example-exception.json](./input/operationoutcome-example-exception.json) ✔
---
### [valueset-supplyrequest-reason.json](./input/valueset-supplyrequest-reason.json) ✔
---
### [namingsystem-example-id.json](./input/namingsystem-example-id.json)
*NamingSystem:*

**<sub>Keys lost during transform:</sub>**
```python
{'useContext'}
```

---
### [valueset-allergy-intolerance-criticality.json](./input/valueset-allergy-intolerance-criticality.json) ✔
---
### [valueset-choice-list-orientation.json](./input/valueset-choice-list-orientation.json) ✔
---
### [valueset-copy-number-event.json](./input/valueset-copy-number-event.json) ✔
---
### [valueset-link-type.json](./input/valueset-link-type.json) ✔
---
### [slot-example-unavailable.json](./input/slot-example-unavailable.json) ✔
---
### [valueset-postal-address-use.json](./input/valueset-postal-address-use.json) ✔
---
### [valueset-fm-conditions.json](./input/valueset-fm-conditions.json) ✔
---
### [valueset-days-of-week.json](./input/valueset-days-of-week.json) ✔
---
### [valueset-codesystem-content-mode.json](./input/valueset-codesystem-content-mode.json) ✔
---
### [valueset-age-units.json](./input/valueset-age-units.json) ✔
---
### [valueset-questionnaire-display-category.json](./input/valueset-questionnaire-display-category.json) ✔
---
### [valueset-relationship.json](./input/valueset-relationship.json) ✔
---
### [operation-task-set-input.json](./input/operation-task-set-input.json) ✔
---
### [encounter-example-xcda.json](./input/encounter-example-xcda.json)
*Encounter:*

**<sub>Keys lost during transform:</sub>**
```python
{'class'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reason'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient'}
```

---
### [valueset-encounter-special-arrangements.json](./input/valueset-encounter-special-arrangements.json) ✔
---
### [valueset-conditional-delete-status.json](./input/valueset-conditional-delete-status.json) ✔
---
### [flag-example.json](./input/flag-example.json) ✔
---
### [valueset-name-v3-representation.json](./input/valueset-name-v3-representation.json) ✔
---
### [valueset-contract-actorrole.json](./input/valueset-contract-actorrole.json) ✔
---
### [valueset-observation-category.json](./input/valueset-observation-category.json) ✔
---
### [operation-task-suspend.json](./input/operation-task-suspend.json) ✔
---
### [valueset-order-set-participant.json](./input/valueset-order-set-participant.json) ✔
---
### [substance-example-f202-staphylococcus.json](./input/substance-example-f202-staphylococcus.json) ✔
---
### [valueset-goal-status.json](./input/valueset-goal-status.json) ✔
---
### [person-example.json](./input/person-example.json)
*Person:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_gender'}
```

---
### [valueset-service-type.json](./input/valueset-service-type.json) ✔
---
### [valueset-timing-abbreviation.json](./input/valueset-timing-abbreviation.json) ✔
---
### [valueset-profile-code.json](./input/valueset-profile-code.json) ✔
---
### [practitioner-example-f006-rvdb.json](./input/practitioner-example-f006-rvdb.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [valueset-instance-availability.json](./input/valueset-instance-availability.json) ✔
---
### [observation-example-bloodpressure-cancel.json](./input/observation-example-bloodpressure-cancel.json)
*Observation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'comment'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'note'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

---
### [valueset-questionnaire-status.json](./input/valueset-questionnaire-status.json) ✔
---
### [organization-example-gastro.json](./input/organization-example-gastro.json) ✔
---
### [valueset-ucum-common.json](./input/valueset-ucum-common.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### [operation-conceptmap-translate.json](./input/operation-conceptmap-translate.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [valueset-cardinality-behavior.json](./input/valueset-cardinality-behavior.json) ✔
---
### [condition-example-f202-malignancy.json](./input/condition-example-f202-malignancy.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_dateRecorded', 'dateRecorded', 'patient', 'onsetQuantity'}
```

*Condition --> evidence:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-guide-page-kind.json](./input/valueset-guide-page-kind.json) ✔
---
### [valueset-manifestation-or-symptom.json](./input/valueset-manifestation-or-symptom.json) ✔
---
### [valueset-observation-relationshiptypes.json](./input/valueset-observation-relationshiptypes.json) ✔
---
### [valueset-identity-assuranceLevel.json](./input/valueset-identity-assuranceLevel.json) ✔
---
### [valueset-history-status.json](./input/valueset-history-status.json) ✔
---
### [valueset-action-required-behavior.json](./input/valueset-action-required-behavior.json) ✔
---
### [valueset-structure-definition-kind.json](./input/valueset-structure-definition-kind.json) ✔
---
### [valueset-audit-event-action.json](./input/valueset-audit-event-action.json) ✔
---
### [riskassessment-example.json](./input/riskassessment-example.json)
*RiskAssessment:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'date'}
```

---
### [organization-example-f001-burgers.json](./input/organization-example-f001-burgers.json) ✔
---
### [valueset-service-provision-conditions.json](./input/valueset-service-provision-conditions.json) ✔
---
### [valueset-specimen-treatment-procedure.json](./input/valueset-specimen-treatment-procedure.json) ✔
---
### [valueset-supplyrequest-kind.json](./input/valueset-supplyrequest-kind.json) ✔
---
### [valueset-cds-rule-participant.json](./input/valueset-cds-rule-participant.json) ✔
---
### [observation-example-unsat.json](./input/observation-example-unsat.json)
*Observation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'comment'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'note'}
```

---
### [valueset-service-product.json](./input/valueset-service-product.json) ✔
---
### [valueset-benefit-term.json](./input/valueset-benefit-term.json) ✔
---
### [valueset-address-use.json](./input/valueset-address-use.json) ✔
---
### [encounter-example-f201-20130404.json](./input/encounter-example-f201-20130404.json)
*Encounter:*

**<sub>Keys lost during transform:</sub>**
```python
{'class'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reason'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', '_class'}
```

---
### [valueset-episode-of-care-status.json](./input/valueset-episode-of-care-status.json) ✔
---
### [valueset-goal-start-event.json](./input/valueset-goal-start-event.json) ✔
---
### [slot-questionnaire.json](./input/slot-questionnaire.json) ✔
---
### [structuremap-example.json](./input/structuremap-example.json) ✔
---
### [valueset-dataelement-stringency.json](./input/valueset-dataelement-stringency.json) ✔
---
### [valueset-resource-slicing-rules.json](./input/valueset-resource-slicing-rules.json) ✔
---
### [encounter-example-f002-lung.json](./input/encounter-example-f002-lung.json)
*Encounter:*

**<sub>Keys lost during transform:</sub>**
```python
{'class'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reason'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient'}
```

---
### [valueset-unknown-content-code.json](./input/valueset-unknown-content-code.json) ✔
---
### [subscription-questionnaire.json](./input/subscription-questionnaire.json) ✔
---
### [valueset-immunization-recommendation-status.json](./input/valueset-immunization-recommendation-status.json) ✔
---
### [valueset-HGNC-geneIdentifiers.json](./input/valueset-HGNC-geneIdentifiers.json) ✔
---
### [valueset-concept-map-equivalence.json](./input/valueset-concept-map-equivalence.json) ✔
---
### [riskassessment-example-population.json](./input/riskassessment-example-population.json) ✔
---
### [valueset-payeetype.json](./input/valueset-payeetype.json) ✔
---
### [list-example.json](./input/list-example.json) ✔
---
### [patient-glossy-example.json](./input/patient-glossy-example.json)
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'careProvider'}
```

---
### [valueset-remittance-outcome.json](./input/valueset-remittance-outcome.json) ✔
---
### [operation-composition-document.json](./input/operation-composition-document.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [condition-example-f003-abscess.json](./input/condition-example-f003-abscess.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'encounter', 'dateRecorded', 'patient'}
```

*Condition --> evidence:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-operation-kind.json](./input/valueset-operation-kind.json) ✔
---
### [valueset-measure-data-usage.json](./input/valueset-measure-data-usage.json) ✔
---
### [valueset-metric-calibration-state.json](./input/valueset-metric-calibration-state.json) ✔
---
### [valueset-route-codes.json](./input/valueset-route-codes.json) ✔
---
### [valueset-assert-direction-codes.json](./input/valueset-assert-direction-codes.json) ✔
---
### [valueset-ucum-bodytemp.json](./input/valueset-ucum-bodytemp.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### [valueset-adjudication-error.json](./input/valueset-adjudication-error.json) ✔
---
### [valueset-flag-status.json](./input/valueset-flag-status.json) ✔
---
### [measurereport-questionnaire.json](./input/measurereport-questionnaire.json) ✔
---
### [valueset-anzsco-occupations.json](./input/valueset-anzsco-occupations.json)
*ValueSet:*

**<sub>Keys lost during transform:</sub>**
```python
{'useContext'}
```

---
### [practitioner-example-f005-al.json](./input/practitioner-example-f005-al.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [valueset-adjudication-reason.json](./input/valueset-adjudication-reason.json) ✔
---
### [valueset-audit-event-type.json](./input/valueset-audit-event-type.json) ✔
---
### [library-exclusive-breastfeeding-cds-logic.json](./input/library-exclusive-breastfeeding-cds-logic.json)
*Library:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'model', 'moduleMetadata', 'document', 'valueSet'}
```

---
### [appointment-example-request.json](./input/appointment-example-request.json)
*Appointment:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reason'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

*Appointment --> participant:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_required'}
```

---
### [operation-messageheader-process-message.json](./input/operation-messageheader-process-message.json) ✔
---
### [patient-example-proband.json](./input/patient-example-proband.json) ✔
---
### [patient-extensions-Patient-mothersMaidenName.json](./input/patient-extensions-Patient-mothersMaidenName.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [observation-example-f004-erythrocyte.json](./input/observation-example-f004-erythrocyte.json) ✔
---
### [valueset-sequence-species.json](./input/valueset-sequence-species.json) ✔
---
### [valueset-goal-status-reason.json](./input/valueset-goal-status-reason.json) ✔
---
### [practitioner-example-f002-pv.json](./input/practitioner-example-f002-pv.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [observation-genetics-Observation-dna-variant.json](./input/observation-genetics-Observation-dna-variant.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [substance-questionnaire.json](./input/substance-questionnaire.json) ✔
---
### [valueset-contract-action.json](./input/valueset-contract-action.json) ✔
---
### [valueset-patient-contact-relationship.json](./input/valueset-patient-contact-relationship.json) ✔
---
### [patient-example-us-extensions.json](./input/patient-example-us-extensions.json) ✔
---
### [observation-example-f206-staphylococcus.json](./input/observation-example-f206-staphylococcus.json)
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments', 'valueCodeableConcept'}
```

---
### [valueset-LOINC-53034-5-answerlist.json](./input/valueset-LOINC-53034-5-answerlist.json) ✔
---
### [valueset-patient-mpi-match.json](./input/valueset-patient-mpi-match.json) ✔
---
### [operation-task-fail.json](./input/operation-task-fail.json) ✔
---
### [valueset-address-type.json](./input/valueset-address-type.json) ✔
---
### [valueset-object-role.json](./input/valueset-object-role.json) ✔
---
### [valueset-issue-type.json](./input/valueset-issue-type.json) ✔
---
### [valueset-flag-priority.json](./input/valueset-flag-priority.json) ✔
---
### [binary-questionnaire.json](./input/binary-questionnaire.json) ✔
---
### [location-extensions-Location-alias.json](./input/location-extensions-Location-alias.json) ✔
---
### [valueset-module-metadata-resource-type.json](./input/valueset-module-metadata-resource-type.json) ✔
---
### [list-example-allergies.json](./input/list-example-allergies.json) ✔
---
### [valueset-quantity-comparator.json](./input/valueset-quantity-comparator.json) ✔
---
### [valueset-namingsystem-type.json](./input/valueset-namingsystem-type.json) ✔
---
### [valueset-LOINC-48002-0-answerlist.json](./input/valueset-LOINC-48002-0-answerlist.json) ✔
---
### [valueset-dicom-cid29.json](./input/valueset-dicom-cid29.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'requirements'}
```

---
### [encounter-example-f203-20130311.json](./input/encounter-example-f203-20130311.json)
*Encounter:*

**<sub>Keys lost during transform:</sub>**
```python
{'class'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reason'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', '_class'}
```

*Encounter --> hospitalization:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-media-view.json](./input/valueset-media-view.json) ✔
---
### [valueset-encounter-admit-source.json](./input/valueset-encounter-admit-source.json) ✔
---
### [valueset-event-timing.json](./input/valueset-event-timing.json) ✔
---
### [valueset-benefit-type.json](./input/valueset-benefit-type.json) ✔
---
### [namingsystem-questionnaire.json](./input/namingsystem-questionnaire.json) ✔
---
### [condition-example-f203-sepsis.json](./input/condition-example-f203-sepsis.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'encounter', 'dateRecorded', 'patient'}
```

---
### [appointmentresponse-example.json](./input/appointmentresponse-example.json) ✔
---
### [valueset-operation-parameter-use.json](./input/valueset-operation-parameter-use.json) ✔
---
### [valueset-observation-valueabsentreason.json](./input/valueset-observation-valueabsentreason.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

---
### [valueset-account-status.json](./input/valueset-account-status.json) ✔
---
### [valueset-care-plan-relationship.json](./input/valueset-care-plan-relationship.json) ✔
---
### [valueset-detectedissue-category.json](./input/valueset-detectedissue-category.json) ✔
---
### [valueset-note-type.json](./input/valueset-note-type.json) ✔
---
### [condition-example-f002-lung.json](./input/condition-example-f002-lung.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'encounter', 'dateRecorded', 'patient'}
```

---
### [valueset-benefit-unit.json](./input/valueset-benefit-unit.json) ✔
---
### [practitioner-example-f007-sh.json](./input/practitioner-example-f007-sh.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [device-example-ihe-pcd.json](./input/device-example-ihe-pcd.json)
*Device:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'model'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'modelNumber'}
```

---
### [valueset-metric-category.json](./input/valueset-metric-category.json) ✔
---
### [valueset-order-status.json](./input/valueset-order-status.json) ✔
---
### [valueset-c80-doc-typecodes.json](./input/valueset-c80-doc-typecodes.json) ✔
---
### [relatedperson-example.json](./input/relatedperson-example.json) ✔
---
### [valueset-example.json](./input/valueset-example.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_name', '_url', '_lockedDate', '_version', 'lockedDate'}
```

---
### [valueset-performer-role.json](./input/valueset-performer-role.json) ✔
---
### [valueset-device-use-request-status.json](./input/valueset-device-use-request-status.json) ✔
---
### [valueset-action-grouping-behavior.json](./input/valueset-action-grouping-behavior.json) ✔
---
### [valueset-payment-adjustment-reason.json](./input/valueset-payment-adjustment-reason.json) ✔
---
### [patient-example-dicom.json](./input/patient-example-dicom.json)
*Patient:*

**<sub>Keys lost during transform:</sub>**
```python
{'name'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_gender'}
```

---
### [valueset-clinical-findings.json](./input/valueset-clinical-findings.json) ✔
---
### [structuredefinition-questionnaire.json](./input/structuredefinition-questionnaire.json) ✔
---
### [valueset-supplement-type.json](./input/valueset-supplement-type.json) ✔
---
### [valueset-procedure-status.json](./input/valueset-procedure-status.json) ✔
---
### [operation-resource-validate.json](./input/operation-resource-validate.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [valueset-medication-codes.json](./input/valueset-medication-codes.json) ✔
---
### [valueset-testscript-profile-destination-types.json](./input/valueset-testscript-profile-destination-types.json) ✔
---
### [valueset-ex-program-code.json](./input/valueset-ex-program-code.json) ✔
---
### [valueset-action-type.json](./input/valueset-action-type.json) ✔
---
### [medicationexample3.json](./input/medicationexample3.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [valueset-xds-relationship-type.json](./input/valueset-xds-relationship-type.json) ✔
---
### [diagnosticreport-example-f201-brainct.json](./input/diagnosticreport-example-f201-brainct.json)
*DiagnosticReport:*

**<sub>Keys lost during transform:</sub>**
```python
{'performer'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'codedDiagnosis'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'conclusionCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

*DiagnosticReport --> performer:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'display', 'reference'}
```

---
### [patient-example-d.json](./input/patient-example-d.json) ✔
---
### [parameters-example.json](./input/parameters-example.json)
*Parameters --> parameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'resource'}
```

---
### [codesystem-extensions-CodeSystem-author.json](./input/codesystem-extensions-CodeSystem-author.json) ✔
---
### [valueset-cds-rule-trigger-type.json](./input/valueset-cds-rule-trigger-type.json) ✔
---
### [valueset-type-restful-interaction.json](./input/valueset-type-restful-interaction.json) ✔
---
### [patient-example.json](./input/patient-example.json)
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_gender', '_birthDate'}
```

---
### [valueset-care-plan-status.json](./input/valueset-care-plan-status.json) ✔
---
### [valueset-audit-event-outcome.json](./input/valueset-audit-event-outcome.json) ✔
---
### [valueset-list-mode.json](./input/valueset-list-mode.json) ✔
---
### [valueset-metric-calibration-type.json](./input/valueset-metric-calibration-type.json) ✔
---
### [observation-example-f203-bicarbonate.json](./input/observation-example-f203-bicarbonate.json)
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status'}
```

*Observation --> referenceRange:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'meaning'}
```

---
### [medication-example-f001-combivent.json](./input/medication-example-f001-combivent.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [supplydelivery-example.json](./input/supplydelivery-example.json)
*SupplyDelivery:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-service-modifiers.json](./input/valueset-service-modifiers.json) ✔
---
### [media-example-dicom.json](./input/media-example-dicom.json)
*Media:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'subtype'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'modality'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'deviceName'}
```

---
### [valueset-action-relationship-anchor.json](./input/valueset-action-relationship-anchor.json) ✔
---
### [medicationstatementexample6.json](./input/medicationstatementexample6.json)
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime', 'patient', 'wasNotTaken'}
```

---
### [patient-example-b.json](./input/patient-example-b.json)
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_gender'}
```

---
### [valueset-kos-title.json](./input/valueset-kos-title.json) ✔
---
### [location-example-ukpharmacy.json](./input/location-example-ukpharmacy.json) ✔
---
### [valueset-encounter-location-status.json](./input/valueset-encounter-location-status.json) ✔
---
### [medicationexample16.json](./input/medicationexample16.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [auditevent-example-disclosure.json](./input/auditevent-example-disclosure.json)
*AuditEvent:*

**<sub>Keys lost during transform:</sub>**
```python
{'purposeOfEvent'}
```

*AuditEvent --> agent:*

**<sub>Keys lost during transform:</sub>**
```python
{'purposeOfUse'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId', 'reference'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

*AuditEvent --> entity:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier', 'reference'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'what'}
```

*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_site'}
```

---
### [observation-genetics-Observation-gene-dnavariant.json](./input/observation-genetics-Observation-gene-dnavariant.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [compartmentdefinition-device.json](./input/compartmentdefinition-device.json) ✔
---
### [valueset-map-list-mode.json](./input/valueset-map-list-mode.json) ✔
---
### [valueset-chromosome-human.json](./input/valueset-chromosome-human.json) ✔
---
### [valueset-ucum-bodyweight.json](./input/valueset-ucum-bodyweight.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### [valueset-claim-type-link.json](./input/valueset-claim-type-link.json) ✔
---
### [valueset-identifier-type.json](./input/valueset-identifier-type.json) ✔
---
### [valueset-reference-version-rules.json](./input/valueset-reference-version-rules.json) ✔
---
### [valueset-item-type.json](./input/valueset-item-type.json) ✔
---
### [valueset-extension-context.json](./input/valueset-extension-context.json) ✔
---
### [valueset-contract-term-type.json](./input/valueset-contract-term-type.json) ✔
---
### [medicationexample11.json](./input/medicationexample11.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [schedule-example.json](./input/schedule-example.json) ✔
---
### [valueset-approach-site-codes.json](./input/valueset-approach-site-codes.json) ✔
---
### [valueset-object-lifecycle.json](./input/valueset-object-lifecycle.json) ✔
---
### [valueset-vaccination-protocol-dose-status.json](./input/valueset-vaccination-protocol-dose-status.json) ✔
---
### [valueset-medication-admin-status.json](./input/valueset-medication-admin-status.json) ✔
---
### [valueset-conformance-statement-kind.json](./input/valueset-conformance-statement-kind.json) ✔
---
### [valueset-doc-typecodes.json](./input/valueset-doc-typecodes.json) ✔
---
### [valueset-digital-media-subtype.json](./input/valueset-digital-media-subtype.json)
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### [valueset-payment-status.json](./input/valueset-payment-status.json) ✔
---
### [valueset-transaction-mode.json](./input/valueset-transaction-mode.json) ✔
---
### [valueset-medication-order-status.json](./input/valueset-medication-order-status.json) ✔
---
### [practitionerrole-questionnaire.json](./input/practitionerrole-questionnaire.json) ✔
---
### [substance-example.json](./input/substance-example.json) ✔
---
### [valueset-location-mode.json](./input/valueset-location-mode.json) ✔
---
### [codesystem-extensions-CodeSystem-workflow.json](./input/codesystem-extensions-CodeSystem-workflow.json) ✔
---
### [devicemetric-questionnaire.json](./input/devicemetric-questionnaire.json) ✔
---
### [valueset-match-grade.json](./input/valueset-match-grade.json) ✔
---
### [immunization-example.json](./input/immunization-example.json)
*Immunization:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'vaccinationProtocol', 'explanation', 'date'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'protocolApplied', 'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'performer', 'requester', 'wasNotGiven', 'reported'}
```

---
### [valueset-process-outcome.json](./input/valueset-process-outcome.json) ✔
---
### [practitioner-example-f203-jvg.json](./input/practitioner-example-f203-jvg.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_birthDate', 'practitionerRole'}
```

---
### [communicationrequest-example.json](./input/communicationrequest-example.json) ✔
---
### [codesystem-extensions-CodeSystem-keyword.json](./input/codesystem-extensions-CodeSystem-keyword.json) ✔
---
### [operation-structuredefinition-questionnaire.json](./input/operation-structuredefinition-questionnaire.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [valueset-immunization-site.json](./input/valueset-immunization-site.json) ✔
---
### [appointmentresponse-example-req.json](./input/appointmentresponse-example-req.json) ✔
---
### [valueset-assert-response-code-types.json](./input/valueset-assert-response-code-types.json) ✔
---
### [practitioner-example-f202-lm.json](./input/practitioner-example-f202-lm.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_birthDate', 'practitionerRole'}
```

---
### [valueset-doc-section-codes.json](./input/valueset-doc-section-codes.json) ✔
---
### [medication-example-f005-enalapril.json](./input/medication-example-f005-enalapril.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### [valueset-contact-point-use.json](./input/valueset-contact-point-use.json) ✔
---
### [person-example-f002-ariadne.json](./input/person-example-f002-ariadne.json) ✔
---
### [valueset-condition-severity.json](./input/valueset-condition-severity.json) ✔
---
### [operation-resource-meta-delete.json](./input/operation-resource-meta-delete.json) ✔
---
### [observation-example-genetics-2.json](./input/observation-example-genetics-2.json)
*Observation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'related'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'derivedFrom'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueCodeableConcept'}
```

*Observation --> component:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueCodeableConcept'}
```

---
### [enrollmentresponse-questionnaire.json](./input/enrollmentresponse-questionnaire.json) ✔
---
### [valueset-medication-package-form-codes.json](./input/valueset-medication-package-form-codes.json) ✔
---
### [medicationexample8.json](./input/medicationexample8.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [valueset-usps-state.json](./input/valueset-usps-state.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

---
### [valueset-vaccination-protocol-dose-status-reason.json](./input/valueset-vaccination-protocol-dose-status-reason.json) ✔
---
### [imagingstudy-questionnaire.json](./input/imagingstudy-questionnaire.json) ✔
---
### [valueset-slotstatus.json](./input/valueset-slotstatus.json) ✔
---
### [valueset-vision-base-codes.json](./input/valueset-vision-base-codes.json) ✔
---
### [valueset-message-reason-encounter.json](./input/valueset-message-reason-encounter.json) ✔
---
### [patient-example-c.json](./input/patient-example-c.json)
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'deceasedDateTime'}
```

---
### [valueset-restful-security-service.json](./input/valueset-restful-security-service.json) ✔
---
### [deviceusestatement-example.json](./input/deviceusestatement-example.json) ✔
---
### [organization-example.json](./input/organization-example.json) ✔
---
### [valueset-medication-dispense-status.json](./input/valueset-medication-dispense-status.json) ✔
---
### [valueset-referencerange-meaning.json](./input/valueset-referencerange-meaning.json)
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### [medicationadministrationexample3.json](./input/medicationadministrationexample3.json)
*MedicationAdministration:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'prescription'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'request'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitioner', 'patient', 'effectiveTimePeriod'}
```

*MedicationAdministration --> dosage:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'quantity'}
```

---
### [valueset-measure-report-status.json](./input/valueset-measure-report-status.json) ✔
---
### [account-example.json](./input/account-example.json)
*Account:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [enrollmentrequest-example.json](./input/enrollmentrequest-example.json)
*EnrollmentRequest:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'subject', 'organization'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'candidate'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'relationship'}
```

---
### [healthcareservice-questionnaire.json](./input/healthcareservice-questionnaire.json) ✔
---
### [person-grahame.json](./input/person-grahame.json)
*Person:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_gender'}
```

---
### [compartmentdefinition-encounter.json](./input/compartmentdefinition-encounter.json) ✔
---
### [medicationadministrationexample2.json](./input/medicationadministrationexample2.json)
*MedicationAdministration:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'prescription'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'request'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitioner', 'patient', 'effectiveTimePeriod'}
```

*MedicationAdministration --> dosage:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'quantity'}
```

---
### [auditevent-example.json](./input/auditevent-example.json)
*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

*AuditEvent --> entity:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'what'}
```

*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

---
### [operation-task-stop.json](./input/operation-task-stop.json) ✔
---
### [operationoutcome-example-searchfail.json](./input/operationoutcome-example-searchfail.json) ✔
---
### [practitioner-example-f003-mv.json](./input/practitioner-example-f003-mv.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [flag-example-encounter.json](./input/flag-example-encounter.json) ✔
---
### [valueset-bodysite-laterality.json](./input/valueset-bodysite-laterality.json) ✔
---
### [bodysite-questionnaire.json](./input/bodysite-questionnaire.json) ✔
---
### [valueset-ruleset.json](./input/valueset-ruleset.json) ✔
---
### [observation-genetics-Observation-gene-amino-acid-change.json](./input/observation-genetics-Observation-gene-amino-acid-change.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [valueset-content-type.json](./input/valueset-content-type.json) ✔
---
### [immunization-questionnaire.json](./input/immunization-questionnaire.json) ✔
---
### [observation-example-f205-egfr.json](./input/observation-example-f205-egfr.json)
*Observation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'comment'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'note'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status'}
```

*Observation --> component:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-identifier-use.json](./input/valueset-identifier-use.json) ✔
---
### [valueset-modified-foodtype.json](./input/valueset-modified-foodtype.json) ✔
---
### [valueset-type-derivation-rule.json](./input/valueset-type-derivation-rule.json) ✔
---
### [valueset-provider-qualification.json](./input/valueset-provider-qualification.json) ✔
---
### [observation-example-genetics-5.json](./input/observation-example-genetics-5.json)
*Observation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'related'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueCodeableConcept'}
```

---
### [medicationstatementexample7.json](./input/medicationstatementexample7.json)
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime', 'patient', 'wasNotTaken'}
```

---
### [procedure-example.json](./input/procedure-example.json)
*Procedure:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'performedDateTime', 'reasonCodeableConcept', 'notes'}
```

---
### [codesystem-extensions-CodeSystem-end.json](./input/codesystem-extensions-CodeSystem-end.json) ✔
---
### [valueset-contact-point-system.json](./input/valueset-contact-point-system.json) ✔
---
### [valueset-abstract-types.json](./input/valueset-abstract-types.json) ✔
---
### [valueset-claim-use-link.json](./input/valueset-claim-use-link.json) ✔
---
### [valueset-location-physical-type.json](./input/valueset-location-physical-type.json) ✔
---
### [medicationexample5.json](./input/medicationexample5.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### [substance-example-f203-potassium.json](./input/substance-example-f203-potassium.json) ✔
---
### [valueset-provenance-agent-type.json](./input/valueset-provenance-agent-type.json) ✔
---
### [valueset-diagnostic-order-priority.json](./input/valueset-diagnostic-order-priority.json) ✔
---
### [valueset-referralstatus.json](./input/valueset-referralstatus.json) ✔
---
### [valueset-action-relationship-type.json](./input/valueset-action-relationship-type.json) ✔
---
### [location-example-patients-home.json](./input/location-example-patients-home.json) ✔
---
### [valueset-filter-operator.json](./input/valueset-filter-operator.json) ✔
---
### [valueset-occurrence-codes.json](./input/valueset-occurrence-codes.json) ✔
---
### [valueset-group-type.json](./input/valueset-group-type.json) ✔
---
### [valueset-search-xpath-usage.json](./input/valueset-search-xpath-usage.json) ✔
---
### [valueset-observation-codes.json](./input/valueset-observation-codes.json) ✔
---
### [valueset-measure-population.json](./input/valueset-measure-population.json) ✔
---
### [contract-example.json](./input/contract-example.json)
*Contract:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [slot-example-busy.json](./input/slot-example-busy.json) ✔
---
### [valueset-extensions-ValueSet-workflow.json](./input/valueset-extensions-ValueSet-workflow.json) ✔
---
### [valueset-data-absent-reason.json](./input/valueset-data-absent-reason.json) ✔
---
### [valueset-audit-event-sub-type.json](./input/valueset-audit-event-sub-type.json) ✔
---
### [valueset-metric-color.json](./input/valueset-metric-color.json) ✔
---
### [valueset-action-participant-type.json](./input/valueset-action-participant-type.json) ✔
---
### [valueset-texture-code.json](./input/valueset-texture-code.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_description'}
```

---
### [valueset-no-immunization-reason.json](./input/valueset-no-immunization-reason.json) ✔
---
### [operation-resource-meta.json](./input/operation-resource-meta.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [codesystem-extensions-CodeSystem-effective.json](./input/codesystem-extensions-CodeSystem-effective.json) ✔
---
### [organization-example-good-health-care.json](./input/organization-example-good-health-care.json) ✔
---
### [riskassessment-example-prognosis.json](./input/riskassessment-example-prognosis.json)
*RiskAssessment:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'date'}
```

*RiskAssessment --> prediction:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'probabilityCodeableConcept'}
```

---
### [valueset-measure-report-type.json](./input/valueset-measure-report-type.json) ✔
---
### [media-example.json](./input/media-example.json)
*Media:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'subtype'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'modality'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_frames', 'deviceName'}
```

---
### [valueset-procedure-progress-status-codes.json](./input/valueset-procedure-progress-status-codes.json) ✔
---
### [valueset-goal-acceptance-status.json](./input/valueset-goal-acceptance-status.json) ✔
---
### [valueset-task-priority.json](./input/valueset-task-priority.json) ✔
---
### [audit-event-example-vread.json](./input/audit-event-example-vread.json)
*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

*AuditEvent --> entity:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reference'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'what'}
```

*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

---
### [library-exclusive-breastfeeding-cqm-logic.json](./input/library-exclusive-breastfeeding-cqm-logic.json)
*Library:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'model', 'moduleMetadata', 'document', 'valueSet'}
```

---
### [valueset-activity-definition-category.json](./input/valueset-activity-definition-category.json) ✔
---
### [valueset-system-restful-interaction.json](./input/valueset-system-restful-interaction.json) ✔
---
### [observation-example.json](./input/observation-example.json)
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'encounter', 'effectiveDateTime'}
```

---
### [condition-example-f001-heart.json](./input/condition-example-f001-heart.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'encounter', 'dateRecorded', 'patient'}
```

---
### [valueset-dataelement-sdcobjectclassproperty.json](./input/valueset-dataelement-sdcobjectclassproperty.json) ✔
---
### [observation-example-genetics-4.json](./input/observation-example-genetics-4.json)
*Observation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'related'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'hasMember'}
```

---
### [valueset-service-place.json](./input/valueset-service-place.json) ✔
---
### [practitioner-example-f001-evdb.json](./input/practitioner-example-f001-evdb.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [valueset-diagnostic-order-status.json](./input/valueset-diagnostic-order-status.json) ✔
---
### [practitionerrole-example.json](./input/practitionerrole-example.json)
*PractitionerRole:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'role'}
```

---
### [valueset-procedure-code.json](./input/valueset-procedure-code.json) ✔
---
### [valueset-detectedissue-mitigation-action.json](./input/valueset-detectedissue-mitigation-action.json) ✔
---
### [medication-example-f003-tolbutamide.json](./input/medication-example-f003-tolbutamide.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### [valueset-condition-category.json](./input/valueset-condition-category.json) ✔
---
### [valueset-immunization-reason.json](./input/valueset-immunization-reason.json) ✔
---
### [us-core-Patient-race.json](./input/us-core-Patient-race.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [library-example.json](./input/library-example.json)
*Library:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'model', 'moduleMetadata', 'document', 'valueSet'}
```

---
### [valueset-HGVSvariant.json](./input/valueset-HGVSvariant.json) ✔
---
### [valueset-map-model-mode.json](./input/valueset-map-model-mode.json) ✔
---
### [compartmentdefinition-relatedperson.json](./input/compartmentdefinition-relatedperson.json) ✔
---
### [valueset-ldlcholesterol-codes.json](./input/valueset-ldlcholesterol-codes.json) ✔
---
### [medicationstatementexample5.json](./input/medicationstatementexample5.json)
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime', 'patient', 'reasonForUseCodeableConcept', 'wasNotTaken'}
```

---
### [slot-example-tentative.json](./input/slot-example-tentative.json) ✔
---
### [valueset-communication-status.json](./input/valueset-communication-status.json) ✔
---
### [valueset-encounter-discharge-disposition.json](./input/valueset-encounter-discharge-disposition.json) ✔
---
### [valueset-supplyrequest-when.json](./input/valueset-supplyrequest-when.json) ✔
---
### [valueset-extensions-ValueSet-author.json](./input/valueset-extensions-ValueSet-author.json) ✔
---
### [valueset-conformance-resource-status.json](./input/valueset-conformance-resource-status.json) ✔
---
### [valueset-classification-or-context.json](./input/valueset-classification-or-context.json) ✔
---
### [diagnosticreport-hla-genetics-results-example.json](./input/diagnosticreport-hla-genetics-results-example.json)
*DiagnosticReport:*

**<sub>Keys lost during transform:</sub>**
```python
{'performer'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

*DiagnosticReport --> performer:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'display', 'reference'}
```

---
### [medicationexample14.json](./input/medicationexample14.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [substance-example-silver-nitrate-product.json](./input/substance-example-silver-nitrate-product.json) ✔
---
### [valueset-operation-outcome.json](./input/valueset-operation-outcome.json) ✔
---
### [consensus-sequence-block-questionnaire.json](./input/consensus-sequence-block-questionnaire.json) ✔
---
### [valueset-service-uscls.json](./input/valueset-service-uscls.json) ✔
---
### [valueset-adjudication.json](./input/valueset-adjudication.json) ✔
---
### [valueset-subscription-status.json](./input/valueset-subscription-status.json) ✔
---
### [valueset-participant-role.json](./input/valueset-participant-role.json) ✔
---
### [valueset-animal-species.json](./input/valueset-animal-species.json) ✔
---
### [valueset-flag-code.json](./input/valueset-flag-code.json) ✔
---
### [operationoutcome-questionnaire.json](./input/operationoutcome-questionnaire.json) ✔
---
### [valueset-supplyrequest-status.json](./input/valueset-supplyrequest-status.json) ✔
---
### [valueset-subscription-tag.json](./input/valueset-subscription-tag.json) ✔
---
### [media-example-sound.json](./input/media-example-sound.json) ✔
---
### [valueset-animal-breeds.json](./input/valueset-animal-breeds.json) ✔
---
### [valueset-dicm-402-roleid.json](./input/valueset-dicm-402-roleid.json) ✔
---
### [operation-resource-meta-add.json](./input/operation-resource-meta-add.json) ✔
---
### [operation-task-start.json](./input/operation-task-start.json) ✔
---
### [valueset-versioning-policy.json](./input/valueset-versioning-policy.json) ✔
---
### [valueset-observation-interpretation.json](./input/valueset-observation-interpretation.json) ✔
---
### [operation-list-find.json](./input/operation-list-find.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [valueset-questionnaire-answers.json](./input/valueset-questionnaire-answers.json) ✔
---
### [valueset-supplydelivery-status.json](./input/valueset-supplydelivery-status.json) ✔
---
### [valueset-resource-aggregation-mode.json](./input/valueset-resource-aggregation-mode.json) ✔
---
### [organization-questionnaire.json](./input/organization-questionnaire.json) ✔
---
### [patient-example-animal.json](./input/patient-example-animal.json)
*Patient:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'animal'}
```

---
### [valueset-action-behavior-type.json](./input/valueset-action-behavior-type.json) ✔
---
### [searchparameter-example-extension.json](./input/searchparameter-example-extension.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [basic-example-narrative.json](./input/basic-example-narrative.json) ✔
---
### [searchparameter-example.json](./input/searchparameter-example.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'requirements', '_requirements'}
```

---
### [medicationexample2.json](./input/medicationexample2.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [encounter-example-f001-heart.json](./input/encounter-example-f001-heart.json)
*Encounter:*

**<sub>Keys lost during transform:</sub>**
```python
{'class'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reason'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient'}
```

---
### [valueset-communication-request-status.json](./input/valueset-communication-request-status.json) ✔
---
### [device-example-software.json](./input/device-example-software.json) ✔
---
### [coverage-example-2.json](./input/coverage-example-2.json)
*Coverage:*

**<sub>Keys lost during transform:</sub>**
```python
{'relationship', 'type'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'beneficiaryReference',
 'issuerReference',
 'plan',
 'planholderReference',
 'subPlan'}
```

---
### [valueset-action-cardinality-behavior.json](./input/valueset-action-cardinality-behavior.json) ✔
---
### [valueset-surface.json](./input/valueset-surface.json) ✔
---
### [allergyintolerance-medication.json](./input/allergyintolerance-medication.json)
*AllergyIntolerance:*

**<sub>Keys lost during transform:</sub>**
```python
{'category'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'recordedDate', '_recordedDate', 'substance', 'status'}
```

---
### [valueset-message-transport.json](./input/valueset-message-transport.json) ✔
---
### [observation-example-glasgow-qa.json](./input/observation-example-glasgow-qa.json)
*Observation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'related'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'derivedFrom'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

*Observation --> referenceRange:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'meaning'}
```

---
### [valueset-marital-status.json](./input/valueset-marital-status.json) ✔
---
### [location-questionnaire.json](./input/location-questionnaire.json) ✔
---
### [valueset-digital-media-type.json](./input/valueset-digital-media-type.json) ✔
---
### [valueset-response-code.json](./input/valueset-response-code.json) ✔
---
### [operation-valueset-expand.json](./input/operation-valueset-expand.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [valueset-claim-subtype.json](./input/valueset-claim-subtype.json) ✔
---
### [encounter-example.json](./input/encounter-example.json)
*Encounter:*

**<sub>Keys lost during transform:</sub>**
```python
{'class'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient'}
```

---
### [valueset-resource-validation-mode.json](./input/valueset-resource-validation-mode.json) ✔
---
### [operation-task-cancel.json](./input/operation-task-cancel.json) ✔
---
### [valueset-use-context.json](./input/valueset-use-context.json)
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### [valueset-service-category.json](./input/valueset-service-category.json) ✔
---
### [valueset-list-status.json](./input/valueset-list-status.json) ✔
---
### [organization-example-f002-burgers-card.json](./input/organization-example-f002-burgers-card.json) ✔
---
### [valueset-fm-itemtype.json](./input/valueset-fm-itemtype.json) ✔
---
### [valueset-composition-attestation-mode.json](./input/valueset-composition-attestation-mode.json) ✔
---
### [valueset-audit-source-type.json](./input/valueset-audit-source-type.json) ✔
---
### [coverage-example.json](./input/coverage-example.json)
*Coverage:*

**<sub>Keys lost during transform:</sub>**
```python
{'relationship', 'type'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'sequence'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'beneficiaryReference',
 'issuerReference',
 'plan',
 'planholderReference',
 'subPlan'}
```

---
### [patient-mpi-search.json](./input/patient-mpi-search.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'idempotent'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'affectsState'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'requirements'}
```

*OperationDefinition --> parameter:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [person-provider-directory.json](./input/person-provider-directory.json) ✔
---
### [paymentnotice-example.json](./input/paymentnotice-example.json)
*PaymentNotice:*

**<sub>Keys lost during transform:</sub>**
```python
{'paymentStatus'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'requestReference', 'organizationReference'}
```

---
### [valueset-protocol-type.json](./input/valueset-protocol-type.json) ✔
---
### [valueset-goal-relationship-type.json](./input/valueset-goal-relationship-type.json) ✔
---
### [valueset-substance-code.json](./input/valueset-substance-code.json) ✔
---
### [valueset-signature-type.json](./input/valueset-signature-type.json) ✔
---
### [valueset-example-intensional.json](./input/valueset-example-intensional.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_name', '_url', '_version'}
```

*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [enrollmentresponse-example.json](./input/enrollmentresponse-example.json)
*EnrollmentResponse:*

**<sub>Keys lost during transform:</sub>**
```python
{'outcome'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'requestOrganization'}
```

---
### [valueset-trigger-type.json](./input/valueset-trigger-type.json) ✔
---
### [operation-task-finish.json](./input/operation-task-finish.json) ✔
---
### [medication-example-f202-flucloxacilline.json](./input/medication-example-f202-flucloxacilline.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [group-example.json](./input/group-example.json)
*Group --> characteristic:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueCodeableConcept'}
```

---
### [appointment-example.json](./input/appointment-example.json) ✔
---
### [observation-example-f001-glucose.json](./input/observation-example-f001-glucose.json) ✔
---
### [valueset-intervention.json](./input/valueset-intervention.json) ✔
---
### [valueset-diagnostic-report-status.json](./input/valueset-diagnostic-report-status.json) ✔
---
### [elementdefinition-11179-DataElement-objectClassProperty.json](./input/elementdefinition-11179-DataElement-objectClassProperty.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [valueset-diagnostic-order-event.json](./input/valueset-diagnostic-order-event.json) ✔
---
### [operation-valueset-validate-code.json](./input/operation-valueset-validate-code.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [relatedperson-questionnaire.json](./input/relatedperson-questionnaire.json) ✔
---
### [operation-resource-cds-hook.json](./input/operation-resource-cds-hook.json) ✔
---
### [detectedissue-example.json](./input/detectedissue-example.json)
*DetectedIssue:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'date', 'category'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'code'}
```

---
### [valueset-example-yesnodontknow.json](./input/valueset-example-yesnodontknow.json)
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### [practitioner-questionnaire.json](./input/practitioner-questionnaire.json) ✔
---
### [valueset-contract-subtype.json](./input/valueset-contract-subtype.json) ✔
---
### [relatedperson-example-peter.json](./input/relatedperson-example-peter.json) ✔
---
### [audit-event-example-search.json](./input/audit-event-example-search.json)
*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

---
### [compartmentdefinition-practitioner.json](./input/compartmentdefinition-practitioner.json) ✔
---
### [medicationexample7.json](./input/medicationexample7.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [valueset-formatcodes.json](./input/valueset-formatcodes.json) ✔
---
### [dataelement-questionnaire.json](./input/dataelement-questionnaire.json) ✔
---
### [observation-example-bloodpressure.json](./input/observation-example-bloodpressure.json)
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

*Observation --> component:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-example-expansion.json](./input/valueset-example-expansion.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

*ValueSet --> expansion:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_timestamp', '_offset', '_total', '_identifier', 'fhir_comments'}
```

---
### [valueset-vision-product.json](./input/valueset-vision-product.json) ✔
---
### [valueset-encounter-reason.json](./input/valueset-encounter-reason.json) ✔
---
### [valueset-supplydelivery-type.json](./input/valueset-supplydelivery-type.json) ✔
---
### [encounter-example-f202-20130128.json](./input/encounter-example-f202-20130128.json)
*Encounter:*

**<sub>Keys lost during transform:</sub>**
```python
{'class'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reason'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', '_class', 'indication'}
```

---
### [visionprescription-example.json](./input/visionprescription-example.json)
*VisionPrescription:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'dispense'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'lensSpecification'}
```

---
### [valueset-message-events.json](./input/valueset-message-events.json) ✔
---
### [patient-example-xcda.json](./input/patient-example-xcda.json) ✔
---
### [valueset-property-representation.json](./input/valueset-property-representation.json) ✔
---
### [valueset-questionnaire-category.json](./input/valueset-questionnaire-category.json) ✔
---
### [valueset-condition-predecessor.json](./input/valueset-condition-predecessor.json) ✔
---
### [device-example-udi1.json](./input/device-example-udi1.json)
*Device:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'model'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'modelNumber'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'udiCarrier'}
```

---
### [valueset-probability-distribution-type.json](./input/valueset-probability-distribution-type.json) ✔
---
### [valueset-contract-type.json](./input/valueset-contract-type.json) ✔
---
### [detectedissue-example-lab.json](./input/detectedissue-example-lab.json)
*DetectedIssue:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [patient-extensions-Patient-age.json](./input/patient-extensions-Patient-age.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [valueset-observation-status.json](./input/valueset-observation-status.json) ✔
---
### [valueset-care-plan-activity.json](./input/valueset-care-plan-activity.json) ✔
---
### [valueset-benefit-network.json](./input/valueset-benefit-network.json) ✔
---
### [procedure-example-implant.json](./input/procedure-example-implant.json)
*Procedure:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'performedDateTime', 'reasonCodeableConcept', 'notes'}
```

---
### [valueset-procedure-followup.json](./input/valueset-procedure-followup.json) ✔
---
### [valueset-participationstatus.json](./input/valueset-participationstatus.json) ✔
---
### [medicationadministrationexample1.json](./input/medicationadministrationexample1.json)
*MedicationAdministration:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'prescription'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'request'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitioner', 'patient', 'effectiveTimePeriod'}
```

*MedicationAdministration --> dosage:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'quantity'}
```

---
### [condition-example-stroke.json](./input/condition-example-stroke.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'patient'}
```

---
### [valueset-condition-cause.json](./input/valueset-condition-cause.json) ✔
---
### [medication-example-f203-paracetamol.json](./input/medication-example-f203-paracetamol.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [devicecomponent-questionnaire.json](./input/devicecomponent-questionnaire.json) ✔
---
### [organization-example-lab.json](./input/organization-example-lab.json) ✔
---
### [valueset-medication-form-codes.json](./input/valueset-medication-form-codes.json) ✔
---
### [sequence-questionnaire.json](./input/sequence-questionnaire.json) ✔
---
### [valueset-name-part-qualifier.json](./input/valueset-name-part-qualifier.json) ✔
---
### [valueset-encounter-class.json](./input/valueset-encounter-class.json) ✔
---
### [patient-example-f201-roel.json](./input/patient-example-f201-roel.json)
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_deceasedBoolean', '_active'}
```

---
### [codesystem-example.json](./input/codesystem-example.json)
*CodeSystem:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_url', '_version', '_caseSensitive'}
```

*CodeSystem --> concept:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-device-use-request-priority.json](./input/valueset-device-use-request-priority.json) ✔
---
### [practitioner-example.json](./input/practitioner-example.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [valueset-task-status.json](./input/valueset-task-status.json) ✔
---
### [basic-example.json](./input/basic-example.json) ✔
---
### [valueset-risk-probability.json](./input/valueset-risk-probability.json) ✔
---
### [observation-genetics-Observation-gene-identifier.json](./input/observation-genetics-Observation-gene-identifier.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [valueset-conformance-expectation.json](./input/valueset-conformance-expectation.json) ✔
---
### [valueset-constraint-severity.json](./input/valueset-constraint-severity.json) ✔
---
### [immunizationrecommendation-example.json](./input/immunizationrecommendation-example.json)
*ImmunizationRecommendation:*

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'authority', 'date'}
```

*ImmunizationRecommendation --> recommendation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'protocol', 'date', 'doseNumber'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'description', 'series'}
```

---
### [valueset-occurrence-span-codes.json](./input/valueset-occurrence-span-codes.json) ✔
---
### [valueset-action-precheck-behavior.json](./input/valueset-action-precheck-behavior.json) ✔
---
### [operationoutcome-example.json](./input/operationoutcome-example.json) ✔
---
### [valueset-all-types.json](./input/valueset-all-types.json) ✔
---
### [riskassessment-example-cardiac.json](./input/riskassessment-example-cardiac.json)
*RiskAssessment:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'date'}
```

---
### [valueset-nutrient-code.json](./input/valueset-nutrient-code.json) ✔
---
### [valueset-additionalmaterials.json](./input/valueset-additionalmaterials.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### [valueset-doc-classcodes.json](./input/valueset-doc-classcodes.json) ✔
---
### [operation-encounter-everything.json](./input/operation-encounter-everything.json) ✔
---
### [valueset-object-type.json](./input/valueset-object-type.json) ✔
---
### [valueset-body-site.json](./input/valueset-body-site.json) ✔
---
### [compartmentdefinition-patient.json](./input/compartmentdefinition-patient.json) ✔
---
### [observation-example-genetics-3.json](./input/observation-example-genetics-3.json)
*Observation:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'related', 'comment'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'note', 'derivedFrom'}
```

---
### [valueset-focal-subject.json](./input/valueset-focal-subject.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

---
### [valueset-coverage-exception.json](./input/valueset-coverage-exception.json) ✔
---
### [valueset-protocol-status.json](./input/valueset-protocol-status.json) ✔
---
### [valueset-vaccine-code.json](./input/valueset-vaccine-code.json) ✔
---
### [medicationexample6.json](./input/medicationexample6.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [valueset-module-metadata-status.json](./input/valueset-module-metadata-status.json) ✔
---
### [location-example-hl7hq.json](./input/location-example-hl7hq.json)
*Location:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status'}
```

---
### [medicationexample17.json](./input/medicationexample17.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [observation-example-satO2.json](./input/observation-example-satO2.json)
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

---
### [valueset-dataelement-sdcobjectclass.json](./input/valueset-dataelement-sdcobjectclass.json) ✔
---
### [valueset-sequence-variationID.json](./input/valueset-sequence-variationID.json) ✔
---
### [person-patient-portal.json](./input/person-patient-portal.json) ✔
---
### [valueset-reason-medication-not-given-codes.json](./input/valueset-reason-medication-not-given-codes.json) ✔
---
### [list-example-empty.json](./input/list-example-empty.json) ✔
---
### [valueset-extensions-ValueSet-keyword.json](./input/valueset-extensions-ValueSet-keyword.json) ✔
---
### [operationoutcome-example-allok.json](./input/operationoutcome-example-allok.json) ✔
---
### [medicationexample12.json](./input/medicationexample12.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

---
### [valueset-contactentity-type.json](./input/valueset-contactentity-type.json) ✔
---
### [valueset-module-metadata-contributor.json](./input/valueset-module-metadata-contributor.json) ✔
---
### [valueset-value-codes.json](./input/valueset-value-codes.json) ✔
---
### [valueset-issue-severity.json](./input/valueset-issue-severity.json) ✔
---
### [valueset-precheck-behavior.json](./input/valueset-precheck-behavior.json) ✔
---
### [diagnosticreport-example-ultrasound.json](./input/diagnosticreport-example-ultrasound.json)
*DiagnosticReport:*

**<sub>Keys lost during transform:</sub>**
```python
{'performer'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'image'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'media'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

*DiagnosticReport --> performer:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'reference'}
```

---
### [audit-event-example-login.json](./input/audit-event-example-login.json)
*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

---
### [valueset-practitioner-specialty.json](./input/valueset-practitioner-specialty.json) ✔
---
### [valueset-location-status.json](./input/valueset-location-status.json) ✔
---
### [valueset-missing-tooth-reason.json](./input/valueset-missing-tooth-reason.json) ✔
---
### [valueset-dicm-405-mediatype.json](./input/valueset-dicm-405-mediatype.json) ✔
---
### [appointment-example2doctors.json](./input/appointment-example2doctors.json) ✔
---
### [location-example-ambulance.json](./input/location-example-ambulance.json) ✔
---
### [operation-codesystem-lookup.json](./input/operation-codesystem-lookup.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [valueset-fips-county.json](./input/valueset-fips-county.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

---
### [practitioner-example-f201-ab.json](./input/practitioner-example-f201-ab.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [valueset-administrative-gender.json](./input/valueset-administrative-gender.json) ✔
---
### [valueset-clinical-impression-status.json](./input/valueset-clinical-impression-status.json) ✔
---
### [binary-example.json](./input/binary-example.json)
*Binary:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'content'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'data'}
```

---
### [valueset-encounter-type.json](./input/valueset-encounter-type.json) ✔
---
### [valueset-guide-dependency-type.json](./input/valueset-guide-dependency-type.json) ✔
---
### [valueset-list-empty-reason.json](./input/valueset-list-empty-reason.json) ✔
---
### [practitioner-example-xcda1.json](./input/practitioner-example-xcda1.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [practitioner-example-f004-rb.json](./input/practitioner-example-f004-rb.json)
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### [valueset-icd-10.json](./input/valueset-icd-10.json) ✔
---
### [valueset-sequence-referenceSeq.json](./input/valueset-sequence-referenceSeq.json) ✔
---
### [valueset-cpt-all.json](./input/valueset-cpt-all.json) ✔
---
### [valueset-contract-term-subtype.json](./input/valueset-contract-term-subtype.json) ✔
---
### [valueset-questionnaire-answers-status.json](./input/valueset-questionnaire-answers-status.json) ✔
---
### [valueset-encounter-priority.json](./input/valueset-encounter-priority.json) ✔
---
### [operationoutcome-example-validationfail.json](./input/operationoutcome-example-validationfail.json) ✔
---
### [medication-example-f004-metoprolol.json](./input/medication-example-f004-metoprolol.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### [basic-example2.json](./input/basic-example2.json) ✔
---
### [valueset-namingsystem-identifier-type.json](./input/valueset-namingsystem-identifier-type.json) ✔
---
### [valueset-document-mode.json](./input/valueset-document-mode.json) ✔
---
### [valueset-care-plan-category.json](./input/valueset-care-plan-category.json) ✔
---
### [valueset-restful-conformance-mode.json](./input/valueset-restful-conformance-mode.json) ✔
---
### [allergyintolerance-example.json](./input/allergyintolerance-example.json)
*AllergyIntolerance:*

**<sub>Keys lost during transform:</sub>**
```python
{'category'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_category',
 '_criticality',
 '_lastOccurence',
 '_onset',
 '_recordedDate',
 '_status',
 '_type',
 'lastOccurence',
 'onset',
 'recordedDate',
 'reporter',
 'status',
 'substance'}
```

*AllergyIntolerance --> reaction:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'certainty', 'fhir_comments'}
```

---
### [valueset-service-pharmacy.json](./input/valueset-service-pharmacy.json) ✔
---
### [valueset-reason-medication-given-codes.json](./input/valueset-reason-medication-given-codes.json) ✔
---
### [valueset-tooth.json](./input/valueset-tooth.json) ✔
---
### [searchparameter-questionnaire.json](./input/searchparameter-questionnaire.json) ✔
---
### [valueset-fundsreserve.json](./input/valueset-fundsreserve.json) ✔
---
### [valueset-encounter-diet.json](./input/valueset-encounter-diet.json) ✔
---
### [valueset-forms.json](./input/valueset-forms.json) ✔
---
### [valueset-allergy-intolerance-type.json](./input/valueset-allergy-intolerance-type.json) ✔
---
### [valueset-service-referral-method.json](./input/valueset-service-referral-method.json) ✔
---
### [valueset-metric-operational-status.json](./input/valueset-metric-operational-status.json) ✔
---
### [patient-extensions-Patient-birthOrderBoolean.json](./input/patient-extensions-Patient-birthOrderBoolean.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [valueset-list-item-flag.json](./input/valueset-list-item-flag.json) ✔
---
### [valueset-sequence-type.json](./input/valueset-sequence-type.json) ✔
---
### [valueset-measure-scoring.json](./input/valueset-measure-scoring.json) ✔
---
### [valueset-required-behavior.json](./input/valueset-required-behavior.json) ✔
---
### [audit-event-example-logout.json](./input/audit-event-example-logout.json)
*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

---
### [location-example-room.json](./input/location-example-room.json) ✔
---
### [goal-example.json](./input/goal-example.json)
*Goal:*

**<sub>Keys lost during transform:</sub>**
```python
{'description'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'status'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'achievementStatus', 'lifecycleStatus'}
```

---
### [task-example.json](./input/task-example.json)
*Task:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'creator', 'created', 'subject', 'type'}
```

---
### [valueset-variant-state.json](./input/valueset-variant-state.json) ✔
---
### [diagnosticreport-genetics-DiagnosticReport-assessed-condition.json](./input/diagnosticreport-genetics-DiagnosticReport-assessed-condition.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [device-example-pacemaker.json](./input/device-example-pacemaker.json)
*Device:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'model'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'modelNumber'}
```

---
### [valueset-related-claim-relationship.json](./input/valueset-related-claim-relationship.json) ✔
---
### [valueset-substance-category.json](./input/valueset-substance-category.json) ✔
---
### [valueset-entformula-type.json](./input/valueset-entformula-type.json) ✔
---
### [namingsystem-example.json](./input/namingsystem-example.json) ✔
---
### [organization-extensions-Organization-alias.json](./input/organization-extensions-Organization-alias.json) ✔
---
### [valueset-bodysite-relative-location.json](./input/valueset-bodysite-relative-location.json) ✔
---
### [valueset-narrative-status.json](./input/valueset-narrative-status.json) ✔
---
### [valueset-animal-genderstatus.json](./input/valueset-animal-genderstatus.json) ✔
---
### [list-example-medlist.json](./input/list-example-medlist.json)
*List --> entry:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-designation-use.json](./input/valueset-designation-use.json) ✔
---
### [elementdefinition-11179-DataElement-objectClass.json](./input/elementdefinition-11179-DataElement-objectClass.json)
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### [observation-example-f202-temperature.json](./input/observation-example-f202-temperature.json) ✔
---
### [episodeofcare-example.json](./input/episodeofcare-example.json)
*EpisodeOfCare:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'condition', 'fhir_comments'}
```

---
### [valueset-oral-prosthodontic-material.json](./input/valueset-oral-prosthodontic-material.json) ✔
---
### [valueset-linkage-type.json](./input/valueset-linkage-type.json) ✔
---
### [familymemberhistory-example.json](./input/familymemberhistory-example.json)
*FamilyMemberHistory --> condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetQuantity'}
```

---
### [valueset-procedure-outcome.json](./input/valueset-procedure-outcome.json) ✔
---
### [bundle-questionnaire.json](./input/bundle-questionnaire.json) ✔
---
### [valueset-encounter-state.json](./input/valueset-encounter-state.json) ✔
---
### [enrollmentrequest-questionnaire.json](./input/enrollmentrequest-questionnaire.json) ✔
---
### [valueset-activity-reason.json](./input/valueset-activity-reason.json) ✔
---
### [operation-task-set-output.json](./input/operation-task-set-output.json) ✔
---
### [observation-example-f204-creatinine.json](./input/observation-example-f204-creatinine.json)
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status'}
```

*Observation --> referenceRange:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'meaning'}
```

---
### [patient-example-f001-pieter.json](./input/patient-example-f001-pieter.json) ✔
---
### [valueset-procedure-category.json](./input/valueset-procedure-category.json) ✔
---
### [valueset-selection-behavior.json](./input/valueset-selection-behavior.json) ✔
---
### [observation-example-f002-excess.json](./input/observation-example-f002-excess.json) ✔
---
### [valueset-document-relationship-type.json](./input/valueset-document-relationship-type.json) ✔
---
### [condition-example-f201-fever.json](./input/condition-example-f201-fever.json)
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetDateTime', 'encounter', 'dateRecorded', 'patient'}
```

*Condition --> evidence:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-observation-vitalsignresult.json](./input/valueset-observation-vitalsignresult.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_description'}
```

---
### [valueset-ucum-bodylength.json](./input/valueset-ucum-bodylength.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### [questionnaire-example-f201-lifelines.json](./input/questionnaire-example-f201-lifelines.json)
*Questionnaire:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'concept'}
```

---
### [valueset-claim-exception.json](./input/valueset-claim-exception.json) ✔
---
### [valueset-list-example-codes.json](./input/valueset-list-example-codes.json) ✔
---
### [organization-example-f201-aumc.json](./input/organization-example-f201-aumc.json)
*Organization --> contact:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-immunization-recommendation-date-criterion.json](./input/valueset-immunization-recommendation-date-criterion.json) ✔
---
### [compartmentdefinition-questionnaire.json](./input/compartmentdefinition-questionnaire.json) ✔
---
### [valueset-allergyintolerance-substance-code.json](./input/valueset-allergyintolerance-substance-code.json)
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### [valueset-testscript-profile-origin-types.json](./input/valueset-testscript-profile-origin-types.json) ✔
---
### [valueset-encounter-participant-type.json](./input/valueset-encounter-participant-type.json) ✔
---
### [valueset-dWebType.json](./input/valueset-dWebType.json) ✔
---
### [valueset-measurement-principle.json](./input/valueset-measurement-principle.json) ✔
---
### [valueset-action-selection-behavior.json](./input/valueset-action-selection-behavior.json) ✔
---
### [valueset-questionnaire-questions.json](./input/valueset-questionnaire-questions.json) ✔
---
### [valueset-specimen-collection-priority.json](./input/valueset-specimen-collection-priority.json) ✔
---
### [valueset-contract-signer-type.json](./input/valueset-contract-signer-type.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### [observation-example-f003-co2.json](./input/observation-example-f003-co2.json) ✔
---
### [valueset-c80-practice-codes.json](./input/valueset-c80-practice-codes.json) ✔
---
### [valueset-procedure-reason.json](./input/valueset-procedure-reason.json) ✔
---
### [clinicalimpression-example.json](./input/clinicalimpression-example.json)
*ClinicalImpression:*

**<sub>Keys lost during transform:</sub>**
```python
{'finding'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'plan', 'investigations'}
```

*ClinicalImpression --> finding:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'item'}
```

---
### [imagingstudy-example.json](./input/imagingstudy-example.json)
*ImagingStudy:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'uid', 'patient'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'subject'}
```

---
### [valueset-search-entry-mode.json](./input/valueset-search-entry-mode.json) ✔
---
### [audit-event-example-pixQuery.json](./input/audit-event-example-pixQuery.json)
*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

*AuditEvent --> entity:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'what'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_query'}
```

*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

---
### [valueset-ucum-vitals-common.json](./input/valueset-ucum-vitals-common.json)
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### [location-example.json](./input/location-example.json) ✔
---
### [device-example-f001-feedingtube.json](./input/device-example-f001-feedingtube.json)
*Device:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'udiCarrier'}
```

---
### [valueset-provenance-entity-role.json](./input/valueset-provenance-entity-role.json) ✔
---
### [valueset-icd-10-procedures.json](./input/valueset-icd-10-procedures.json) ✔
---
### [patient-example-a.json](./input/patient-example-a.json) ✔
---
### [testscript-questionnaire.json](./input/testscript-questionnaire.json) ✔
---
### [encounter-example-f003-abscess.json](./input/encounter-example-f003-abscess.json)
*Encounter:*

**<sub>Keys lost during transform:</sub>**
```python
{'class'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reason'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient'}
```

---
### [valueset-condition-outcome.json](./input/valueset-condition-outcome.json) ✔
---
### [supplyrequest-example.json](./input/supplyrequest-example.json)
*SupplyRequest:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### [valueset-compartment-type.json](./input/valueset-compartment-type.json) ✔
---
### [valueset-http-verb.json](./input/valueset-http-verb.json) ✔
---
### [valueset-ex-onsettype.json](./input/valueset-ex-onsettype.json) ✔
---
### [immunization-example-refused.json](./input/immunization-example-refused.json)
*Immunization:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'explanation', 'date'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'wasNotGiven', 'reported'}
```

---
### [valueset-procedure-relationship-type.json](./input/valueset-procedure-relationship-type.json) ✔
---
### [valueset-questionnaire-item-control.json](./input/valueset-questionnaire-item-control.json) ✔
---
### [valueset-benefit-category.json](./input/valueset-benefit-category.json) ✔
---
### [devicemetric-example.json](./input/devicemetric-example.json) ✔
---
### [medicationexample15.json](./input/medicationexample15.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [valueset-guidance-response-status.json](./input/valueset-guidance-response-status.json) ✔
---
### [valueset-c80-facilitycodes.json](./input/valueset-c80-facilitycodes.json) ✔
---
### [operation-patient-match.json](./input/operation-patient-match.json)
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### [valueset-teeth.json](./input/valueset-teeth.json) ✔
---
### [valueset-reaction-event-certainty.json](./input/valueset-reaction-event-certainty.json) ✔
---
### [medicationstatementexample4.json](./input/medicationstatementexample4.json)
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime', 'patient', 'reasonForUseCodeableConcept', 'wasNotTaken'}
```

---
### [patient-example-ihe-pcd.json](./input/patient-example-ihe-pcd.json) ✔
---
### [valueset-assert-operator-codes.json](./input/valueset-assert-operator-codes.json) ✔
---
### [valueset-question-max-occurs.json](./input/valueset-question-max-occurs.json) ✔
---
### [conformance-questionnaire.json](./input/conformance-questionnaire.json) ✔
---
### [questionnaireresponse-example-f201-lifelines.json](./input/questionnaireresponse-example-f201-lifelines.json)
*QuestionnaireResponse --> item:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_linkId'}
```

---
### [valueset-concept-property-type.json](./input/valueset-concept-property-type.json) ✔
---
### [valueset-reaction-event-severity.json](./input/valueset-reaction-event-severity.json) ✔
---
### [valueset-goal-priority.json](./input/valueset-goal-priority.json) ✔
---
### [valueset-resource-types.json](./input/valueset-resource-types.json) ✔
---
### [valueset-udi.json](./input/valueset-udi.json) ✔
---
### [medication-example-f002-crestor.json](./input/medication-example-f002-crestor.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### [valueset-allergy-intolerance-category.json](./input/valueset-allergy-intolerance-category.json) ✔
---
### [valueset-relatedperson-relationshiptype.json](./input/valueset-relatedperson-relationshiptype.json)
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### [valueset-report-codes.json](./input/valueset-report-codes.json) ✔
---
### [valueset-detectedissue-severity.json](./input/valueset-detectedissue-severity.json) ✔
---
### [medication-example-f201-salmeterol.json](./input/medication-example-f201-salmeterol.json)
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'product'}
```

---
### [valueset-consistency-type.json](./input/valueset-consistency-type.json) ✔
---
### [allergyintolerance-fishallergy.json](./input/allergyintolerance-fishallergy.json)
*AllergyIntolerance:*

**<sub>Keys lost during transform:</sub>**
```python
{'category'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'recordedDate', '_recordedDate', '_category', 'substance'}
```

---
### [valueset-network-type.json](./input/valueset-network-type.json) ✔
---
### [device-questionnaire.json](./input/device-questionnaire.json) ✔
---
### [specimen-example-urine.json](./input/specimen-example-urine.json)
*Specimen:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'treatment'}
```

*Specimen --> collection:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'collectedDateTime', 'fhir_comments', '_collectedDateTime'}
```

---
### [valueset-grouping-behavior.json](./input/valueset-grouping-behavior.json) ✔
---
### [valueset-condition-stage.json](./input/valueset-condition-stage.json) ✔
---
### [valueset-procedure-request-status.json](./input/valueset-procedure-request-status.json) ✔
---
### [valueset-extensions-ValueSet-end.json](./input/valueset-extensions-ValueSet-end.json) ✔
---
### [valueset-medication-statement-status.json](./input/valueset-medication-statement-status.json) ✔
---
### [valueset-composition-status.json](./input/valueset-composition-status.json) ✔
---
### [valueset-devicestatus.json](./input/valueset-devicestatus.json) ✔
---
### [observation-example-genetics-1.json](./input/observation-example-genetics-1.json)
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueCodeableConcept'}
```

---
### [valueset-entformula-additive.json](./input/valueset-entformula-additive.json)
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status'}
```

---
### [valueset-benefit-subcategory.json](./input/valueset-benefit-subcategory.json) ✔
---
### [valueset-special-values.json](./input/valueset-special-values.json) ✔
---
### [valueset-diagnostic-service-sections.json](./input/valueset-diagnostic-service-sections.json) ✔
---
### [valueset-food-type.json](./input/valueset-food-type.json) ✔
---
### [procedure-example-biopsy.json](./input/procedure-example-biopsy.json)
*Procedure:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'performedDateTime', 'reasonCodeableConcept', 'notes'}
```

---
### [medicationstatementexample2.json](./input/medicationstatementexample2.json)
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reasonNotTaken'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime', 'patient', 'wasNotTaken'}
```

---
### [relatedperson-example-f001-sarah.json](./input/relatedperson-example-f001-sarah.json) ✔
---
### [valueset-search-param-type.json](./input/valueset-search-param-type.json) ✔
---
### [valueset-enteral-route.json](./input/valueset-enteral-route.json) ✔
---
### [valueset-document-reference-status.json](./input/valueset-document-reference-status.json) ✔
---
### [valueset-vaccination-protocol-dose-target.json](./input/valueset-vaccination-protocol-dose-target.json) ✔
---
### [valueset-referralcategory.json](./input/valueset-referralcategory.json) ✔
---
### [valueset-practitioner-role.json](./input/valueset-practitioner-role.json) ✔
---
### [valueset-diagnostic-requests.json](./input/valueset-diagnostic-requests.json) ✔
---
### [valueset-diet-type.json](./input/valueset-diet-type.json) ✔
---
### [valueset-nutrition-order-status.json](./input/valueset-nutrition-order-status.json) ✔
---
### [valueset-condition-clinical.json](./input/valueset-condition-clinical.json) ✔
---
### [valueset-defined-types.json](./input/valueset-defined-types.json) ✔
---
