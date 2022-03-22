from .documentcompare import DocumentCompare
from .jsoncompare import JSONCompare
import os.path


class TransformCompare:
    documentcompare: DocumentCompare

    def set_comparator(self, file_extension) -> None:
        # Only JSON implemented and only checking file extension, as opposed to ensuring document
        # structure is correct for the type.
        if file_extension == '.json':
            self.documentcompare = JSONCompare()
        elif file_extension == '.xml':
            raise NotImplementedError('XML compartor not implemented - TODO')
        elif file_extension == '.ttl':
            raise NotImplementedError('Turtle compartor not implemented - TODO')
        else:
            raise ValueError('Document type not supported')

    def compare_transform(self, input_file, transformed_file):
        input_file_extension = os.path.splitext(input_file)[1]
        transformed_file_extension = os.path.splitext(transformed_file)[1]

        if input_file_extension != transformed_file_extension:
            raise ValueError('Differing document types not supported.')

        self.set_comparator(input_file_extension)

        comparison = self.documentcompare.generate_comparison(input_file, transformed_file)

        # Order comparisons so report output is the same on each run, i.e. diff-able
        return self.order_dict(comparison)

    def order_dict(self, dictionary):
        result = {}
        for k, v in sorted(dictionary.items()):
            if isinstance(v, dict):
                result[k] = self.order_dict(v)
            else:
                result[k] = sorted(v)
        return result

    def count_flagged(self, comparisons):
        flagged = 0
        for f in comparisons:
            all_empty = True
            for k in comparisons[f]:
                if not (len(comparisons[f][k]['Lost']) == 0 and len(comparisons[f][k]['InputRenamed']) == 0 and
                   len(comparisons[f][k]['TransformedRenamed']) == 0 and len(comparisons[f][k]['InvalidKeys']) == 0):
                    all_empty = False
            if not all_empty:
                flagged = flagged + 1
        return flagged