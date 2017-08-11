class ConfigBuildFilter(object):

    def __init__(self, included=[], excluded=[]):
        self.reserved = ['Incondition', 'InForLoop']
        self.included = [x for x in included if x not in self.reserved]
        self.excluded = [x for x in excluded]
        print "Included:{}".format(self.included)
        print "Excluded:{}".format(self.excluded)

    def allowed(self, name):
        if self.included and self.excluded:
            if name in self.included:
                return True
            if name in self.excluded and name not in self.reserved:
                return False
            return True
        elif self.included:
            return name in self.included or name in self.reserved
        elif self.excluded:
            return name not in self.excluded
        return True

    def extend_from_dict(self, d):
        if 'excluded' in d:
            self.excluded.extend(d['excluded'])
        if 'included' in d:
            items = [x for x in d['included'] if x not in self.reserved]
            self.included.extend(items)
        return self
