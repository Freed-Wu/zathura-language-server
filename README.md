# syntax-test.vim

[![github/license](https://shields.io/github/license/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/blob/master/LICENSE)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/sublime-syntax.vim/total)](https://github.com/Freed-Wu/sublime-syntax.vim/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/sublime-syntax.vim/latest/total)](https://github.com/Freed-Wu/sublime-syntax.vim/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/releases/latest)

![github/languages](https://shields.io/github/languages/count/Freed-Wu/sublime-syntax.vim)
![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/sublime-syntax.vim)
![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/sublime-syntax.vim)
![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/sublime-syntax.vim)
![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/sublime-syntax.vim)
![github/v](https://shields.io/github/v/release/Freed-Wu/sublime-syntax.vim)

Vim filetype plugin for:

- [sublime-syntax](http://www.sublimetext.com/docs/syntax.html)
- [syntax-test](http://www.sublimetext.com/docs/syntax.html#testing)

![Screenshot](https://user-images.githubusercontent.com/32936898/194713936-8ea3403f-8133-4c75-876f-9d68bc145123.png)

- [x] ftplugin: commentstring, etc
- [x] syntax highlight, include incorrect header
- [x] completion
- [x] linter
- [ ] document hover
- [ ] LSP
- [ ] support [tmLanguage](https://macromates.com/manual/en/language_grammars)

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=1 -->

- [syntax-test.vim](#syntax-testvim)
  - [Syntax Highlight](#syntax-highlight)
  - [Completion](#completion)
  - [Linter](#linter)
    - [Install syntest](#install-syntest)
      - [Build From Source](#build-from-source)
      - [For Archlinux](#for-archlinux)
      - [Other Install Methods](#other-install-methods)

<!-- mdformat-toc end -->

## Syntax Highlight

Every syntax test file should have a correct header. If you input a typo, syntax
highlight will tell you:

![Correct](https://user-images.githubusercontent.com/32936898/194894921-0f9167a8-a297-4719-986f-93298111963a.png)

![Incorrect](https://user-images.githubusercontent.com/32936898/194894923-9b82fd5f-2f13-4651-abe5-1a645e737671.png)

If you input correct keyword of sublime syntax file, it will be highlighted as `Keyword`.
Note `watch` should be `match` and `strings` should be `string`:

![Keyword](https://user-images.githubusercontent.com/32936898/195125476-59f056e1-7001-4aa9-b2ba-62a8fd0e0d2e.png)

## Completion

Completion needs [coc.nvim](https://github.com/neoclide/coc.nvim). Now it can
complete scope names and sublime syntax file's keywords. Generate completion
cache needs [some python library](requirements.txt). If you don't want to
install python, you can use generated completion cache:

```vim
:echo g:sublime_syntax#cache_dir
# usually be ~/.cache/nvim/sublime_syntax.vim
```

```sh
install assets/json/*.json -Dt ~/.cache/nvim/sublime_syntax.vim
```

A more intelligent completion needs LSP, which is a TODO.

![Completion](https://user-images.githubusercontent.com/32936898/195147969-93486f40-9c8a-4b79-841b-e2c8dd0b2766.png)

## Linter

For sublime syntax files, make needs [bat](https://github.com/sharkdp/bat).
Linter needs [coc-yaml](https://github.com/neoclide/coc-yaml).

For syntax test files, `:make` needs [syntest](https://github.com/trishume/syntect).
Linter needs [coc-diagnostic](https://github.com/iamcco/coc-diagnostic/pull/136).

### Install syntest

#### Build From Source

```sh
git clone --depth=1 https://github.com/trishume/syntect
cd syntect
cargo build --release --example syntest
sudo install -D target/release/examples/syntest -t /usr/local/bin
```

#### For Archlinux

```sh
yay -S syntest
```

#### Other Install Methods

- [ ] Windows (Msys2)
- [ ] Android (Termux)
- [ ] Linux/macOS (Homebrew)
