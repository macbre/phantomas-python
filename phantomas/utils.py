""" Utility functions """


def is_sequence(arg):
    """
    Is given object a list or a tuple?
    """
    return type(arg) is list or type(arg) is tuple


def format_args(options):
    """ Convert hash/key options into arguments list """
    args = list()

    for key, value in options.items():
        # convert foo_bar key into --foo-bar option
        key = key.replace('_', '-')

        if value is True:
            # key: True
            # --key
            args.append('--{key}'.format(key=key))
        elif is_sequence(value):
            # key: ['foo', 'bar']
            # --key=foo,bar
            values = [str(val) for val in value]
            args.append('--{key}={values}'.format(
                key=key, values=','.join(values)))
        else:
            # key: 'foo'
            # --key=foo
            args.append('--{key}={value}'.format(key=key, value=value))

    return args
