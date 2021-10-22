// Slightly update version of the original bundle script that doesn't include
// the vscode and extension specific code.

const path = require('path');
const fs = require('fs-extra');
const esbuild = require('esbuild');
const glob = require('fast-glob');

const rootDir = path.resolve(__dirname, '..');

const args = new Set(process.argv.slice(2));

/** @returns {Promise<void>} */
async function bundle() {
    const entryPoints = ['src/start-server.js'];

    for (const item of await glob('dist/*', { cwd: rootDir })) {
        await fs.remove(item);
    }

    try {
        await esbuild.build({
            absWorkingDir: rootDir,
            entryPoints,
            entryNames: '[name]',
            bundle: true,
            outdir: 'dist',
            format: 'cjs',
            platform: 'node',
            logLevel: 'info',
            watch: args.has('--watch'),
            sourcemap: args.has('--sourcemap'),
            minify: args.has('--minify'),
        });
    } catch {
        process.exit(1);
    }
}

bundle();
