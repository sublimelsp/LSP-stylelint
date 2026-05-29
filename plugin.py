from __future__ import annotations

from enum import IntEnum
from LSP.plugin import LspPlugin
from LSP.plugin import notification_handler
from LSP.plugin import OnPreStartContext
from lsp_utils import NodeManager
from pathlib import Path
from sublime_lib import ResourcePath
from typing import final
from typing import TypedDict
from typing_extensions import override


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
    LspStylelintPlugin.register()


def plugin_unloaded():
    LspStylelintPlugin.unregister()


@final
class LspStylelintPlugin(LspPlugin):

    @classmethod
    @override
    def on_pre_start_async(cls, context: OnPreStartContext) -> None:
        package_name = cls.plugin_storage_path.name
        NodeManager.on_pre_start_async(
            context,
            cls.plugin_storage_path,
            ResourcePath("Packages", package_name, "language-server"),
            Path("node_modules", "@stylelint", "language-server", "bin", "stylelint-language-server.mjs"),
            node_version_requirement=">=22.17.0",
        )

    @notification_handler('stylelint/status')
    def on_stylelint_status(self, params: StatusParams) -> None:
        if (session := self.weaksession()) and (sb := session.get_session_buffer_for_uri_async(params['uri'])):
            for sv in sb.session_views:
                session.config.set_view_status(sv.view, state_text(params['state']))
