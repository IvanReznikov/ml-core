from sourced.ml.core.algorithms.uast_struct_to_bag import UastSeq2Bag
from sourced.ml.core.extractors.helpers import (
    BagsExtractor, filter_kwargs, get_names_from_kwargs, register_extractor)


@register_extractor
class UastSeqBagExtractor(BagsExtractor):
    NAME = "uast2seq"
    NAMESPACE = "s."
    OPTS = dict(get_names_from_kwargs(UastSeq2Bag.__init__))
    OPTS.update(BagsExtractor.OPTS)

    def __init__(self, docfreq_threshold=None, **kwargs):
        original_kwargs = kwargs
        uast2bag_kwargs = filter_kwargs(kwargs, UastSeq2Bag.__init__)
        for k in uast2bag_kwargs:
            kwargs.pop(k)
        super().__init__(docfreq_threshold, **kwargs)
        self._log.debug("__init__ %s", original_kwargs)
        self.uast2bag = UastSeq2Bag(**uast2bag_kwargs)

    def uast_to_bag(self, uast):
        return self.uast2bag(uast)