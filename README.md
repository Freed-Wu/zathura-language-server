# syntax-test.vim

[![github/license](https://shields.io/github/license/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/blob/master/LICENSE)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/syntax-test.vim/total)](https://github.com/Freed-Wu/syntax-test.vim/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/syntax-test.vim/latest/total)](https://github.com/Freed-Wu/syntax-test.vim/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/syntax-test.vim)](https://github.com/Freed-Wu/syntax-test.vim/releases/latest)

![github/languages](https://shields.io/github/languages/count/Freed-Wu/syntax-test.vim)
![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/syntax-test.vim)
![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/syntax-test.vim)
![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/syntax-test.vim)
![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/syntax-test.vim)
![github/v](https://shields.io/github/v/release/Freed-Wu/syntax-test.vim)

Vim filetype plugin for [syntax-test](http://www.sublimetext.com/docs/syntax.html#testing).

![Screenshot](https://user-images.githubusercontent.com/32936898/194603713-1dbc6a4c-cd9a-4894-8cd0-bae0563fa176.png)

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=1 -->

- [syntax-test.vim](#syntax-testvim)
  - [Requirements](#requirements)
    - [Compiler](#compiler)
      - [Install syntest](#install-syntest)
        - [For Any OS](#for-any-os)
        - [For Archlinux](#for-archlinux)
        - [Other Install methods](#other-install-methods)
  - [See Also](#see-also)

<!-- mdformat-toc end -->

## Requirements

### Compiler

`:make` need `syntest`.

#### Install syntest

##### For Any OS

```sh
git clone --depth=1 https://github.com/trishume/syntect
cd syntect
cargo build --release --example syntest
sudo install -D target/release/examples/syntest -t /usr/local/bin
```

##### For Archlinux

```sh
yay -S syntest
```

##### Other Install methods

- [ ] Windows (Msys2)
- [ ] Android (Termux)
- [ ] Linux/macOS (Homebrew)

## See Also

- [syntest for coc-diagnostic](https://github.com/iamcco/coc-diagnostic/pull/136)
