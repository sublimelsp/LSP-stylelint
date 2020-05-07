#!/usr/bin/env bash
# @see https://github.com/mattn/vim-lsp-settings/pull/48

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="${SCRIPT_DIR}"
SRC_DIR="${REPO_DIR}/vscode-stylelint"
TEMP_DIR="${SRC_DIR}/temp"


# ------------------------ #
# clean out existing files #
# ------------------------ #

pushd "${REPO_DIR}" || exit

rm -rf "${SRC_DIR}"

mkdir -p "${TEMP_DIR}"

popd || exit


# ------------------------- #
# download the source codes #
# ------------------------- #

pushd "${TEMP_DIR}" || exit

echo 'Enter commit SHA or tag (for example 2.1.0) to build'
read -rp 'SHA or tag: ' ref

# or get the source via git clone
# git clone --depth=1 https://github.com/stylelint/vscode-stylelint "${SRC_DIR}"

# We strip the top-level directory so that we don't have to deal with extra one.
curl -L "https://github.com/stylelint/vscode-stylelint/archive/${ref}.tar.gz" | tar -xzv --strip 1

popd || exit


# ----------------- #
# move server files #
# ----------------- #

pushd "${TEMP_DIR}" || exit

cp -r lib server.js package.json package-lock.json "${SRC_DIR}"
rm -rf "${TEMP_DIR}"

popd || exit
