# zathura-language-server

[![readthedocs](https://shields.io/readthedocs/zathura-language-server)](https://zathura-language-server.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Freed-Wu/zathura-language-server/main.svg)](https://results.pre-commit.ci/latest/github/Freed-Wu/zathura-language-server/main)
[![github/workflow](https://github.com/Freed-Wu/zathura-language-server/actions/workflows/main.yml/badge.svg)](https://github.com/Freed-Wu/zathura-language-server/actions)
[![codecov](https://codecov.io/gh/Freed-Wu/zathura-language-server/branch/main/graph/badge.svg)](https://codecov.io/gh/Freed-Wu/zathura-language-server)
[![DeepSource](https://deepsource.io/gh/Freed-Wu/zathura-language-server.svg/?show_trend=true)](https://deepsource.io/gh/Freed-Wu/zathura-language-server)

[![github/downloads](https://shields.io/github/downloads/Freed-Wu/zathura-language-server/total)](https://github.com/Freed-Wu/zathura-language-server/releases)
[![github/downloads/latest](https://shields.io/github/downloads/Freed-Wu/zathura-language-server/latest/total)](https://github.com/Freed-Wu/zathura-language-server/releases/latest)
[![github/issues](https://shields.io/github/issues/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/discussions)
[![github/milestones](https://shields.io/github/milestones/all/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/milestones)
[![github/forks](https://shields.io/github/forks/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/network/members)
[![github/stars](https://shields.io/github/stars/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/stargazers)
[![github/watchers](https://shields.io/github/watchers/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/watchers)
[![github/contributors](https://shields.io/github/contributors/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/commits)
[![github/release-date](https://shields.io/github/release-date/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/releases/latest)

[![github/license](https://shields.io/github/license/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server)
[![github/languages/top](https://shields.io/github/languages/top/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server)
[![github/directory-file-count](https://shields.io/github/directory-file-count/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server)
[![github/code-size](https://shields.io/github/languages/code-size/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server)
[![github/repo-size](https://shields.io/github/repo-size/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server)
[![github/v](https://shields.io/github/v/release/Freed-Wu/zathura-language-server)](https://github.com/Freed-Wu/zathura-language-server)

[![pypi/status](https://shields.io/pypi/status/zathura-language-server)](https://pypi.org/project/zathura-language-server/#description)
[![pypi/v](https://shields.io/pypi/v/zathura-language-server)](https://pypi.org/project/zathura-language-server/#history)
[![pypi/downloads](https://shields.io/pypi/dd/zathura-language-server)](https://pypi.org/project/zathura-language-server/#files)
[![pypi/format](https://shields.io/pypi/format/zathura-language-server)](https://pypi.org/project/zathura-language-server/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/zathura-language-server)](https://pypi.org/project/zathura-language-server/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/zathura-language-server)](https://pypi.org/project/zathura-language-server/#files)

A language server for zathura's zathurarc.

- [x] [Diagnostic](https://microsoft.github.io/language-server-protocol/specifications/specification-current#diagnostic):
  - [x] option value
  - [x] function
  - [x] argument
  - [x] included paths must be unique
  - [x] unmapped keys must be unique
- [x] [Hover](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_hover)
  - [x] option
  - [x] command
- [x] [Completion](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_completion)
  - [x] option
  - [x] command
  - [x] mode
  - [x] function
  - [x] argument
  - [x] included path

## Diagnostic

![diagnostic](https://github.com/Freed-Wu/zathura-language-server/assets/32936898/f30764f0-afae-4f1b-a966-fc9eaabdafa7)

## Document hover

![document hover](https://github.com/Freed-Wu/zathura-language-server/assets/32936898/1399c992-9dfc-4b7f-9640-a66f0dff5432)

## Completion

![option](https://github.com/Freed-Wu/zathura-language-server/assets/32936898/5dfc602d-3089-4c85-8b8c-5e7ca2738c66)

![function](https://github.com/Freed-Wu/zathura-language-server/assets/32936898/45b75d73-d8ec-42b6-881e-8255e3a4f6b1)

See
[![readthedocs](https://shields.io/readthedocs/zathura-language-server)](https://zathura-language-server.readthedocs.io)
to know more.
