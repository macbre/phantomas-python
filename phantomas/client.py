"""
Python's phantomas wrapper
"""
import json
import logging

from subprocess import Popen, PIPE

from .errors import PhantomasError


class Phantomas(object):
    """ Main entry point"""

    CMD = 'phantomas'

    def __init__(self, url, **kwargs):
        """
        Set up phantomas run

        :param url:
        :param kwargs:
        :return:
        """
        self._logger = logging.getLogger(self.__class__.__name__)

        self._url = url

        self._options = dict()
        self._options.update(kwargs)

        self._options['reporter'] = 'json'
        self._options['url'] = url

    def run(self):
        """ Perform phantomas run """
        self._logger.info("running for <{url}>".format(url=self._url))

        args = self.format_args(self._options)
        self._logger.debug("command: {cmd} / args: {args}".
                           format(cmd=self.CMD, args=args))

        # run the process
        try:
            process = Popen(
                args=[self.CMD] + args,
                stdin=PIPE,
                stdout=PIPE,
                stderr=PIPE
            )

            pid = process.pid
            self._logger.debug("running as PID #{pid}".format(pid=pid))
        except OSError as ex:
            raise PhantomasError("Failed to run phantomas: exit code #{errno}".
                                 format(errno=ex.errno))

        # wait to complete
        try:
            stdout, stderr = process.communicate()
            returncode = process.returncode
        except Exception:
            raise PhantomasError("Failed to complete the run")

        # check the response code
        self._logger.debug("completed with return code #{returncode}".
                           format(returncode=returncode))

        if stderr != '':
            self._logger.debug("stderr: {stderr}".format(stderr=stderr))
            raise PhantomasError("Got #{returncode} return code".
                                 format(returncode=returncode))

        # try parsing the response
        try:
            results = json.loads(stdout)
        except Exception:
            raise PhantomasError("Unable to parse the response")

        return results

    @staticmethod
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
            elif hasattr(value, '__iter__'):
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

    def __repr__(self):
        return '<Phantomas for {url}>'.format(url=self._url)
