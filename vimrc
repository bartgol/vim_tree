set nocompatible
filetype plugin indent on
syntax on

" Let pathogen handles plugins
execute pathogen#infect()

set nocompatible              " be iMproved, required
filetype off                  " required

" To ignore plugin indent changes, instead use:
filetype plugin on

" YouCompleteMe options
let g:ycm_global_ycm_extra_conf = '~/.vim/.ycm_extra_conf.py'
let g:ycm_clangd_binary_path = '~/workdir/libs/llvm/llvm-10.0.0-install'

" yankring options
let g:yankring_history_dir = '~/.vim/temp'

" nerdcommented options
let g:NERDSpaceDelims = 1

" make backspace and del keys work like most other apps
set backspace=2
:fixdel

" To enable 256 colors
set t_Co=256

" Set background
set background=light
highlight Normal ctermbg=256 ctermfg=46

" Turn on syntax highlight
syntax on

" Show relative line number
set relativenumber

" Always display file name
set ls=2

" Highlight current window
hi StatusLine gui=bold ctermfg=Blue

" Customize status line
set statusline=%<%f\ %h%w%m%r%y%=Row:%l/%L\ (%p%%)\ Col:%c%V

" Tab and spacing
set tabstop=2 softtabstop=2 textwidth=120 shiftwidth=2 expandtab
highlight ExtraWhitespace ctermbg=darkgreen guibg=lightgreen

" No re-tab Makefiles
autocmd BufNewFile,BufRead Makefile* setlocal noexpandtab
autocmd BufNewFile,BufRead makefile* setlocal noexpandtab
autocmd BufNewFile,BufRead MAKEFILE* setlocal noexpandtab

" Automatic re-tab
" if has("autocmd")
    " autocmd BufReadPost * if &modifiable | retab | endif
" endif

" Line numbering
highlight LineNr term=bold cterm=NONE ctermfg=DarkGrey ctermbg=NONE gui=NONE guifg=DarkGrey guibg=NONE
map <F6> :set number! <CR><Bar>:echo "Line Number: " . strpart("OffOn", 3 * &number, 3 )<CR>

" Check spelling English
if has("spell")
    map <F7> :set spell! spelllang=en_gb <CR><Bar>:echo "English Spell Check: " . strpart("OffOn", 3 * &spell, 3 )<CR>
endif

" Check spelling Italian
if has("spell")
    map <F8> :set spell! spelllang=it <CR><Bar>:echo "Italian Spell Check: " . strpart("OffOn", 3 * &spell, 3 )<CR>
endif

" Makes tilde file backups
set backup
if has('persistent_undo')
    "so is persistent undo ...
    set undofile
    "maximum number of changes that can be undone
    set undolevels=1000
    "maximum number lines to save for undo on a buffer reload
    set undoreload=10000
endif

" Match trailing white space, except when typing at the end of a line:
autocmd InsertEnter * match ExtraWhitespace /\s\+\%#\@<!$\| \t/
autocmd InsertLeave * match ExtraWhitespace /\s\+$/

" Autoremove trailing white space on save
" autocmd BufWritePre * :%s/\s\+$//e

" Search highlight
set hlsearch

" Incremental search
set incsearch

" Search ignores case only if all small caps
set ignorecase
set smartcase

" Bash-like filename completion
set wildmode=longest:full
set wildmenu

" Disable autocomment in new lines
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Set some of the parameter for the viminfo: the maximum
" number of previous edited file, disable highlight when
" re-open a file and define the viminfo file.
set viminfo='50,h,n~/.viminfo

" Store a ton of history (default is 20)
set history=1000

" set vim to chdir for each file
if exists('+autochdir')
    set autochdir
else
    autocmd BufEnter * silent! lcd %:p:h:gs/ /\\ /
endif

" Tell vim to ignore certain files patterns in netrw
let g:netrw_list_hide= '.*\.swp$,^\./$'
let g:netrw_hide=1
let g:netrw_keepdir=0

" Backup files location
set backup                    " keep a backup file
set undodir=~/.vim/_undos     " store undo files here
set backupdir=~/.vim/_backups " store backups here
set directory=~/.vim/_swaps   " store swap files here

" Tab navigation
nnoremap <C-Left> :tabprevious<CR>
nnoremap <C-Right> :tabnext<CR>

" Tabline colors, to be coherent with the status line colors
hi TabLineFill ctermfg=White ctermbg=White
hi TabLine ctermfg=White ctermbg=Black term=none cterm=none
hi TabLineSel ctermfg=White ctermbg=Blue term=bold cterm=bold

" Set the default color scheme
colorscheme elflord

" Activate rainbow highlight for c++ delimiters
" let g:rainbow_active=1

" Do not wrap text (i.e., break line if past textwidth)
set fo-=t

" Wait very little for combined commands
set timeoutlen=350

" Remove scratch preview window
set completeopt-=preview

" Remap some commands

" Normal mode
nnoremap ww :w<Enter>
nnoremap qa :qa<Enter>
nnoremap rr R
nnoremap wa :wa<Enter>
nnoremap sw cw
nnoremap QQ :q<Enter>
nnoremap <C-a> GVgg
nnoremap <C-o> :tabedit . <Enter>
nnoremap <C-z> u
nnoremap <C-t> :tabnew <Enter>

" Visual mode
vnoremap qq <Esc>
vnoremap i I
vnoremap ginc :YcmCompleter GoToInclude <Enter>
vnoremap gdec :YcmCompleter GoToDeclaration <Enter>
vnoremap gdef :YcmCompleter GoToDefinition <Enter>
vnoremap gt   :YcmCompleter GetType <Enter>
vnoremap fix  :YcmCompleter FixIt <Enter>

" Insert mode
inoremap qq <Esc>
" :inoremap <expr> <CR> pumvisible() ? "\<C-y><space>" : "\<C-g>u\<CR>"
