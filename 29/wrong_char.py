import string


def get_index_different_char(chars):
    alphanumeric = list(string.ascii_letters + string.digits)

    single_alphanumeric_index = None
    single_non_alphanumeric_index = None

    for index, char in enumerate(chars):
        if str(char) in alphanumeric:
            if single_alphanumeric_index is None:
                single_alphanumeric_index = index
            else:
                # We've found our second alphanumeric character,
                # so we can stop if we've also found a non-alphanumeric one
                if single_non_alphanumeric_index is not None:
                    return single_non_alphanumeric_index
                single_alphanumeric_index = None
        else:
            if single_non_alphanumeric_index is None:
                single_non_alphanumeric_index = index
            else:
                # We've found our second non-alphanumeric character,
                # so we can stop if we've also found an alphanumeric one
                if single_alphanumeric_index is not None:
                    return single_alphanumeric_index
                single_non_alphanumeric_index = None

    # At this point we've gone through all characters and one of the indexes must be non-None
    return (
        single_alphanumeric_index
        if single_alphanumeric_index is not None
        else single_non_alphanumeric_index
    )
