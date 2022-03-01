# LSP-stylelint

Stylelint support for Sublime's LSP plugin using [Stylelint server](https://github.com/stylelint/vscode-stylelint/).

- Install [LSP](https://packagecontrol.io/packages/LSP) and `LSP-stylelint` from Package Control.
  If you use Sass or SCSS, install [Sass](https://packagecontrol.io/packages/Sass).
  If you use Less, install [LESS](https://packagecontrol.io/packages/LESS).
- Restart Sublime.

## Configuration

Configure the Stylelint language server by accessing `Preferences > Package Settings > LSP > Servers > LSP-stylelint`.

## FAQ

Q: I'm using Stylelint 13 in my project and the package is telling me that it's no longer supported.

A: Please update Stylelint to version 14 by following the [migration guide](https://github.com/stylelint/vscode-stylelint#migrating-from-vscode-stylelint-0xstylelint-13x).

Q: How to enable Stylelint to automatically fix issues on saving the file?

A: Open `Preferences: LSP Settings` from the command palette and add or modify the following setting:

```js
  "lsp_code_actions_on_save": {
    "source.fixAll.stylelint": true,
  },
```
