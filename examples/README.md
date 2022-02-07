# Comparison of JSON transforms
## Overview
A walk-through of how these results are generated is given in the [directory](../scripts/README.md) of the [script](../script/generate_comparison.py) that generates these results.

## Results
### Summary
|<sub>Total transforms examined:</sub>                 |<sub>788</sub>|
|----------------------------------------|---------------|
|<sub>Number of transforms with issues to review:</sub> |<sub>224</sub>    |
|<sub>Transforms with no issue detected:</sub>|<sub>564</sub>  |
---
### composition-example.json
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
### patient-example-xds.json ✔
---
### valueset-vision-eye-codes.json ✔
---
### slot-example.json ✔
---
### valueset-care-plan-activity-status.json ✔
---
### communication-example.json
*Communication:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

*Communication --> payload:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'contentString', 'contentReference'}
```

---
### binary-f006.json
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
### expansionprofile-questionnaire.json ✔
---
### operation-conceptmap-closure.json ✔
---
### questionnaire-extensions-Questionnaire-deReference.json ✔
---
### observation-genetics-Observation-amino-acid-change.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### valueset-task-performer-type.json ✔
---
### valueset-data-types.json ✔
---
### valueset-c80-doc-classcodes.json ✔
---
### valueset-message-conformance-event-mode.json ✔
---
### valueset-flag-category.json ✔
---
### valueset-appointmentstatus.json ✔
---
### valueset-map-context-type.json ✔
---
### valueset-name-use.json ✔
---
### valueset-actionlist.json ✔
---
### valueset-module-metadata-type.json ✔
---
### valueset-measure-type.json ✔
---
### valueset-process-priority.json ✔
---
### valueset-template-status-code.json ✔
---
### medicationexample13.json
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
### valueset-LOINC-48019-4-answerlist.json ✔
---
### medicationstatementexample1.json
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime',
 'medicationReference',
 'patient',
 'reasonForUseCodeableConcept',
 'wasNotTaken'}
```

---
### valueset-module-metadata-focus-type.json ✔
---
### valueset-immunization-route.json ✔
---
### valueset-claim-modifiers.json ✔
---
### organization-example-insurer.json ✔
---
### medicationexample1.json ✔
---
### linkage-example.json ✔
---
### condition-example-f205-infection.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'dateRecorded'}
```

---
### valueset-participantrequired.json ✔
---
### valueset-manifestation-codes.json ✔
---
### valueset-map-transform.json ✔
---
### condition-example-f204-renal.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'abatementDateTime', 'patient', 'dateRecorded', 'encounter', 'onsetDateTime'}
```

*Condition --> stage:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-search-modifier-code.json ✔
---
### relatedperson-example-f002-ariadne.json ✔
---
### valueset-allergy-intolerance-status.json ✔
---
### valueset-order-set-item-type.json ✔
---
### observation-example-sample-data.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

*Observation --> component:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments', 'valueSampledData'}
```

---
### valueset-organization-type.json ✔
---
### operation-task-release.json ✔
---
### valueset-condition-ver-status.json ✔
---
### valueset-units-of-time.json ✔
---
### valueset-testscript-operation-codes.json ✔
---
### valueset-goal-category.json ✔
---
### practitioner-example-f204-ce.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### condition-example.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'onsetDateTime'}
```

---
### valueset-subscription-channel-type.json ✔
---
### valueset-binding-strength.json ✔
---
### valueset-basic-resource-type.json ✔
---
### valueset-care-plan-activity-category.json ✔
---
### valueset-specimen-collection-method.json ✔
---
### organization-example-f203-bumc.json
*Organization:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_active'}
```

---
### visionprescription-example-1.json
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
### device-extensions-Device-din.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### valueset-LOINC-53037-8-answerlist.json ✔
---
### medicationexample4.json
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
### valueset-procedure-request-priority.json ✔
---
### valueset-specimen-container-type.json ✔
---
### familymemberhistory-example-mother.json
*FamilyMemberHistory --> condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetQuantity'}
```

---
### valueset-device-kind.json ✔
---
### valueset-provenance-agent-role.json
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### us-core-Patient-ethnicity.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### valueset-payment-type.json ✔
---
### practitioner-example-xcda-author.json ✔
---
### valueset-condition-code.json ✔
---
### valueset-device-action.json ✔
---
### operation-task-resume.json ✔
---
### valueset-condition-state.json ✔
---
### valueset-security-labels.json
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
### valueset-extensions-ValueSet-effective.json ✔
---
### valueset-list-order.json ✔
---
### valueset-procedure-not-performed-reason.json ✔
---
### operation-patient-everything.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### organization-example-f003-burgers-ENT.json ✔
---
### detectedissue-example-dup.json
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
### valueset-bundle-type.json ✔
---
### group-example-member.json ✔
---
### episodeofcare-questionnaire.json ✔
---
### valueset-encounter-special-courtesy.json ✔
---
### valueset-cds-rule-action-type.json ✔
---
### namingsystem-example-replaced.json
*NamingSystem:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'replacedBy'}
```

---
### valueset-investigation-sets.json ✔
---
### valueset-observation-methods.json ✔
---
### audit-event-example-media.json
*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
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

---
### valueset-parent-relationship-codes.json ✔
---
### valueset-map-input-mode.json ✔
---
### element.profile.json ✔
---
### condition-example2.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'onsetDateTime'}
```

---
### operation-task-reserve.json ✔
---
### valueset-message-significance-category.json ✔
---
### detectedissue-example-allergy.json
*DetectedIssue:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### substance-example-f201-dust.json ✔
---
### observation-example-f005-hemoglobin.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectivePeriod', 'valueQuantity'}
```

---
### valueset-specimen-status.json ✔
---
### operationoutcome-example-exception.json ✔
---
### valueset-supplyrequest-reason.json ✔
---
### namingsystem-example-id.json
*NamingSystem:*

**<sub>Keys lost during transform:</sub>**
```python
{'useContext'}
```

---
### valueset-allergy-intolerance-criticality.json ✔
---
### valueset-choice-list-orientation.json ✔
---
### valueset-copy-number-event.json ✔
---
### valueset-link-type.json ✔
---
### slot-example-unavailable.json ✔
---
### valueset-postal-address-use.json ✔
---
### valueset-fm-conditions.json ✔
---
### valueset-days-of-week.json ✔
---
### valueset-codesystem-content-mode.json ✔
---
### valueset-age-units.json ✔
---
### valueset-questionnaire-display-category.json ✔
---
### valueset-relationship.json ✔
---
### operation-task-set-input.json ✔
---
### encounter-example-xcda.json
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
### valueset-encounter-special-arrangements.json ✔
---
### valueset-conditional-delete-status.json ✔
---
### flag-example.json ✔
---
### valueset-name-v3-representation.json ✔
---
### valueset-contract-actorrole.json ✔
---
### valueset-observation-category.json ✔
---
### operation-task-suspend.json ✔
---
### valueset-order-set-participant.json ✔
---
### substance-example-f202-staphylococcus.json ✔
---
### valueset-goal-status.json ✔
---
### person-example.json
*Person:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_gender'}
```

---
### valueset-service-type.json ✔
---
### valueset-timing-abbreviation.json ✔
---
### valueset-profile-code.json ✔
---
### practitioner-example-f006-rvdb.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### valueset-instance-availability.json ✔
---
### observation-example-bloodpressure-cancel.json
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
### valueset-questionnaire-status.json ✔
---
### organization-example-gastro.json ✔
---
### valueset-ucum-common.json
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### operation-conceptmap-translate.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### valueset-cardinality-behavior.json ✔
---
### condition-example-f202-malignancy.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetQuantity', 'patient', '_dateRecorded', 'dateRecorded'}
```

*Condition --> evidence:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-guide-page-kind.json ✔
---
### valueset-manifestation-or-symptom.json ✔
---
### valueset-observation-relationshiptypes.json ✔
---
### valueset-identity-assuranceLevel.json ✔
---
### valueset-history-status.json ✔
---
### valueset-action-required-behavior.json ✔
---
### valueset-structure-definition-kind.json ✔
---
### valueset-audit-event-action.json ✔
---
### riskassessment-example.json
*RiskAssessment:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'date'}
```

*RiskAssessment --> prediction:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'probabilityDecimal', 'whenRange'}
```

---
### organization-example-f001-burgers.json ✔
---
### valueset-service-provision-conditions.json ✔
---
### valueset-specimen-treatment-procedure.json ✔
---
### valueset-supplyrequest-kind.json ✔
---
### valueset-cds-rule-participant.json ✔
---
### observation-example-unsat.json
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
{'effectivePeriod'}
```

---
### valueset-service-product.json ✔
---
### valueset-benefit-term.json ✔
---
### valueset-address-use.json ✔
---
### encounter-example-f201-20130404.json
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
### valueset-episode-of-care-status.json ✔
---
### valueset-goal-start-event.json ✔
---
### slot-questionnaire.json ✔
---
### structuremap-example.json ✔
---
### valueset-dataelement-stringency.json ✔
---
### valueset-resource-slicing-rules.json ✔
---
### encounter-example-f002-lung.json
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
### valueset-unknown-content-code.json ✔
---
### subscription-questionnaire.json ✔
---
### valueset-immunization-recommendation-status.json ✔
---
### valueset-HGNC-geneIdentifiers.json ✔
---
### valueset-concept-map-equivalence.json ✔
---
### riskassessment-example-population.json ✔
---
### valueset-payeetype.json ✔
---
### list-example.json ✔
---
### patient-glossy-example.json
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'careProvider'}
```

---
### valueset-remittance-outcome.json ✔
---
### operation-composition-document.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### condition-example-f003-abscess.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'dateRecorded', 'encounter', 'onsetDateTime'}
```

*Condition --> evidence:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-operation-kind.json ✔
---
### valueset-measure-data-usage.json ✔
---
### valueset-metric-calibration-state.json ✔
---
### valueset-route-codes.json ✔
---
### valueset-assert-direction-codes.json ✔
---
### valueset-ucum-bodytemp.json
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### valueset-adjudication-error.json ✔
---
### valueset-flag-status.json ✔
---
### measurereport-questionnaire.json ✔
---
### valueset-anzsco-occupations.json
*ValueSet:*

**<sub>Keys lost during transform:</sub>**
```python
{'useContext'}
```

---
### practitioner-example-f005-al.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### valueset-adjudication-reason.json ✔
---
### valueset-audit-event-type.json ✔
---
### library-exclusive-breastfeeding-cds-logic.json
*Library:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'model', 'valueSet', 'document', 'moduleMetadata'}
```

---
### appointment-example-request.json
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
### operation-messageheader-process-message.json ✔
---
### patient-example-proband.json
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'deceasedBoolean'}
```

---
### patient-extensions-Patient-mothersMaidenName.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### observation-example-f004-erythrocyte.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectivePeriod', 'valueQuantity'}
```

---
### valueset-sequence-species.json ✔
---
### valueset-goal-status-reason.json ✔
---
### practitioner-example-f002-pv.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### observation-genetics-Observation-dna-variant.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### substance-questionnaire.json ✔
---
### valueset-contract-action.json ✔
---
### valueset-patient-contact-relationship.json ✔
---
### patient-example-us-extensions.json ✔
---
### observation-example-f206-staphylococcus.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueCodeableConcept', 'fhir_comments'}
```

---
### valueset-LOINC-53034-5-answerlist.json ✔
---
### valueset-patient-mpi-match.json ✔
---
### operation-task-fail.json ✔
---
### valueset-address-type.json ✔
---
### valueset-object-role.json ✔
---
### valueset-issue-type.json ✔
---
### valueset-flag-priority.json ✔
---
### binary-questionnaire.json ✔
---
### location-extensions-Location-alias.json ✔
---
### valueset-module-metadata-resource-type.json ✔
---
### list-example-allergies.json ✔
---
### valueset-quantity-comparator.json ✔
---
### valueset-namingsystem-type.json ✔
---
### valueset-LOINC-48002-0-answerlist.json ✔
---
### valueset-dicom-cid29.json
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
### encounter-example-f203-20130311.json
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
### valueset-media-view.json ✔
---
### valueset-encounter-admit-source.json ✔
---
### valueset-event-timing.json ✔
---
### valueset-benefit-type.json ✔
---
### namingsystem-questionnaire.json ✔
---
### condition-example-f203-sepsis.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'dateRecorded', 'encounter', 'onsetDateTime'}
```

---
### appointmentresponse-example.json ✔
---
### valueset-operation-parameter-use.json ✔
---
### valueset-observation-valueabsentreason.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

---
### valueset-account-status.json ✔
---
### valueset-care-plan-relationship.json ✔
---
### valueset-detectedissue-category.json ✔
---
### valueset-note-type.json ✔
---
### condition-example-f002-lung.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'dateRecorded', 'encounter', 'onsetDateTime'}
```

---
### valueset-benefit-unit.json ✔
---
### practitioner-example-f007-sh.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### device-example-ihe-pcd.json
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
### valueset-metric-category.json ✔
---
### valueset-order-status.json ✔
---
### valueset-c80-doc-typecodes.json ✔
---
### relatedperson-example.json ✔
---
### valueset-example.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_name', '_lockedDate', '_url', 'lockedDate', '_version'}
```

---
### valueset-performer-role.json ✔
---
### valueset-device-use-request-status.json ✔
---
### valueset-action-grouping-behavior.json ✔
---
### valueset-payment-adjustment-reason.json ✔
---
### patient-example-dicom.json
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
### valueset-clinical-findings.json ✔
---
### structuredefinition-questionnaire.json ✔
---
### valueset-supplement-type.json ✔
---
### valueset-procedure-status.json ✔
---
### operation-resource-validate.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### valueset-medication-codes.json ✔
---
### valueset-testscript-profile-destination-types.json ✔
---
### valueset-ex-program-code.json ✔
---
### valueset-action-type.json ✔
---
### medicationexample3.json
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
### valueset-xds-relationship-type.json ✔
---
### diagnosticreport-example-f201-brainct.json
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
{'reference', 'display'}
```

---
### patient-example-d.json
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'deceasedBoolean'}
```

---
### parameters-example.json
*Parameters --> parameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'resource'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueDate'}
```

---
### codesystem-extensions-CodeSystem-author.json ✔
---
### valueset-cds-rule-trigger-type.json ✔
---
### valueset-type-restful-interaction.json ✔
---
### patient-example.json
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_birthDate', 'deceasedBoolean', '_gender'}
```

---
### valueset-care-plan-status.json ✔
---
### valueset-audit-event-outcome.json ✔
---
### valueset-list-mode.json ✔
---
### valueset-metric-calibration-type.json ✔
---
### observation-example-f203-bicarbonate.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status', 'valueQuantity'}
```

*Observation --> referenceRange:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'meaning'}
```

---
### medication-example-f001-combivent.json
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
### supplydelivery-example.json
*SupplyDelivery:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-service-modifiers.json ✔
---
### media-example-dicom.json
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
### valueset-action-relationship-anchor.json ✔
---
### medicationstatementexample6.json
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'medicationReference', 'effectiveDateTime', 'patient', 'wasNotTaken'}
```

---
### patient-example-b.json
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_gender'}
```

---
### valueset-kos-title.json ✔
---
### location-example-ukpharmacy.json ✔
---
### valueset-encounter-location-status.json ✔
---
### medicationexample16.json
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
### auditevent-example-disclosure.json
*AuditEvent:*

**<sub>Keys lost during transform:</sub>**
```python
{'purposeOfEvent'}
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

*AuditEvent --> entity:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier', 'reference'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'what'}
```

*AuditEvent --> agent:*

**<sub>Keys lost during transform:</sub>**
```python
{'purposeOfUse'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'reference', 'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

---
### observation-genetics-Observation-gene-dnavariant.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### compartmentdefinition-device.json ✔
---
### valueset-map-list-mode.json ✔
---
### valueset-chromosome-human.json ✔
---
### valueset-ucum-bodyweight.json
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### valueset-claim-type-link.json ✔
---
### valueset-identifier-type.json ✔
---
### valueset-reference-version-rules.json ✔
---
### valueset-item-type.json ✔
---
### valueset-extension-context.json ✔
---
### valueset-contract-term-type.json ✔
---
### medicationexample11.json
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
### schedule-example.json ✔
---
### valueset-approach-site-codes.json ✔
---
### valueset-object-lifecycle.json ✔
---
### valueset-vaccination-protocol-dose-status.json ✔
---
### valueset-medication-admin-status.json ✔
---
### valueset-conformance-statement-kind.json ✔
---
### valueset-doc-typecodes.json ✔
---
### valueset-digital-media-subtype.json
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### valueset-payment-status.json ✔
---
### valueset-transaction-mode.json ✔
---
### valueset-medication-order-status.json ✔
---
### practitionerrole-questionnaire.json ✔
---
### substance-example.json ✔
---
### valueset-location-mode.json ✔
---
### codesystem-extensions-CodeSystem-workflow.json ✔
---
### devicemetric-questionnaire.json ✔
---
### valueset-match-grade.json ✔
---
### immunization-example.json
*Immunization:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'date', 'explanation', 'vaccinationProtocol'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'reasonCode', 'protocolApplied'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'performer', 'reported', 'wasNotGiven', 'requester'}
```

---
### valueset-process-outcome.json ✔
---
### practitioner-example-f203-jvg.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_birthDate', 'practitionerRole'}
```

---
### communicationrequest-example.json ✔
---
### codesystem-extensions-CodeSystem-keyword.json ✔
---
### operation-structuredefinition-questionnaire.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### valueset-immunization-site.json ✔
---
### appointmentresponse-example-req.json ✔
---
### valueset-assert-response-code-types.json ✔
---
### practitioner-example-f202-lm.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_birthDate', 'practitionerRole'}
```

---
### valueset-doc-section-codes.json ✔
---
### medication-example-f005-enalapril.json
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### valueset-contact-point-use.json ✔
---
### person-example-f002-ariadne.json ✔
---
### valueset-condition-severity.json ✔
---
### operation-resource-meta-delete.json ✔
---
### observation-example-genetics-2.json
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
### enrollmentresponse-questionnaire.json ✔
---
### valueset-medication-package-form-codes.json ✔
---
### medicationexample8.json
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
### valueset-usps-state.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

---
### valueset-vaccination-protocol-dose-status-reason.json ✔
---
### imagingstudy-questionnaire.json ✔
---
### valueset-slotstatus.json ✔
---
### valueset-vision-base-codes.json ✔
---
### valueset-message-reason-encounter.json ✔
---
### patient-example-c.json
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'deceasedDateTime'}
```

---
### valueset-restful-security-service.json ✔
---
### deviceusestatement-example.json ✔
---
### organization-example.json ✔
---
### valueset-medication-dispense-status.json ✔
---
### valueset-referencerange-meaning.json
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### medicationadministrationexample3.json
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
{'medicationReference', 'patient', 'effectiveTimePeriod', 'practitioner'}
```

*MedicationAdministration --> dosage:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'quantity', 'rateRatio'}
```

---
### valueset-measure-report-status.json ✔
---
### account-example.json
*Account:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### enrollmentrequest-example.json
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
### healthcareservice-questionnaire.json ✔
---
### person-grahame.json
*Person:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_gender'}
```

---
### compartmentdefinition-encounter.json ✔
---
### medicationadministrationexample2.json
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
{'medicationReference', 'patient', 'effectiveTimePeriod', 'practitioner'}
```

*MedicationAdministration --> dosage:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'quantity', 'rateRatio'}
```

---
### auditevent-example.json
*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
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

*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

---
### operation-task-stop.json ✔
---
### operationoutcome-example-searchfail.json ✔
---
### practitioner-example-f003-mv.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### flag-example-encounter.json ✔
---
### valueset-bodysite-laterality.json ✔
---
### bodysite-questionnaire.json ✔
---
### valueset-ruleset.json ✔
---
### observation-genetics-Observation-gene-amino-acid-change.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### valueset-content-type.json ✔
---
### immunization-questionnaire.json ✔
---
### observation-example-f205-egfr.json
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
{'fhir_comments', 'valueQuantity'}
```

---
### valueset-identifier-use.json ✔
---
### valueset-modified-foodtype.json ✔
---
### valueset-type-derivation-rule.json ✔
---
### valueset-provider-qualification.json ✔
---
### observation-example-genetics-5.json
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
### medicationstatementexample7.json
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'medicationReference', 'effectiveDateTime', 'patient', 'wasNotTaken'}
```

---
### procedure-example.json
*Procedure:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'notes', 'performedDateTime', 'reasonCodeableConcept'}
```

---
### codesystem-extensions-CodeSystem-end.json ✔
---
### valueset-contact-point-system.json ✔
---
### valueset-abstract-types.json ✔
---
### valueset-claim-use-link.json ✔
---
### valueset-location-physical-type.json ✔
---
### medicationexample5.json
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### substance-example-f203-potassium.json ✔
---
### valueset-provenance-agent-type.json ✔
---
### valueset-diagnostic-order-priority.json ✔
---
### valueset-referralstatus.json ✔
---
### valueset-action-relationship-type.json ✔
---
### location-example-patients-home.json ✔
---
### valueset-filter-operator.json ✔
---
### valueset-occurrence-codes.json ✔
---
### valueset-group-type.json ✔
---
### valueset-search-xpath-usage.json ✔
---
### valueset-observation-codes.json ✔
---
### valueset-measure-population.json ✔
---
### contract-example.json
*Contract:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### slot-example-busy.json ✔
---
### valueset-extensions-ValueSet-workflow.json ✔
---
### valueset-data-absent-reason.json ✔
---
### valueset-audit-event-sub-type.json ✔
---
### valueset-metric-color.json ✔
---
### valueset-action-participant-type.json ✔
---
### valueset-texture-code.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_description'}
```

---
### valueset-no-immunization-reason.json ✔
---
### operation-resource-meta.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### codesystem-extensions-CodeSystem-effective.json ✔
---
### organization-example-good-health-care.json ✔
---
### riskassessment-example-prognosis.json
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
### valueset-measure-report-type.json ✔
---
### media-example.json
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
### valueset-procedure-progress-status-codes.json ✔
---
### valueset-goal-acceptance-status.json ✔
---
### valueset-task-priority.json ✔
---
### audit-event-example-vread.json
*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
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

*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

---
### library-exclusive-breastfeeding-cqm-logic.json
*Library:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'model', 'valueSet', 'document', 'moduleMetadata'}
```

---
### valueset-activity-definition-category.json ✔
---
### valueset-system-restful-interaction.json ✔
---
### observation-example.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime', 'valueQuantity', 'encounter'}
```

---
### condition-example-f001-heart.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'dateRecorded', 'encounter', 'onsetDateTime'}
```

---
### valueset-dataelement-sdcobjectclassproperty.json ✔
---
### observation-example-genetics-4.json
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
### valueset-service-place.json ✔
---
### practitioner-example-f001-evdb.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### valueset-diagnostic-order-status.json ✔
---
### practitionerrole-example.json
*PractitionerRole:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'role'}
```

---
### valueset-procedure-code.json ✔
---
### valueset-detectedissue-mitigation-action.json ✔
---
### medication-example-f003-tolbutamide.json
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### valueset-condition-category.json ✔
---
### valueset-immunization-reason.json ✔
---
### us-core-Patient-race.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### library-example.json
*Library:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'model', 'valueSet', 'document', 'moduleMetadata'}
```

---
### valueset-HGVSvariant.json ✔
---
### valueset-map-model-mode.json ✔
---
### compartmentdefinition-relatedperson.json ✔
---
### valueset-ldlcholesterol-codes.json ✔
---
### medicationstatementexample5.json
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime',
 'medicationReference',
 'patient',
 'reasonForUseCodeableConcept',
 'wasNotTaken'}
```

---
### slot-example-tentative.json ✔
---
### valueset-communication-status.json ✔
---
### valueset-encounter-discharge-disposition.json ✔
---
### valueset-supplyrequest-when.json ✔
---
### valueset-extensions-ValueSet-author.json ✔
---
### valueset-conformance-resource-status.json ✔
---
### valueset-classification-or-context.json ✔
---
### diagnosticreport-hla-genetics-results-example.json
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
{'reference', 'display'}
```

---
### medicationexample14.json
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
### substance-example-silver-nitrate-product.json ✔
---
### valueset-operation-outcome.json ✔
---
### consensus-sequence-block-questionnaire.json ✔
---
### valueset-service-uscls.json ✔
---
### valueset-adjudication.json ✔
---
### valueset-subscription-status.json ✔
---
### valueset-participant-role.json ✔
---
### valueset-animal-species.json ✔
---
### valueset-flag-code.json ✔
---
### operationoutcome-questionnaire.json ✔
---
### valueset-supplyrequest-status.json ✔
---
### valueset-subscription-tag.json ✔
---
### media-example-sound.json ✔
---
### valueset-animal-breeds.json ✔
---
### valueset-dicm-402-roleid.json ✔
---
### operation-resource-meta-add.json ✔
---
### operation-task-start.json ✔
---
### valueset-versioning-policy.json ✔
---
### valueset-observation-interpretation.json ✔
---
### operation-list-find.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### valueset-questionnaire-answers.json ✔
---
### valueset-supplydelivery-status.json ✔
---
### valueset-resource-aggregation-mode.json ✔
---
### organization-questionnaire.json ✔
---
### patient-example-animal.json
*Patient:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'animal'}
```

---
### valueset-action-behavior-type.json ✔
---
### searchparameter-example-extension.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### basic-example-narrative.json ✔
---
### searchparameter-example.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_requirements', 'requirements'}
```

---
### medicationexample2.json
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
### encounter-example-f001-heart.json
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
### valueset-communication-request-status.json ✔
---
### device-example-software.json ✔
---
### coverage-example-2.json
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
### valueset-action-cardinality-behavior.json ✔
---
### valueset-surface.json ✔
---
### allergyintolerance-medication.json
*AllergyIntolerance:*

**<sub>Keys lost during transform:</sub>**
```python
{'category'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'status', '_recordedDate', 'recordedDate', 'substance'}
```

---
### valueset-message-transport.json ✔
---
### observation-example-glasgow-qa.json
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
{'effectiveDateTime', 'valueQuantity'}
```

*Observation --> referenceRange:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'meaning'}
```

---
### valueset-marital-status.json ✔
---
### location-questionnaire.json ✔
---
### valueset-digital-media-type.json ✔
---
### valueset-response-code.json ✔
---
### operation-valueset-expand.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### valueset-claim-subtype.json ✔
---
### encounter-example.json
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
### valueset-resource-validation-mode.json ✔
---
### operation-task-cancel.json ✔
---
### valueset-use-context.json
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### valueset-service-category.json ✔
---
### valueset-list-status.json ✔
---
### organization-example-f002-burgers-card.json ✔
---
### valueset-fm-itemtype.json ✔
---
### valueset-composition-attestation-mode.json ✔
---
### valueset-audit-source-type.json ✔
---
### coverage-example.json
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
### patient-mpi-search.json
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
### person-provider-directory.json ✔
---
### paymentnotice-example.json
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
### valueset-protocol-type.json ✔
---
### valueset-goal-relationship-type.json ✔
---
### valueset-substance-code.json ✔
---
### valueset-signature-type.json ✔
---
### valueset-example-intensional.json
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
### enrollmentresponse-example.json
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
### valueset-trigger-type.json ✔
---
### operation-task-finish.json ✔
---
### medication-example-f202-flucloxacilline.json
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
### group-example.json
*Group --> characteristic:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueCodeableConcept'}
```

---
### appointment-example.json ✔
---
### observation-example-f001-glucose.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectivePeriod', 'valueQuantity'}
```

---
### valueset-intervention.json ✔
---
### valueset-diagnostic-report-status.json ✔
---
### elementdefinition-11179-DataElement-objectClassProperty.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### valueset-diagnostic-order-event.json ✔
---
### operation-valueset-validate-code.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### relatedperson-questionnaire.json ✔
---
### operation-resource-cds-hook.json ✔
---
### detectedissue-example.json
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
### valueset-example-yesnodontknow.json
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### practitioner-questionnaire.json ✔
---
### valueset-contract-subtype.json ✔
---
### relatedperson-example-peter.json ✔
---
### audit-event-example-search.json
*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

---
### compartmentdefinition-practitioner.json ✔
---
### medicationexample7.json
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
### valueset-formatcodes.json ✔
---
### dataelement-questionnaire.json ✔
---
### observation-example-bloodpressure.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime'}
```

*Observation --> component:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments', 'valueQuantity'}
```

---
### valueset-example-expansion.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

*ValueSet --> expansion:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_total', '_timestamp', '_identifier', '_offset', 'fhir_comments'}
```

*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-vision-product.json ✔
---
### valueset-encounter-reason.json ✔
---
### valueset-supplydelivery-type.json ✔
---
### encounter-example-f202-20130128.json
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
{'patient', 'indication', '_class'}
```

---
### visionprescription-example.json
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
### valueset-message-events.json ✔
---
### patient-example-xcda.json ✔
---
### valueset-property-representation.json ✔
---
### valueset-questionnaire-category.json ✔
---
### valueset-condition-predecessor.json ✔
---
### device-example-udi1.json
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
### valueset-probability-distribution-type.json ✔
---
### valueset-contract-type.json ✔
---
### detectedissue-example-lab.json
*DetectedIssue:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### patient-extensions-Patient-age.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### valueset-observation-status.json ✔
---
### valueset-care-plan-activity.json ✔
---
### valueset-benefit-network.json ✔
---
### procedure-example-implant.json
*Procedure:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'notes', 'performedDateTime', 'reasonCodeableConcept'}
```

---
### valueset-procedure-followup.json ✔
---
### valueset-participationstatus.json ✔
---
### medicationadministrationexample1.json
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
{'medicationReference', 'patient', 'effectiveTimePeriod', 'practitioner'}
```

*MedicationAdministration --> dosage:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'quantity'}
```

---
### condition-example-stroke.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'onsetDateTime'}
```

---
### valueset-condition-cause.json ✔
---
### medication-example-f203-paracetamol.json
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
### devicecomponent-questionnaire.json ✔
---
### organization-example-lab.json ✔
---
### valueset-medication-form-codes.json ✔
---
### sequence-questionnaire.json ✔
---
### valueset-name-part-qualifier.json ✔
---
### valueset-encounter-class.json ✔
---
### patient-example-f201-roel.json
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'deceasedBoolean', '_deceasedBoolean', '_active', 'multipleBirthBoolean'}
```

---
### codesystem-example.json
*CodeSystem:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_caseSensitive', '_url', '_version'}
```

*CodeSystem --> concept:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-device-use-request-priority.json ✔
---
### practitioner-example.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### valueset-task-status.json ✔
---
### basic-example.json ✔
---
### valueset-risk-probability.json ✔
---
### observation-genetics-Observation-gene-identifier.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### valueset-conformance-expectation.json ✔
---
### valueset-constraint-severity.json ✔
---
### immunizationrecommendation-example.json
*ImmunizationRecommendation:*

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'date', 'authority'}
```

*ImmunizationRecommendation --> recommendation:*

**<sub>Keys lost during transform:</sub>**
```python
{'doseNumber'}
```

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'date', 'protocol'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'description', 'series'}
```

---
### valueset-occurrence-span-codes.json ✔
---
### valueset-action-precheck-behavior.json ✔
---
### operationoutcome-example.json ✔
---
### valueset-all-types.json ✔
---
### riskassessment-example-cardiac.json
*RiskAssessment:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'date'}
```

*RiskAssessment --> prediction:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'probabilityDecimal', 'whenRange'}
```

---
### valueset-nutrient-code.json ✔
---
### valueset-additionalmaterials.json
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### valueset-doc-classcodes.json ✔
---
### operation-encounter-everything.json ✔
---
### valueset-object-type.json ✔
---
### valueset-body-site.json ✔
---
### compartmentdefinition-patient.json ✔
---
### observation-example-genetics-3.json
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
### valueset-focal-subject.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

---
### valueset-coverage-exception.json ✔
---
### valueset-protocol-status.json ✔
---
### valueset-vaccine-code.json ✔
---
### medicationexample6.json
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
### valueset-module-metadata-status.json ✔
---
### location-example-hl7hq.json
*Location:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status'}
```

---
### medicationexample17.json
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
### observation-example-satO2.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime', 'valueQuantity'}
```

---
### valueset-dataelement-sdcobjectclass.json ✔
---
### valueset-sequence-variationID.json ✔
---
### person-patient-portal.json ✔
---
### valueset-reason-medication-not-given-codes.json ✔
---
### list-example-empty.json ✔
---
### valueset-extensions-ValueSet-keyword.json ✔
---
### operationoutcome-example-allok.json ✔
---
### medicationexample12.json
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'isBrand'}
```

---
### valueset-contactentity-type.json ✔
---
### valueset-module-metadata-contributor.json ✔
---
### valueset-value-codes.json ✔
---
### valueset-issue-severity.json ✔
---
### valueset-precheck-behavior.json ✔
---
### diagnosticreport-example-ultrasound.json
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
### audit-event-example-login.json
*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

---
### valueset-practitioner-specialty.json ✔
---
### valueset-location-status.json ✔
---
### valueset-missing-tooth-reason.json ✔
---
### valueset-dicm-405-mediatype.json ✔
---
### appointment-example2doctors.json ✔
---
### location-example-ambulance.json ✔
---
### operation-codesystem-lookup.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### valueset-fips-county.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_publisher'}
```

---
### practitioner-example-f201-ab.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### valueset-administrative-gender.json ✔
---
### valueset-clinical-impression-status.json ✔
---
### binary-example.json
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
### valueset-encounter-type.json ✔
---
### valueset-guide-dependency-type.json ✔
---
### valueset-list-empty-reason.json ✔
---
### practitioner-example-xcda1.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### practitioner-example-f004-rb.json
*Practitioner:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'practitionerRole'}
```

---
### valueset-icd-10.json ✔
---
### valueset-sequence-referenceSeq.json ✔
---
### valueset-cpt-all.json ✔
---
### valueset-contract-term-subtype.json ✔
---
### valueset-questionnaire-answers-status.json ✔
---
### valueset-encounter-priority.json ✔
---
### operationoutcome-example-validationfail.json ✔
---
### medication-example-f004-metoprolol.json
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### basic-example2.json ✔
---
### valueset-namingsystem-identifier-type.json ✔
---
### valueset-document-mode.json ✔
---
### valueset-care-plan-category.json ✔
---
### valueset-restful-conformance-mode.json ✔
---
### allergyintolerance-example.json
*AllergyIntolerance:*

**<sub>Keys lost during transform:</sub>**
```python
{'category', 'onset'}
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
### valueset-service-pharmacy.json ✔
---
### valueset-reason-medication-given-codes.json ✔
---
### valueset-tooth.json ✔
---
### searchparameter-questionnaire.json ✔
---
### valueset-fundsreserve.json ✔
---
### valueset-encounter-diet.json ✔
---
### valueset-forms.json ✔
---
### valueset-allergy-intolerance-type.json ✔
---
### valueset-service-referral-method.json ✔
---
### valueset-metric-operational-status.json ✔
---
### patient-extensions-Patient-birthOrderBoolean.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### valueset-list-item-flag.json ✔
---
### valueset-sequence-type.json ✔
---
### valueset-measure-scoring.json ✔
---
### valueset-required-behavior.json ✔
---
### audit-event-example-logout.json
*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
```

*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

---
### location-example-room.json ✔
---
### goal-example.json
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
{'lifecycleStatus', 'achievementStatus'}
```

---
### task-example.json
*Task:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'created', 'subject', 'creator', 'type'}
```

---
### valueset-variant-state.json ✔
---
### diagnosticreport-genetics-DiagnosticReport-assessed-condition.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### device-example-pacemaker.json
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
### valueset-related-claim-relationship.json ✔
---
### valueset-substance-category.json ✔
---
### valueset-entformula-type.json ✔
---
### namingsystem-example.json ✔
---
### organization-extensions-Organization-alias.json ✔
---
### valueset-bodysite-relative-location.json ✔
---
### valueset-narrative-status.json ✔
---
### valueset-animal-genderstatus.json ✔
---
### list-example-medlist.json
*List --> entry:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-designation-use.json ✔
---
### elementdefinition-11179-DataElement-objectClass.json
*SearchParameter:*

**<sub>Keys lost during transform:</sub>**
```python
{'base'}
```

---
### observation-example-f202-temperature.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueQuantity'}
```

---
### episodeofcare-example.json
*EpisodeOfCare:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'condition', 'fhir_comments'}
```

---
### valueset-oral-prosthodontic-material.json ✔
---
### valueset-linkage-type.json ✔
---
### familymemberhistory-example.json
*FamilyMemberHistory --> condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'onsetQuantity'}
```

---
### valueset-procedure-outcome.json ✔
---
### bundle-questionnaire.json ✔
---
### valueset-encounter-state.json ✔
---
### enrollmentrequest-questionnaire.json ✔
---
### valueset-activity-reason.json ✔
---
### operation-task-set-output.json ✔
---
### observation-example-f204-creatinine.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status', 'valueQuantity'}
```

*Observation --> referenceRange:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'meaning'}
```

---
### patient-example-f001-pieter.json
*Patient:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'deceasedBoolean', 'multipleBirthBoolean'}
```

---
### valueset-procedure-category.json ✔
---
### valueset-selection-behavior.json ✔
---
### observation-example-f002-excess.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectivePeriod', 'valueQuantity'}
```

---
### valueset-document-relationship-type.json ✔
---
### condition-example-f201-fever.json
*Condition:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'patient', 'dateRecorded', 'encounter', 'onsetDateTime'}
```

*Condition --> evidence:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-observation-vitalsignresult.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_description'}
```

---
### valueset-ucum-bodylength.json
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### questionnaire-example-f201-lifelines.json
*Questionnaire:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'concept'}
```

---
### valueset-claim-exception.json ✔
---
### valueset-list-example-codes.json ✔
---
### organization-example-f201-aumc.json
*Organization --> contact:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-immunization-recommendation-date-criterion.json ✔
---
### compartmentdefinition-questionnaire.json ✔
---
### valueset-allergyintolerance-substance-code.json
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### valueset-testscript-profile-origin-types.json ✔
---
### valueset-encounter-participant-type.json ✔
---
### valueset-dWebType.json ✔
---
### valueset-measurement-principle.json ✔
---
### valueset-action-selection-behavior.json ✔
---
### valueset-questionnaire-questions.json ✔
---
### valueset-specimen-collection-priority.json ✔
---
### valueset-contract-signer-type.json
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### observation-example-f003-co2.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectivePeriod', 'valueQuantity'}
```

---
### valueset-c80-practice-codes.json ✔
---
### valueset-procedure-reason.json ✔
---
### clinicalimpression-example.json
*ClinicalImpression:*

**<sub>Keys lost during transform:</sub>**
```python
{'finding'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'investigations', 'patient', 'plan'}
```

*ClinicalImpression --> finding:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'item'}
```

---
### imagingstudy-example.json
*ImagingStudy:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'patient', 'uid'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'subject'}
```

---
### valueset-search-entry-mode.json ✔
---
### audit-event-example-pixQuery.json
*AuditEvent --> source:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'identifier'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'observer'}
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

*AuditEvent --> agent:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'userId'}
```

**<sub>Transform output keys possibly lost or renamed:</sub>**
```python
{'who'}
```

---
### valueset-ucum-vitals-common.json
*ValueSet:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'extensible'}
```

---
### location-example.json ✔
---
### device-example-f001-feedingtube.json
*Device:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'udiCarrier'}
```

---
### valueset-provenance-entity-role.json ✔
---
### valueset-icd-10-procedures.json ✔
---
### patient-example-a.json ✔
---
### testscript-questionnaire.json ✔
---
### encounter-example-f003-abscess.json
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
### valueset-condition-outcome.json ✔
---
### supplyrequest-example.json
*SupplyRequest:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'fhir_comments'}
```

---
### valueset-compartment-type.json ✔
---
### valueset-http-verb.json ✔
---
### valueset-ex-onsettype.json ✔
---
### immunization-example-refused.json
*Immunization:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'date', 'explanation'}
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
### valueset-procedure-relationship-type.json ✔
---
### valueset-questionnaire-item-control.json ✔
---
### valueset-benefit-category.json ✔
---
### devicemetric-example.json ✔
---
### medicationexample15.json
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
### valueset-guidance-response-status.json ✔
---
### valueset-c80-facilitycodes.json ✔
---
### operation-patient-match.json
*OperationDefinition:*

**<sub>Keys lost during transform:</sub>**
```python
{'type'}
```

---
### valueset-teeth.json ✔
---
### valueset-reaction-event-certainty.json ✔
---
### medicationstatementexample4.json
*MedicationStatement:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'effectiveDateTime',
 'medicationReference',
 'patient',
 'reasonForUseCodeableConcept',
 'wasNotTaken'}
```

---
### patient-example-ihe-pcd.json ✔
---
### valueset-assert-operator-codes.json ✔
---
### valueset-question-max-occurs.json ✔
---
### conformance-questionnaire.json ✔
---
### questionnaireresponse-example-f201-lifelines.json
*QuestionnaireResponse --> item:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_linkId'}
```

---
### valueset-concept-property-type.json ✔
---
### valueset-reaction-event-severity.json ✔
---
### valueset-goal-priority.json ✔
---
### valueset-resource-types.json ✔
---
### valueset-udi.json ✔
---
### medication-example-f002-crestor.json
*Medication:*

**<sub>Input keys possibly lost or renamed:</sub>**
```python
{'package', 'isBrand'}
```

---
### valueset-allergy-intolerance-category.json ✔
---
### valueset-relatedperson-relationshiptype.json
*ValueSet --> compose:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'import'}
```

---
### valueset-report-codes.json ✔
---
### valueset-detectedissue-severity.json ✔
---
### medication-example-f201-salmeterol.json
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
### valueset-consistency-type.json ✔
---
### allergyintolerance-fishallergy.json
*AllergyIntolerance:*

**<sub>Keys lost during transform:</sub>**
```python
{'category'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_category', '_recordedDate', 'recordedDate', 'substance'}
```

---
### valueset-network-type.json ✔
---
### device-questionnaire.json ✔
---
### specimen-example-urine.json
*Specimen:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'treatment'}
```

*Specimen --> collection:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_collectedDateTime', 'collectedDateTime', 'fhir_comments'}
```

---
### valueset-grouping-behavior.json ✔
---
### valueset-condition-stage.json ✔
---
### valueset-procedure-request-status.json ✔
---
### valueset-extensions-ValueSet-end.json ✔
---
### valueset-medication-statement-status.json ✔
---
### valueset-composition-status.json ✔
---
### valueset-devicestatus.json ✔
---
### observation-example-genetics-1.json
*Observation:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'valueCodeableConcept'}
```

---
### valueset-entformula-additive.json
*ValueSet:*

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'_status'}
```

---
### valueset-benefit-subcategory.json ✔
---
### valueset-special-values.json ✔
---
### valueset-diagnostic-service-sections.json ✔
---
### valueset-food-type.json ✔
---
### procedure-example-biopsy.json
*Procedure:*

**<sub>Keys lost during transform:</sub>**
```python
{'status'}
```

**<sub>Invalid keys in inputs not defined in source definition:</sub>**
```python
{'notes', 'performedDateTime', 'reasonCodeableConcept'}
```

---
### medicationstatementexample2.json
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
{'medicationReference', 'effectiveDateTime', 'patient', 'wasNotTaken'}
```

---
### relatedperson-example-f001-sarah.json ✔
---
### valueset-search-param-type.json ✔
---
### valueset-enteral-route.json ✔
---
### valueset-document-reference-status.json ✔
---
### valueset-vaccination-protocol-dose-target.json ✔
---
### valueset-referralcategory.json ✔
---
### valueset-practitioner-role.json ✔
---
### valueset-diagnostic-requests.json ✔
---
### valueset-diet-type.json ✔
---
### valueset-nutrition-order-status.json ✔
---
### valueset-condition-clinical.json ✔
---
### valueset-defined-types.json ✔
---
