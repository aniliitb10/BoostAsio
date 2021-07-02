"""Tests TCP communication between a server and a client."""

from testplan.testing.multitest import MultiTest, testsuite, testcase
from testplan.testing.multitest.driver.tcp import TCPServer, TCPClient
from testplan.testing.multitest.driver.app import App
import re


@testsuite
class TCPTestsuite(object):
    """TCP tests for a server and a client."""

    def setup(self, env):
        """Will be executed before the testcase."""
        # env.client.connect()

    @testcase
    def send_and_receive_msg(self, env, result):
        """
        Client sends a message, server received and responds back.
        """
        msg = env.client.cfg.name
        result.log("Client is sending: {}".format(msg))
        bytes_sent = env.client.send_text(msg)

        received = env.client.receive_text(size=bytes_sent)
        result.equal(received, msg, "Client received")


def get_multitest(name):
    """
    Creates and returns a new MultiTest instance to be added to the plan.
    The environment is a server and a client connecting using the context
    functionality that retrieves host/port of the server after is started.
    """
    test = MultiTest(
        name=name,
        suites=[TCPTestsuite()],
        environment=[
            App(
                "echo",
                binary="/home/anil/CLionProjects/BoostAsio/cmake-build-debug/async_echo_server",
                args=["12345"],
                stdout_regexps=[
                    re.compile(r".*Echo server is up.*")
                ],
            ),
            TCPClient(
                name="client",
                host="127.0.0.1",
                port=12345,
            ),
        ],
    )
    return test