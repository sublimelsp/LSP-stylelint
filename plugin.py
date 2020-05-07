import os
from lsp_utils import NpmClientHandler


def plugin_loaded():
    LspVscodeStylelintPlugin.setup()


def plugin_unloaded():
    LspVscodeStylelintPlugin.cleanup()


class LspVscodeStylelintPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'vscode-stylelint'
    server_binary_path = os.path.join(server_directory, 'server.js')
