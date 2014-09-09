URLUTILS
========
Author: Kristján Eldjárn Hjörleifsson, kristjan@eldjarn.net


DESCRIPTION
-----------
One-to-one mapping of integers to strings
Useful for decoupling database entries from autogenerated IDs.
Note:
  If the database is not ordered by the obfuscated value, the obfuscated
  string should be clarified and the lookup done on the autogenerated ID


USE
---
    init_integer = 27
    obfuscated_value = urlutils.obfuscate(init_integer)
    processed_integer = urlutils.clarify(obfuscated_value)
    assert init_integer == processed_integer
