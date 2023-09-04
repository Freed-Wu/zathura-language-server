#!/usr/bin/env bash
cd "$(dirname "$(readlink -f "$0")")/../release" || exit 1
find . -mindepth 1 -maxdepth 1 -not -name '.git' -exec rm -r {} \;
cp -r ../{ftdetect,ftplugin,syntax,README.md,LICENSE} .

git add -A
git config --global user.name 'Github Actions'
git config --global user.email '41898282+github-actions[bot]@users.noreply.github.com'
git commit -m ":bookmark: Dump version"
git remote set-url origin "https://x-access-token:$GH_TOKEN@github.com/$GITHUB_REPOSITORY"
git push
