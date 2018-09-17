class Sample(object):
    """Define MC and data samples."""

    def __init__(self, name, das_id, xSection=None):
        self.name = name
        self.das_id = das_id
        self.xSection = xSection
