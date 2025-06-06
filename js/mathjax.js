window.MathJax = {
    loader: {load: ['[tex]/physics']},
    tex: {
        inlineMath: [
            ["\\(", "\\)"]
        ],
        displayMath: [
            ["\\[", "\\]"]
        ],
        processEscapes: true,
        processEnvironments: true,
        packages: {'[+]': ['physics']}
    },
    options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
    }
};

document$.subscribe(() => {
    MathJax.typesetPromise()
})