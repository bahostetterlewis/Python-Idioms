# From SO answer http://stackoverflow.com/a/16381580/505163
def is_string_in_string_list(string, string_list, delim='\t'):
    return string in delim.join(string_list)
