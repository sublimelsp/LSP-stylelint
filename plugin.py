from __future__ import annotations

from lsp_utils import NpmClientHandler
from typing import final
from typing_extensions import override
import os


def plugin_loaded():
    LspStylelintPlugin.setup()


def plugin_unloaded():
    LspStylelintPlugin.cleanup()


@final
class LspStylelintPlugin(NpmClientHandler):
    package_name = str(__package__)
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, "node_modules", "@stylelint", "language-server", "bin", "stylelint-language-server.mjs")  # noqa: E501

    @classmethod
    @override
    def required_node_version(cls) -> str:
        return '>=22.17.0'
