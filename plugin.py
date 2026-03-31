from __future__ import annotations

from enum import IntEnum
from LSP.plugin import notification_handler
from lsp_utils import NpmClientHandler
from typing import final
from typing import TypedDict
from typing_extensions import override
import os


class Status(IntEnum):
    ok = 1
    warn = 2
    error = 3


class StatusParams(TypedDict):
    state: Status
    uri: str


def state_text(state: Status) -> str:
    if state == Status.error:
        return 'error'
    if state == Status.warn:
        return 'warning'
    return ''


def plugin_loaded():
    LspStylelintPlugin.setup()


def plugin_unloaded():
    LspStylelintPlugin.cleanup()


@final
class LspStylelintPlugin(NpmClientHandler):
    package_name = str(__package__)
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, "node_modules", "@stylelint", "language-server", "bin", "stylelint-language-server.mjs")

    @classmethod
    @override
    def required_node_version(cls) -> str:
        return '>=22.17.0'

    @notification_handler('stylelint/status')
    def on_stylelint_status(self, params: StatusParams) -> None:
        if (session := self.weaksession()) and (sb := session.get_session_buffer_for_uri_async(params['uri'])):
            for sv in sb.session_views:
                session.config.set_view_status(sv.view, state_text(params['state']))
