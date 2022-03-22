import json
import tarfile
import os
from functools import reduce
from .documentcompare import DocumentCompare

# TODO Haven't considered the case where the keys no longer exist in the transformed version, and when the
# target dictionary is empty, the root will show as lost, really this should be renamed or possibly lost
class JSONCompare(DocumentCompare):

    # NOTE: If the packages aren't tar-ed and are available on disk at ~/.fhir for example, this runs in a few seconds.
    # The packages are included in the repo so there is minimal config needed to run it out of the box
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../../'
        self.IGNORED_KEYS = ['resourceType']
        self.pkg_r4 = tarfile.open(self.ROOT_DIR + 'packages/hl7.fhir.r4.core#4.0.1/package.tar')
        self.pkg_r3 = tarfile.open(self.ROOT_DIR + 'packages/hl7.fhir.r3.core#3.0.2/package.tar')

    def generate_comparison(self, input_file, transformed_file) -> dict:
        input_data = json.load(open(input_file))
        resource_type = input_data.get('resourceType')

        # Remove keys not defined by default in StructureDefinitions.  TODO find an exhaustive list of this
        input_data = self._remove_ignored_keys(input_data, self.IGNORED_KEYS)

        transformed_data = json.load(open(transformed_file))

        # NOTE: If this was to be extends for all versions, would need to look at generalising the package path
        source_definition = json.load(self.pkg_r3.extractfile('package/StructureDefinition-' + resource_type + '.json'))
        target_definition = json.load(self.pkg_r4.extractfile('package/StructureDefinition-' + resource_type + '.json'))

        # Get resource definition from snapshot
        source_snapshot_elements = self._get_snapshot_elements(source_definition)
        target_snapshot_elements = self._get_snapshot_elements(target_definition)

        # Transform the list of elements into a structured dictionary, indexed by tuples containing the path to
        # a given set of elements
        source_elements_dic = self._transform_element_list(source_snapshot_elements)
        target_elements_dic = self._transform_element_list(target_snapshot_elements)

        definition_key = (resource_type,)

        root_comparison = self._element_set_comparison(definition_key, input_data, source_elements_dic,
                                                       transformed_data, target_elements_dic)

        return self._compare_sub_keys(root_comparison, definition_key, input_data, source_elements_dic,
                                      transformed_data, target_elements_dic)

    def _remove_ignored_keys(self, input_data, ignored_keys):
        if not ignored_keys:
            ignored_keys = []

        if input_data:
            [input_data.pop(k) for k in ignored_keys if k in input_data.keys()]
            return input_data
        else:
            return []

    def _get_snapshot_elements(self, input_data) -> list:
        if input_data and \
                'snapshot' in input_data and \
                'element' in input_data['snapshot']:
            return [e for e in input_data['snapshot']['element']]
        else:
            return []

    def _extract_choice_types(self, element):
        if not element:
            return []

        path = element['id'].split('.')
        choice_types = []
        for c in element['type']:
            if c['code']:
                # Take all items in list except on the last.  With the last item, concatenate the type code after
                # capitalising and add this to a list with the first items.
                choice_type_updated_path = [*path[0:-1], path[-1].replace('[x]', '') + c['code'].title()]
                choice_types.append(choice_type_updated_path)
        return choice_types

    def _transform_element_list(self, elements) -> dict:
        if not elements:
            return {}

        paths = []
        for el in elements:
            if '[x]' in el['id']:
                paths.extend(self._extract_choice_types(el))
            else:
                paths.append(el['id'].split('.'))

        dic = {}
        for p in paths:
            dic.setdefault(tuple(p[:-1]), []).append(p[-1])

        return dic

    def _element_set_comparison(self, definition_key, input_data, source_dic, transformed_data, target_dic) -> dict:
        # InvalidKeys = SET( input - source_superset )
        comparison = {definition_key: {'InvalidKeys': self._get_invalid_keys(definition_key, input_data, source_dic)}}

        # ValidKeys = SET( input ∩ source_superset )
        comparison[definition_key]['ValidKeys'] = self._get_valid_keys(definition_key, input_data, source_dic)

        # SET( ((input - source_superset) - transformed) ∩ target_superset )
        # SET( ((input ∩ source_superset) - transformed) ∩ target_superset )
        comparison[definition_key]['Lost'] = self._get_lost_keys(definition_key,
                                                                 input_data,
                                                                 source_dic,
                                                                 transformed_data,
                                                                 target_dic)

        # InputRenamed = SET( (input - transformed) ∩ (source_superset Δ target_superset) )
        # TransformedRenamed = SET( (transformed - input) ∩ (source_superset Δ target_superset) )
        comparison[definition_key]['InputRenamed'], \
        comparison[definition_key]['TransformedRenamed'] = self._get_renamed_keys(definition_key,
                                                                                  comparison[definition_key]['ValidKeys'],
                                                                                  source_dic,
                                                                                  transformed_data,
                                                                                  target_dic)

        comparison[definition_key]['KeysToExamine'] = self._get_keys_to_examine(definition_key,
                                                                                input_data,
                                                                                comparison[definition_key]['ValidKeys'],
                                                                                comparison[definition_key]['InputRenamed'],
                                                                                source_dic)

        return comparison

    def _compare_sub_keys(self, comparison, definition_key, input_data, source_dic, transformed_data, target_dic) -> dict:
        if isinstance(input_data, list):
            input_data = self._strip_list(input_data)
        if isinstance(transformed_data, list):
            transformed_data = self._strip_list(transformed_data)

        for k in comparison[definition_key]['KeysToExamine']:
            if definition_key + (k,) in comparison.keys():
                if comparison[definition_key + (k,)]['KeysToExamine']:
                    for sk in comparison[definition_key + (k,)]['KeysToExamine']:
                        comparison = comparison | self._compare_sub_keys(comparison,
                                                                         definition_key + (k,),
                                                                         input_data.get(k).get(sk),
                                                                         source_dic,
                                                                         transformed_data.get(k).get(sk),
                                                                         target_dic)
            else:
                comparison = comparison | self._element_set_comparison(definition_key + (k,),
                                                                       input_data.get(k),
                                                                       source_dic,
                                                                       transformed_data.get(k),
                                                                       target_dic)

        return comparison

    def _is_or_contains_dict(self, data) -> bool:
        if data and isinstance(data, dict):
            return True
        if data and isinstance(data, list):
            # True if one or more dictionaries exist in the list
            return self._search_list_for_dict(data)

        return False

    def _search_list_for_dict(self, x) -> dict:
        if not x:
            return False

        cases = {list: lambda t: self._search_list_for_dict(t[0]),
                 dict: lambda t: t}

        try:
            return bool(cases[type(x)](x))
        except KeyError:
            return False

    def _strip_list(self, data):
        if not data:
            return {}
        else:
            return reduce(lambda a, b: {**a, **b}, data)

    def _get_invalid_keys(self, definition_key, input_data, source_dic) -> set:
        if not input_data:
            return set()

        if not source_dic:
            raise ValueError("Source definition is empty.")

        if isinstance(input_data, list):
            input_data = self._strip_list(input_data)

        # InvalidKeys = SET( input - source_superset )
        if definition_key in source_dic.keys():
            return set(input_data.keys()).difference(source_dic[definition_key])
        else:
            raise ValueError(''.join(definition_key) + 'is not a key in the source definition')

    def _get_valid_keys(self, definition_key, input_data, source_dic) -> set:
        if not input_data:
            return set()

        if not source_dic:
            raise ValueError("Source definition is empty.")

        if isinstance(input_data, list):
            input_data = self._strip_list(input_data)

        # ValidKeys = SET( input ∩ source_superset )
        if definition_key in source_dic.keys():
            return set(input_data.keys()).intersection(source_dic[definition_key])
        else:
            raise ValueError(''.join(definition_key) + 'is not a key in the source definition')

    def _get_lost_keys(self, definition_key, input_data, source_dic, transformed_data, target_dic) -> set:
        if not input_data:
            return set()

        if not source_dic or not target_dic:
            raise ValueError("Source or target definition is empty.")

        if isinstance(input_data, list):
            input_data = self._strip_list(input_data)

        if isinstance(transformed_data, list):
            transformed_data = self._strip_list(transformed_data)

        if transformed_data is None:
            transformed_data = dict()

        if definition_key in target_dic.keys():
            target_dictionary = target_dic[definition_key]
        else:
            target_dictionary = dict()

        # SET( ((input ∩ source_superset) ∩ target_superset) - transformed )
        if definition_key in source_dic:
            return set(
                (set(input_data.keys()).intersection(source_dic[definition_key]))
            ).intersection(
                target_dictionary
            ) - transformed_data.keys()
        else:
            raise ValueError(''.join(definition_key) + 'is not a key in the source definition')

    def _get_renamed_keys(self, definition_key, valid_keys, source_dic, transformed_data, target_dic) -> (set, set):
        if not valid_keys:
            valid_keys = dict()

        if isinstance(transformed_data, list):
            transformed_data = self._strip_list(transformed_data)

        if transformed_data is None:
            transformed_data = dict()

        if target_dic and definition_key in target_dic.keys():
            target_dictionary = target_dic[definition_key]
        else:
            target_dictionary = dict()

        # SET( (source_superset Δ target_superset) )
        if source_dic is not None and definition_key in source_dic:
            source_target_symmetric_diff = set(source_dic[definition_key]).symmetric_difference(target_dictionary)
        else:
            raise ValueError(''.join(definition_key) + 'is not a key in the source definition')

        # InputRenamed = SET( (input - transformed) ∩ (source_superset Δ target_superset) )
        input_renamed = set(
            valid_keys - transformed_data.keys()
        ).intersection(
            source_target_symmetric_diff
        )

        # TransformedRenamed = SET( (transformed - input) ∩ (source_superset Δ target_superset) )
        transformed_renamed = set(
            transformed_data.keys() - valid_keys
        ).intersection(
            source_target_symmetric_diff
        )

        return input_renamed, transformed_renamed

    def _get_keys_to_examine(self, definition_key, input_data, valid_keys, input_renamed, source_dic) -> set:
        valid_keys_to_examine = set(valid_keys).difference(input_renamed)

        keys_to_examine = []
        if isinstance(input_data, list):
            for d in input_data:
                keys_to_examine.extend([k
                                        for k in valid_keys_to_examine
                                        if self._is_or_contains_dict(d.get(k))])
        elif isinstance(input_data, dict):
            keys_to_examine = [k
                               for k in valid_keys_to_examine
                               if self._is_or_contains_dict(input_data.get(k))]

        keys_to_examine_defined = [k[len(definition_key)]
                                   for k in source_dic.keys()
                                   if len(k) == len(definition_key) + 1]

        return set(keys_to_examine).intersection(keys_to_examine_defined)
