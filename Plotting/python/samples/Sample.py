class Sample(object):
    """Define MC and data samples."""

    def __init__(self, name, das_id, xsec=None):
        self.name = name
        self.das_id = das_id
        self.xsec = xsec
