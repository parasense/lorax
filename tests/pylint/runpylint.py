#!/usr/bin/python3

import sys

from pocketlint import FalsePositive, PocketLintConfig, PocketLinter

class LoraxLintConfig(PocketLintConfig):
    def __init__(self):
        PocketLintConfig.__init__(self)

        self.falsePositives = [ FalsePositive(r"Module 'pylorax' has no 'version' member"),
                                FalsePositive(r"Catching too general exception Exception"),
                                FalsePositive(r"^E0712.*: Catching an exception which doesn't inherit from (Base|)Exception: GError$"),
                                FalsePositive(r"Module 'composer' has no 'version' member"),
                              ]

    @property
    def pylintPlugins(self):
        retval = super(LoraxLintConfig, self).pylintPlugins
        # Not using threads so we can skip this
        retval.remove("pocketlint.checkers.environ")
        # No markup used
        retval.remove("pocketlint.checkers.markup")
        return retval

if __name__ == "__main__":
    conf = LoraxLintConfig()
    linter = PocketLinter(conf)
    rc = linter.run()
    sys.exit(rc)
