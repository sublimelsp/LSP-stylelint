import os
from lsp_utils import NpmClientHandler


def plugin_loaded():
    LspStylelintPlugin.setup()


def plugin_unloaded():
    LspStylelintPlugin.cleanup()


class LspStylelintPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, 'dist', 'server.js')
    skip_npm_install = True
