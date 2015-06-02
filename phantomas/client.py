"""
Python's phantomas wrapper
"""
import json
import logging

from subprocess import Popen, PIPE

from .errors import PhantomasRunError,\
    PhantomasResponseParsingError, PhantomasFailedError
from .results import Results, Runs
from .utils import format_args


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

        if 'exec_path' in kwargs:
            self._cmd = kwargs['exec_path']
            del kwargs['exec_path']
        else:
            self._cmd = self.CMD

        self._options = dict()
        self._options.update(kwargs)

        self._options['reporter'] = 'json'
        self._options['url'] = url

    def run(self):
        """ Perform phantomas run """
        self._logger.info("running for <{url}>".format(url=self._url))

        args = format_args(self._options)
        self._logger.debug("command: `{cmd}` / args: {args}".
                           format(cmd=self._cmd, args=args))

        # run the process
        try:
            process = Popen(
                args=[self._cmd] + args,
                stdin=PIPE,
                stdout=PIPE,
                stderr=PIPE
            )

            pid = process.pid
            self._logger.debug("running as PID #{pid}".format(pid=pid))
        except OSError as ex:
            raise PhantomasRunError(
                "Failed to run phantomas: {0}".format(ex), ex.errno)

        # wait to complete
        try:
            stdout, stderr = process.communicate()
            returncode = process.returncode
        except Exception:
            raise PhantomasRunError("Failed to complete the run")

        # for Python 3.x - decode bytes to string
        stdout = stdout.decode('utf8')
        stderr = stderr.decode('utf8')

        # check the response code
        self._logger.debug("completed with return code #{returncode}".
                           format(returncode=returncode))

        if stderr != '':
            self._logger.debug("stderr: {stderr}".format(stderr=stderr))

            raise PhantomasFailedError(stderr.strip(), returncode)

        # try parsing the response
        try:
            results = json.loads(stdout)
        except Exception:
            raise PhantomasResponseParsingError("Unable to parse the response")

        if self._options.get("runs", 0) > 1:
            return Runs(self._url, results)
        else:
            return Results(self._url, results)

    def __repr__(self):
        return '<Phantomas for {url}>'.format(url=self._url)
