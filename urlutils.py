# URLUTILS
# ========
# Author: Kristján Eldjárn Hjörleifsson, kristjan@eldjarn.net
#
# One-to-one mapping of integers to strings
# Useful for decoupling database entries from autogenerated IDs.
# Note:
#   If the database is not ordered by the obfuscated value, the obfuscated
#   string should be clarified and the lookup done on the autogenerated ID
# ==============================================================================
KEYSPACE = "fw59eorpma2nvxb07liqt83u6kgzs41ycdjh"
CHAFF = 31337

def int_str(val, keyspace = KEYSPACE):
    """ Maps the integer val to a string determined by the position of
    characters in the keyspace """
    assert val >= 0
    out = ""
    while val > 0:
        val, digit = divmod(val, len(keyspace))
        out += keyspace[digit]
    return out[::-1]

def str_int(val, keyspace = KEYSPACE):
    """ Maps the string val to an integer determined by the position of
    individual characters in val in the keyspace """
    out = 0
    for c in val:
        out = out * len(keyspace) + keyspace.index(c)
    return out

def addChaff(val, chaff_val = CHAFF):
    """ Returns (val + 1) * chaff_val. We want to create a string longer than
    one char for low values. """
    # We offset the ID by 1, so as not to get an exception
    # when clarifying ID==0
    val = val+1
    return val * chaff_val

def removeChaff(chaffy_val, chaff_val = CHAFF):
    val, chaff = divmod(chaffy_val, chaff_val)
    if chaff != 0:
        raise ValueError("Invalid chaff")
    # Remove offset from addChaff
    return val-1

def obfuscate(clean_id):
    """ Maps an integer to a corresponding string """
    return int_str(addChaff(clean_id))

def clarify(dirty_id):
    """ Maps a string to a corresponding integer """
    return removeChaff(str_int(dirty_id))

