# sublime-syntax.vim

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/sublime-syntax.vim/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/sublime-syntax.vim/main)
[![github/workflow](https://github.com/Freed-Wu/sublime-syntax.vim/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/sublime-syntax.vim/actions)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FFreed-Wu%2Fsublime-syntax.vim.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FFreed-Wu%2Fsublime-syntax.vim?ref=badge_shield)

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

[![github/license](https://shields.io/github/license/Freed-Wu/sublime-syntax.vim)](https://github.com/Freed-Wu/sublime-syntax.vim/blob/master/LICENSE)
![github/languages](https://shields.io/github/languages/count/Freed-Wu/sublime-syntax.vim)
![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/sublime-syntax.vim)
![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/sublime-syntax.vim)
![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/sublime-syntax.vim)
![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/sublime-syntax.vim)
![github/v](https://shields.io/github/v/release/Freed-Wu/sublime-syntax.vim)

Vim filetype plugin for:

- [sublime-syntax](http://www.sublimetext.com/docs/syntax.html)

- [syntax-test](http://www.sublimetext.com/docs/syntax.html#testing)

- [x] ftplugin: commentstring, etc

- [x] compilers: bat, syntest

- [x] syntax highlight, include incorrect header

## Compilers

Install

- [syntest](https://github.com/trishume/syntect) for `syntax_test_*`
- [bat](https://github.com/sharkdp/bat) for `*.sublime-syntax`

### syntest

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

## Syntax Highlight

Every syntax test file should have a correct header. If you input a typo, syntax
highlight will tell you:

![Correct](https://user-images.githubusercontent.com/32936898/194894921-0f9167a8-a297-4719-986f-93298111963a.png)

![Incorrect](https://user-images.githubusercontent.com/32936898/194894923-9b82fd5f-2f13-4651-abe5-1a645e737671.png)

If you input correct keyword of sublime syntax file, it will be highlighted as `Keyword`.
Note `watch` should be `match` and `strings` should be `string`:

![Keyword](https://user-images.githubusercontent.com/32936898/195125476-59f056e1-7001-4aa9-b2ba-62a8fd0e0d2e.png)

## More usages

[`:help sublime-syntax`](doc/sublime-syntax.txt)

## Similar Projects

- [sublime-syntax-language-server](https://github.com/Freed-Wu/sublime-syntax-language-server)

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FFreed-Wu%2Fsublime-syntax.vim.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FFreed-Wu%2Fsublime-syntax.vim?ref=badge_large)
