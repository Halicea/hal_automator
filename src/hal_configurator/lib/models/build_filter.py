class ConfigBuildFilter(object):
    def __init__(self, included=[], excluded=[]):
        self.included = included
        self.excluded = excluded

    def allowed(self, name):
        print "Included:{}".format(self.included)
        print "Excluded:{}".format(self.excluded)
        if self.included and self.excluded:
            if name in self.included:
                return True
            if name in self.excluded:
                return False
            return True
        elif self.included:
            return name in self.included
        elif self.excluded:
            return name not in self.excluded
        else:
            return True

    def extend_from_dict(self, d):
        if 'excluded' in d:
            self.excluded.extend(d['excluded'])
        if 'included' in d:
            self.included.extend(d['included'])
        return self
