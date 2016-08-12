#!/bin/bash

set -e

mkdocs_repo=https://github.com/mkdocs/mkdocs.git
mkdocs_dir=$(mktemp -d)
themes_dir=mkdocs_bootswatch
bootswatch_themes=(cerulean cosmo cyborg darkly flatly journal lumen paper
                   readable sandstone simplex slate spacelab superhero united
                   yeti)
bootswatch_url=https://bootswatch.com

git clone --depth 1 --branch master --single-branch "$mkdocs_repo" "$mkdocs_dir"
rm -rf "$themes_dir"
mkdir "$themes_dir"
cd "$themes_dir"
touch __init__.py
for theme in "${bootswatch_themes[@]}"; do
    mkdir "$theme"
    cp -r "$mkdocs_dir"/mkdocs/themes/mkdocs/* "$theme"
    wget -O "$theme"/css/bootstrap-custom.min.css \
            "$bootswatch_url/$theme"/bootstrap.min.css
done
rm -rf "$mkdocs_dir"
cd ..
git add -A "$themes_dir"
git commit -m 'Update themes.'
git checkout tweaks
git rebase master
git checkout master
git apply <(git diff --binary master..tweaks)
git add -A "$themes_dir"
git commit -m 'Tweak updated themes.'
