# Configure

See customization in
<https://zathura-language-server.readthedocs.io/en/latest/api/zathura-language-server.html#zathura_language_server.server.get_document>.

## (Neo)[Vim](https://www.vim.org)

### [coc.nvim](https://github.com/neoclide/coc.nvim)

```json
{
  "languageserver": {
    "zathura": {
      "command": "zathura-language-server",
      "filetypes": [
        "zathurarc",
      ],
      "initializationOptions": {
        "method": "builtin"
      }
    }
  }
}
```

### [vim-lsp](https://github.com/prabirzathurarestha/vim-lsp)

```vim
if executable('zathura-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'zathura',
          \ 'cmd': {server_info->['zathura-language-server']},
          \ 'whitelist': ['zathurarc'],
          \ 'initialization_options': {
          \   'method': 'builtin',
          \ },
          \ })
  augroup END
endif
```

## [Neovim](https://neovim.io)

```lua
vim.api.nvim_create_autocmd({ "BufEnter" }, {
  pattern = { "zathurarc*" },
  callback = function()
    vim.lsp.start({
      name = "zathura",
      cmd = { "zathura-language-server" }
    })
  end,
})
```

## [Emacs](https://www.gnu.org/software/emacs)

```elisp
(make-lsp-client :new-connection
(lsp-stdio-connection
  `(,(executable-find "zathura-language-server")))
  :activation-fn (lsp-activate-on "zathurarc*")
  :server-id "zathura")))
```

## [Sublime](https://www.sublimetext.com)

```json
{
  "clients": {
    "zathura": {
      "command": [
        "zathura-language-server"
      ],
      "enabled": true,
      "selector": "source.zathura"
    }
  }
}
```
