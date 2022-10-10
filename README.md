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

- [x] syntax highlight, include incorrect header
- [x] ftplugin: commentstring, etc
- [x] linter
- [x] completion
- [ ] document hover
- [ ] support [tmLanguage](https://macromates.com/manual/en/language_grammars)

![Screenshot](https://user-images.githubusercontent.com/32936898/194713936-8ea3403f-8133-4c75-876f-9d68bc145123.png)

![Correct](https://user-images.githubusercontent.com/32936898/194894921-0f9167a8-a297-4719-986f-93298111963a.png)

![Incorrect](https://user-images.githubusercontent.com/32936898/194894923-9b82fd5f-2f13-4651-abe5-1a645e737671.png)

![Completion](https://user-images.githubusercontent.com/32936898/194894911-0da392fd-59af-429c-8683-d9ee06bc3963.png)

![sublime-syntax](https://user-images.githubusercontent.com/32936898/194923623-4be67f08-6487-4f90-9f24-6686fc3a3e12.png)

<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=1 -->

- [syntax-test.vim](#syntax-testvim)
  - [Requirements](#requirements)
    - [Completion](#completion)
    - [Compiler](#compiler)
      - [Install syntest](#install-syntest)
        - [Build From Source](#build-from-source)
        - [For Archlinux](#for-archlinux)
        - [Other Install Methods](#other-install-methods)
    - [Document](#document)
      - [Dein](#dein)
  - [See Also](#see-also)

<!-- mdformat-toc end -->

## Requirements

### Completion

Completion needs [coc.nvim](https://github.com/neoclide/coc.nvim).

### Compiler

`:make` needs [syntest](https://github.com/trishume/syntect).

#### Install syntest

##### Build From Source

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

##### Other Install Methods

- [ ] Windows (Msys2)
- [ ] Android (Termux)
- [ ] Linux/macOS (Homebrew)

### Document

`doc/syntax-test.txt` is generated by [vimdoc](https://github.com/google/vimdoc).
You can generate document automatically after every update by your plugin
manager (e.g., [dein](https://github.com/Shougo/dein.vim))

#### Dein

```vim
  call dein#add('Freed-Wu/sublime-syntax.vim', {
        \ 'build': 'vimdoc .',
        \ })
```

## See Also

- [syntest for coc-diagnostic](https://github.com/iamcco/coc-diagnostic/pull/136)
