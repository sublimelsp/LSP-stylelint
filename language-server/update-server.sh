#!/usr/bin/env bash

# exit when any command fails
set -e

GITHUB_REPO_URL="https://github.com/stylelint/vscode-stylelint"
GITHUB_REPO_NAME=$(echo "${GITHUB_REPO_URL}" | command grep -oE '[^/]*$')

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="${SCRIPT_DIR}"
SRC_DIR="${REPO_DIR}/${GITHUB_REPO_NAME}"


# -------- #
# clean up #
# -------- #

pushd "${REPO_DIR}"

rm -rf "${SRC_DIR}" dist package.json

popd


# ------------------------- #
# download the source codes #
# ------------------------- #

pushd "${REPO_DIR}"

echo 'Enter commit SHA, branch or tag (for example 2.1.0) to build'
read -rp 'SHA, branch or tag (default: main): ' ref

# use the "main" branch by default
if [ "${ref}" = "" ]; then
    ref="main"
fi

temp_zip="src-${ref}.zip"
curl -L "${GITHUB_REPO_URL}/archive/${ref}.zip" -o "${temp_zip}"
unzip -z "${temp_zip}" | tr -d '\r' > update-info.log
unzip "${temp_zip}" && rm -f "${temp_zip}"
mv "${GITHUB_REPO_NAME}-"* "${SRC_DIR}"

popd

# ---------------- #
# compile the code #
# ---------------- #

pushd "${SRC_DIR}"

npm i
cp "${REPO_DIR}/bundle.ts" scripts/
npm run build
npm run bundle-base -- --minify

popd

# ------------- #
# collect files #
# ------------- #

pushd "${REPO_DIR}"

mv "${SRC_DIR}/package.json" .
mv "${SRC_DIR}/dist/" .

popd

# -------- #
# clean up #
# -------- #

pushd "${REPO_DIR}"

rm -rf "${SRC_DIR}"

popd
