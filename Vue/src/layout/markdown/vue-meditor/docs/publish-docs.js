const shell = require('shelljs');

shell.cd('docs/.vuepress');
if (!shell.which('git')) {
    shell.exit(1);
}

shell.cp('README.md','dist');
shell.cd('dist');
shell.exec('git init');
shell.exec('git add .');
shell.exec('git commit -m "更新文档"');
shell.exec('git push -f git@github.com:zhaoxuhui1122/vue-markdown-docs.git  master');
